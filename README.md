# Audio Cognition Benchmark

A comprehensive taxonomy and analysis of audio cognition tasks across multiple AI benchmarks, including AIR-Bench, AudioBench, and MMAU-Pro.

## Overview

This project analyzes and categorizes audio cognition tasks by:
- Referencing multiple cognitive frameworks and taxonomies
- Mapping tasks across different benchmark datasets
- Identifying gaps in current benchmark coverage
- Establishing consistent task numbering and classification

## Important Files

### [`./output/combined-taxonomy-table.md`](output/combined-taxonomy-table.md)
**Purpose**: Comprehensive taxonomy of audio cognition tasks

This file contains:
- The full range of auditory cognition tasks organized by cognitive layers (Perceptual, Cognitive Control, Inferential)
- Coverage analysis showing which benchmarks (AIR-Bench, AudioBench, MMAU-Pro, WavCaps) test each capability
- Task classifications based on multiple cognitive frameworks:
  - **P1**: Original 6 email tasks
  - **P2**: CASA (Computational Auditory Scene Analysis) framework
  - **P3**: Neuroscience "What/Where/How" pathways
  - **P4**: Clinical assessment perspectives
- Potential gaps in current benchmark coverage with priority ratings
- Framework distribution analysis

**Use this file to**: Understand the breadth of audio cognition capabilities and see which benchmarks cover specific cognitive tasks.

---

### [`./output/benchmark-tasks.md`](output/benchmark-tasks.md)
**Purpose**: Reference guide for specific benchmark tasks

This file catalogs:
- **B1 (AIR-Bench)**: Task IDs B1.T1-T19 covering 19 audio/speech understanding tasks
- **B2 (AudioBench)**: Task IDs B2.T1-T8 covering 8 core audio understanding capabilities
- **B3 (MMAU-Pro)**: Task IDs B3.T1-T38 covering 38 skills across music, sound, and speech domains
  - Music Domain: B3.T1-T14 (perceptual + reasoning)
  - Sound Domain: B3.T15-T22 (perceptual + reasoning)
  - Speech Domain: B3.T23-T38 (perceptual + reasoning)
  - Plus 7 novel testing dimensions (long-form audio, multi-audio reasoning, spatial audio, etc.)

**Use this file to**: Look up specific benchmark task definitions and see how tasks are referenced in other documents (e.g., "B3.T18" refers to MMAU-Pro's Acoustic Scene Reasoning task).

---

### [`./.claude/`](.claude/)
**Purpose**: Daily research session summaries

This directory contains:
- **Date-stamped markdown files** (e.g., `2025-12-09.md`) documenting each day's research progress
- Session summaries including:
  - Tasks completed
  - Files modified
  - Key insights and findings
  - Context for future sessions
- Command history and methodology notes

**Use this directory to**: Understand the research process, see what work was done on specific dates, and get context for how the taxonomy was developed.

## Project Structure

```
audio-cognition-benchmark/
├── output/               # Main deliverables
│   ├── combined-taxonomy-table.md
│   ├── benchmark-tasks.md
│   ├── taxonomy-overview.md
│   └── ...
├── papers/              # Source research papers
│   ├── benchmark/       # Benchmark papers (MMAU-Pro, etc.)
│   └── extracted_text/  # Text extractions from PDFs
├── .claude/             # Daily session summaries
├── references.md        # Bibliography and citations
└── README.md           # This file
```

## Key Findings

### Benchmark Coverage Summary
- **MMAU-Pro (B3)**: Most comprehensive with 38 explicitly defined skills + 7 novel testing dimensions
- **AIR-Bench (B1)**: 19 tasks focused on audio/speech understanding
- **AudioBench (B2)**: 8 core audio understanding capabilities

### Identified Gaps (High Priority)
1. **Phonemic Restoration** (5/5) - Not covered in any benchmark
2. **Auditory Stroop Test** (4/5) - Cross-dimensional conflict resolution not tested

## Task ID Format

All benchmark tasks use a consistent B#.T# format:
- **B1.T#**: AIR-Bench tasks (B1.T1-T19)
- **B2.T#**: AudioBench tasks (B2.T1-T8)
- **B3.T#**: MMAU-Pro tasks (B3.T1-T38)

## Contributing

This is a research project documenting audio cognition benchmarks. For questions or suggestions, please open an issue.

## License

Research and documentation project. See individual papers for their respective licenses.
