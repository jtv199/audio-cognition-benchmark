#!/usr/bin/env python3
"""
Extract first 2000 words from each PDF in papers/benchmark/
"""

import os
import sys
from pathlib import Path

try:
    import pypdf
except ImportError:
    print("pypdf not installed. Installing...")
    os.system("pip install pypdf")
    import pypdf

def extract_first_n_words(pdf_path, n_words=2000):
    """Extract first n words from a PDF"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = pypdf.PdfReader(file)

            text = ""
            word_count = 0

            for page in pdf_reader.pages:
                page_text = page.extract_text()
                words = page_text.split()

                for word in words:
                    if word_count >= n_words:
                        return text
                    text += word + " "
                    word_count += 1

                text += "\n\n"  # Page break

            return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def main():
    benchmark_dir = Path("papers/benchmark")
    output_dir = Path("papers/extracted_text")
    output_dir.mkdir(exist_ok=True)

    if not benchmark_dir.exists():
        print(f"Directory {benchmark_dir} not found")
        return

    pdf_files = list(benchmark_dir.glob("*.pdf"))

    if not pdf_files:
        print(f"No PDF files found in {benchmark_dir}")
        return

    print(f"Found {len(pdf_files)} PDF files")

    for pdf_file in sorted(pdf_files):
        print(f"\nProcessing: {pdf_file.name}")

        text = extract_first_n_words(pdf_file, n_words=2000)

        # Save to text file
        output_file = output_dir / f"{pdf_file.stem}_first2000words.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Source: {pdf_file.name}\n")
            f.write(f"First 2000 words extracted\n")
            f.write("=" * 80 + "\n\n")
            f.write(text)

        word_count = len(text.split())
        print(f"  Extracted {word_count} words → {output_file.name}")

    print(f"\n✓ All extractions saved to {output_dir}/")

if __name__ == "__main__":
    main()
