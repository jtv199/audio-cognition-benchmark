#!/usr/bin/env python3
"""
PDF Metadata Extractor
Extracts author, year, title, journal, DOI, and abstract from PDF files.
"""

import re
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Error: pdfplumber not installed. Install with: pip install pdfplumber")
    sys.exit(1)


def extract_doi(text):
    """Extract DOI from text."""
    # Common DOI patterns
    patterns = [
        r'DOI:\s*(10\.\d{4,}/[^\s]+)',
        r'doi:\s*(10\.\d{4,}/[^\s]+)',
        r'https?://doi\.org/(10\.\d{4,}/[^\s]+)',
        r'\b(10\.\d{4,}/[^\s]+)\b',
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            doi = match.group(1)
            # Clean up common trailing characters
            doi = re.sub(r'[.,;)\]]+$', '', doi)
            return doi
    return None


def extract_year(text):
    """Extract publication year from text."""
    # Look for 4-digit years between 1950-2030
    matches = re.findall(r'\b(19[5-9]\d|20[0-3]\d)\b', text[:500])
    if matches:
        # Return the first reasonable year found
        return matches[0]
    return None


def extract_metadata(pdf_path):
    """Extract metadata from first 2 pages of PDF."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Extract text from first 2 pages
            first_page = pdf.pages[0].extract_text() if len(pdf.pages) > 0 else ""
            second_page = pdf.pages[1].extract_text() if len(pdf.pages) > 1 else ""

            combined_text = first_page + "\n" + second_page

            # Try to extract metadata from PDF properties first
            metadata = pdf.metadata or {}

            # Split into lines for better parsing
            lines = first_page.split('\n')
            lines = [line.strip() for line in lines if line.strip()]

            # Extract DOI
            doi = extract_doi(combined_text)

            # Extract year
            year = extract_year(combined_text)

            # Try to identify title (usually one of the first few lines, often longer)
            title_candidates = []
            for i, line in enumerate(lines[:10]):
                if len(line) > 20 and not line.isupper() and not re.match(r'^[A-Z\s]+$', line):
                    title_candidates.append((i, line))

            title = title_candidates[0][1] if title_candidates else lines[0] if lines else "Unknown"

            # Try to find abstract
            abstract = None
            abstract_patterns = [r'abstract[:\s]+(.*?)(?:\n\n|introduction|keywords)',
                               r'ABSTRACT[:\s]+(.*?)(?:\n\n|INTRODUCTION|KEYWORDS)']
            for pattern in abstract_patterns:
                match = re.search(pattern, combined_text, re.IGNORECASE | re.DOTALL)
                if match:
                    abstract = match.group(1).strip()[:500]  # First 500 chars
                    break

            # Try to identify journal/conference
            journal = None
            journal_patterns = [
                r'(?:published in|journal|proceedings)[:\s]+([^\n]+)',
                r'([A-Z][a-z]+ (?:Journal|Conference|Proceedings)[^\n]+)',
            ]
            for pattern in journal_patterns:
                match = re.search(pattern, combined_text, re.IGNORECASE)
                if match:
                    journal = match.group(1).strip()
                    break

            # Try to identify authors (usually after title, before journal)
            authors = []
            for i, line in enumerate(lines[1:6]):
                # Look for lines with names (capitalized words, possibly with commas)
                if re.match(r'^[A-Z][a-z]+(?:\s+[A-Z]\.)?(?:\s+[A-Z][a-z]+)?(?:,\s*[A-Z].*)?$', line):
                    authors.append(line)

            authors_str = '; '.join(authors) if authors else lines[1] if len(lines) > 1 else "Unknown"

            return {
                'filename': pdf_path.name,
                'title': title,
                'authors': authors_str,
                'year': year,
                'journal': journal,
                'doi': doi,
                'abstract': abstract,
                'first_page_preview': '\n'.join(lines[:15])
            }

    except Exception as e:
        return {
            'filename': pdf_path.name,
            'error': str(e)
        }


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_metadata.py <pdf_file_or_directory>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if path.is_file():
        pdf_files = [path]
    elif path.is_dir():
        pdf_files = sorted(path.glob('*.pdf'))
    else:
        print(f"Error: {path} is not a valid file or directory")
        sys.exit(1)

    print(f"Processing {len(pdf_files)} PDF files...\n")
    print("=" * 80)

    for pdf_file in pdf_files:
        print(f"\n### {pdf_file.name}")
        print("-" * 80)

        metadata = extract_metadata(pdf_file)

        if 'error' in metadata:
            print(f"ERROR: {metadata['error']}")
            continue

        print(f"Title: {metadata['title']}")
        print(f"Authors: {metadata['authors']}")
        print(f"Year: {metadata['year'] or 'Not found'}")
        print(f"Journal: {metadata['journal'] or 'Not found'}")
        print(f"DOI: {metadata['doi'] or 'Not found'}")

        if metadata['abstract']:
            print(f"\nAbstract (preview):\n{metadata['abstract'][:300]}...")

        print(f"\nFirst page preview:")
        print(metadata['first_page_preview'])
        print("=" * 80)


if __name__ == '__main__':
    main()
