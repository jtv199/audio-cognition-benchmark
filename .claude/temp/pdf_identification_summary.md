# PDF Identification Summary

Generated: 2025-12-08
Tool: extract_pdf_metadata.py

---

## papers/input/ (2 files)

### 1. EBSCO-FullText-12_08_2025 (1).pdf
**Identified as**: Rauschecker, J. P., & Scott, S. K. (2009). Maps and streams in the auditory cortex: nonhuman primates illuminate human speech processing.

**Details**:
- **Journal**: Nature Neuroscience
- **DOI**: 10.1038/nn.2331
- **Year**: 2009 (needs manual verification)
- **Importance**: 5/5 (Pillar 3 - Cognitive Neuroscience)
- **Relevance**: Dual Stream Hypothesis (Ventral "What" vs. Dorsal "Where/How")

**Recommended filename**: `Rauschecker_2009_MapsAndStreams.pdf`

**Notes**: This is one of the 4 core pillar papers! Foundational for the Architecture View.

---

### 2. EBSCO-FullText-12_08_2025.pdf
**Identified as**: Katz, J. (2025). The Buffalo Model—a comprehensive approach to evaluate and remediate auditory processing disorders.

**Details**:
- **Journal**: Audiology Today
- **Year**: 2025 (Jan/Feb)
- **Importance**: 3/5 (modern overview, not the original 1992 paper)
- **Relevance**: Related to Pillar 4 (Clinical Audiology), but this is a retrospective article

**Recommended filename**: `Katz_2025_BuffaloModelRetrospective.pdf`

**Notes**: This appears to be a recent article ABOUT the Buffalo Model, not the original 1992 foundational paper. Still useful for understanding the model's development and application, but lower importance than the original. The original paper is: Katz, J. (1992). Classification of auditory processing disorders. In J. Katz, N. Stecker, & D. Henderson (Eds.), *Central Auditory Processing: A Transdisciplinary View* (pp. 81-91). Mosby Year Book.

---

## papers/benchmark/ (10 files)

### Bregman Chapters (ISBN: 9780262269209)

**Book**: Bregman, A. S. (1990). *Auditory Scene Analysis: The Perceptual Organization of Sound*. MIT Press.
**DOI**: 10.7551/mitpress/1486.001.0001
**Importance**: 5/5 (Pillar 2 - CASA)

#### 3. 9780262269209_fa.pdf
**Chapter**: Preface
**Recommended filename**: `Bregman_1990_ASA_Preface.pdf`

#### 4. 9780262269209_caa.pdf
**Chapter**: Chapter 1 - The Auditory Scene
**Recommended filename**: `Bregman_1990_ASA_Ch1_AuditoryScene.pdf`

#### 5. 9780262269209_cac.pdf
**Chapter**: Chapter 3 - Integration of Simultaneous Auditory Components
**Recommended filename**: `Bregman_1990_ASA_Ch3_SimultaneousIntegration.pdf`

#### 6. 9780262269209_cad.pdf
**Chapter**: Chapter 4 - Schema-Based Segregation and Integration
**Recommended filename**: `Bregman_1990_ASA_Ch4_SchemaBasedSegregation.pdf`

#### 7. 9780262269209_caf.pdf
**Chapter**: Chapter 6 - Auditory Organization in Speech Perception
**Recommended filename**: `Bregman_1990_ASA_Ch6_SpeechPerception.pdf`

#### 8. 9780262269209_cah (1).pdf
**Chapter**: Chapter 8 - Summary and Conclusions
**Recommended filename**: `Bregman_1990_ASA_Ch8_Conclusions.pdf`

#### 9. 9780262269209_cai.pdf
**Section**: Notes
**Recommended filename**: `Bregman_1990_ASA_Notes.pdf`

#### 10. f010002_9780262269209.pdf
**Section**: Front matter or figure
**Recommended filename**: `Bregman_1990_ASA_FrontMatter.pdf`

---

### Other Papers

#### 11. 1-s2.0-S0272494405801914-main.pdf
**Identified as**: Book review (appears to be reviewing a book on societal psychology)
**Importance**: 1/5 (likely not relevant)
**Recommended action**: Review manually; may be misidentified or irrelevant

**Notes**: The Elsevier DOI pattern (1-s2.0-...) suggests this is from ScienceDirect, but the extracted text shows a book review about political psychology/genocide, not audio cognition. This may need manual inspection.

---

#### 12. Gaver_1993_WhatInTheWorldDoWeHear.pdf
**Status**: ✅ ALREADY CORRECTLY NAMED

**Details**:
- **Authors**: William W. Gaver
- **Year**: 1993
- **Title**: What in the World Do We Hear? An Ecological Approach to Auditory Event Perception
- **Affiliation**: Rank Xerox Cambridge EuroPARC
- **Importance**: 5/5 (Pillar 1 - Ecological Psychology)
- **Relevance**: Foundational taxonomy for everyday listening (Vibrating Solids, Liquids, Aerodynamics)

**No action needed** - this file is properly named and already processed.

---

## Summary Statistics

- **Total PDFs**: 12
- **Already correctly named**: 1 (Gaver)
- **Bregman chapters**: 8
- **Core pillar papers**: 2 (Rauschecker, Gaver)
- **Related papers**: 1 (Katz 2025)
- **Needs review**: 1 (Elsevier book review)

---

## Action Items

### papers/input/
1. Rename `EBSCO-FullText-12_08_2025 (1).pdf` → `Rauschecker_2009_MapsAndStreams.pdf`
2. Rename `EBSCO-FullText-12_08_2025.pdf` → `Katz_2025_BuffaloModelRetrospective.pdf`
3. Move both to `papers/benchmark/`

### papers/benchmark/
4. Rename all Bregman chapters (8 files) using convention above
5. Review `1-s2.0-S0272494405801914-main.pdf` manually - may need to be moved out or deleted
6. Keep `Gaver_1993_WhatInTheWorldDoWeHear.pdf` as-is (already correct)

---

## Notes for Documentation

### Pillar Coverage
- ✅ **Pillar 1 (Ecological Psychology)**: Gaver 1993 - present and correctly named
- ✅ **Pillar 2 (CASA)**: Bregman 1990 - 8 chapters present (comprehensive coverage!)
- ✅ **Pillar 3 (Cognitive Neuroscience)**: Rauschecker & Scott 2009 - identified, needs renaming
- ⚠️ **Pillar 4 (Clinical Audiology)**: Katz 1992 original paper NOT present; only 2025 retrospective article

### Missing Core Papers
- **Katz, J. (1992)** - Original Buffalo Model paper not found in local files
- Should be acquired if possible for complete coverage of Pillar 4

---

## Metadata Extraction Quality Notes

**Script Performance**:
- ✅ DOI extraction: Good (found DOIs for Rauschecker, all Bregman chapters)
- ⚠️ Year extraction: Moderate (missed some years, needs manual verification)
- ⚠️ Title extraction: Variable (worked well for standalone papers, less reliable for book chapters)
- ⚠️ Author extraction: Needs improvement (often captured first line instead of author names)

**Recommendation**: Use script output as a starting point, but manually verify all metadata before final documentation.
