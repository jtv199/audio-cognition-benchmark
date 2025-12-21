# Changelog

## 2025-12-21

### Added
- **benchmark-tasks.md**: Added B4: MMAR benchmark (Ma et al., 2025)
  - 1,000 audio-question-answer triplets for deep reasoning evaluation
  - 4 hierarchical layers: Signal, Perception, Semantic, Cultural
  - 16 sub-categories extracted from Appendix A
  - Processed PDF from `input/2505.13032v1.pdf` → `papers/benchmark/Ma_2025_MMAR_arXiv2505.13032.pdf`
  - Extracted text saved to `papers/extracted_text/MMAR_2505.13032v1.txt`
- **task-database/tasks.yaml**: Added B4 (MMAR) tasks B4.T1-B4.T16
  - Signal Layer: T1-T3 (Acoustic Quality Analysis, Anomaly Detection, Audio Difference Analysis)
  - Perception Layer: T4-T9 (Spatial, Temporal, Correlation, Counting, Music Theory, Environmental)
  - Semantic Layer: T10-T12 (Content Analysis, Emotion/Intention, Speaker Analysis)
  - Cultural Layer: T13-T16 (Culture, Imagination, Aesthetic, Professional Knowledge)

### Changed
- **commands.md**: Removed "4 Pillars" classification system (Ecological Psychology, CASA, Cognitive Neuroscience, Clinical Audiology) - no longer used for paper classification
- Updated processing workflow to focus on importance ratings and task layers only
- Changed `papers/input/` references to `input/` to reflect new folder structure

