# Research Commands & Procedures

**Last Updated**: December 8, 2025

---

## Processing PDF Research Files

**Command**: "Process PDF research files"

### Definition

"Processing" a PDF research file means performing a systematic extraction and cataloging workflow to integrate the paper into the project's knowledge base.

### Procedure

#### Step 1: Read & Identify
- **Read the PDF** to extract key metadata:
  - Author(s)
  - Publication year
  - Full title
  - Journal/conference/publisher
  - DOI (if available)
  - Abstract or key concepts

#### Step 2: Classify & Rate
- **Determine relevance** to the 4 Pillars:
  1. Ecological Psychology (Physics View)
  2. CASA (Grouping View)
  3. Cognitive Neuroscience (Architecture View)
  4. Clinical Audiology (Stress-Test View)
- **Assign importance rating** (X/5):
  - 5/5: Foundational (defines core framework)
  - 4/5: High importance (essential concepts)
  - 3/5: Medium importance (supporting evidence)
  - 2/5: Low importance (peripheral)
  - 1/5: Reference only (context)
- **Map to task layers** (if applicable):
  - Layer 1: Foundational (Perception & Schema)
  - Layer 2: Cognitive Control (Attention & Load)
  - Layer 3: Inferential (Reasoning & Theory of Mind)

#### Step 3: Rename & Organize
- **Rename file** using academic convention:
  ```
  Author_Year_ShortTitle.pdf
  ```
  Examples:
  - `Gaver_1993_WhatInTheWorldDoWeHear.pdf`
  - `Bregman_1990_AuditorySceneAnalysis_Chapter1.pdf`
  - `Cherry_1953_CocktailPartyEffect.pdf`

- **Move to appropriate directory**:
  - `papers/benchmark/` - Core theoretical papers
  - `papers/tokenizer/` - Audio tokenization/representation
  - `papers/tasks/` - Task design and evaluation (future)

#### Step 4: Update Documentation
- **Update `local-references.md`**:
  - Add to appropriate section (Benchmark Papers, Tokenizer Papers, etc.)
  - Include: Importance | Reference | Notes | File Path | Status
  - Mark status as "✓ Read & Summarized"

- **Update `references.md`** (if paper is important enough):
  - Add to appropriate category
  - Include: Importance | Reference | Notes | File

- **Add notes to session log** (`.claude/YYYY-MM-DD.md`):
  - Key findings
  - Relevance to project
  - Connections to other papers

#### Step 5: Extract & Synthesize
- **Identify key concepts** to extract:
  - Taxonomies or frameworks
  - Task designs
  - Evaluation methods
  - Theoretical contributions
  - Limitations or gaps

- **Note connections**:
  - How does this paper relate to the 4 Pillars?
  - Does it support, extend, or contradict existing framework?
  - What new perspectives does it offer?

---

## Processing Workflow Summary

```
INPUT: Unprocessed PDF in papers/input/
  ↓
STEP 1: Read → Extract metadata & abstract
  ↓
STEP 2: Classify → Rate importance, map to pillars/layers
  ↓
STEP 3: Rename → Author_Year_ShortTitle.pdf
  ↓
STEP 4: Move → papers/benchmark/ (or other appropriate folder)
  ↓
STEP 5: Document → Update local-references.md & references.md
  ↓
OUTPUT: Processed, cataloged, integrated paper
```

---

## Special Cases

### Book Chapters
- Format: `Author_Year_BookTitle_ChapterName.pdf`
- Example: `Bregman_1990_AuditorySceneAnalysis_Ch2_PrimitiveSegregation.pdf`

### Multiple Authors
- Use first author only: `FirstAuthor_Year_ShortTitle.pdf`
- Example: `Rauschecker_2009_MapsAndStreams.pdf` (Rauschecker & Scott)

### Duplicate Years (Same Author)
- Add letter suffix: `Author_YEARa_Title.pdf`, `Author_YEARb_Title.pdf`
- Example: `Gaver_1993a_WhatInTheWorldDoWeHear.pdf`

### ArXiv Preprints
- Use ArXiv number in title: `FirstAuthor_Year_ShortTitle_arXivNUMBER.pdf`
- Example: `Smith_2025_AudioTokenization_arXiv2505.16845.pdf`

### Unknown/Unidentified Papers
- Keep in `papers/input/` or mark as "⚠ Needs Review" in local-references
- Process identification separately before full processing

---

## Quality Checks

Before marking a paper as "✓ Read & Summarized":
- [ ] Metadata fully extracted (authors, year, title, journal)
- [ ] Importance rating assigned with justification
- [ ] Relevance to 4 Pillars documented
- [ ] File renamed following convention
- [ ] File moved to appropriate directory
- [ ] `local-references.md` updated
- [ ] Key concepts extracted and noted

---

## Tools & Assistants

### For Deep Analysis
- **Gemini**: Generate abstracts, identify linking papers
- **Connected Papers**: Explore citation networks
- **Claude Code (Me)**: Read PDFs, extract metadata, organize files

### For Citation Management
- **Google Scholar**: Find full citations
- **DOI lookup**: Resolve digital object identifiers
- **CrossRef**: Validate citation metadata

---

*This document defines standard operating procedures for research file management.*
