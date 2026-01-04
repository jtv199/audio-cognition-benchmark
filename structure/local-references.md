# Local References

**Last Updated**: December 29, 2025

This document catalogs all research papers that have been downloaded and processed locally. Papers are organized by project area and include importance ratings, relevance to the 4 Pillars, and processing status.

---

## Benchmark Papers (Core Theoretical Framework)

### Pillar 1: Ecological Psychology (Physics View)

| Importance | Reference | Notes | File Path | Status |
|------------|-----------|-------|-----------|--------|
| 5/5 | Gaver, W. W. (1993). What in the World Do We Hear? An Ecological Approach to Auditory Event Perception. *Ecological Psychology*. | **Pillar 1 Foundation**. Proposes taxonomy of everyday listening based on physics of sound-producing events. Three categories: Vibrating Solids (impact, scraping, rolling), Liquids (dripping, pouring, splashing), Aerodynamics (explosions, hissing). Critical for "Physics Engine" reasoning tasks. | `papers/benchmark/Gaver_1993_WhatInTheWorldDoWeHear.pdf` | ✓ Read & Summarized |

### Pillar 2: Computational Auditory Scene Analysis (Grouping View)

| Importance | Reference | Notes | File Path | Status |
|------------|-----------|-------|-----------|--------|
| 5/5 | Bregman, A. S. (1990). *Auditory Scene Analysis: The Perceptual Organization of Sound*. MIT Press. DOI: 10.7551/mitpress/1486.001.0001 | **Pillar 2 Foundation**. Complete theoretical framework for auditory scene analysis. Defines primitive vs. schema-based segregation. Essential for "Attention Engine" and stream segregation tasks. Book available in chapters below. | Multiple files (see chapters) | ✓ Read & Summarized |
| 5/5 | Bregman (1990) - Preface | Historical context for ASA research. Discusses origins of "auditory stream segregation" (later "streaming" by Neisser). | `papers/benchmark/Bregman_1990_ASA_Preface.pdf` | ✓ Cataloged |
| 5/5 | Bregman (1990) - Chapter 1: The Auditory Scene | Foundational chapter defining perceptual vs. ecological questions in audition. Establishes the problem of auditory scene analysis. | `papers/benchmark/Bregman_1990_ASA_Ch1_AuditoryScene.pdf` | ✓ Cataloged |
| 5/5 | Bregman (1990) - Chapter 3: Integration of Simultaneous Auditory Components | Sequential vs. spectral grouping mechanisms. Critical for understanding how concurrent sounds are partitioned into perceptual streams. | `papers/benchmark/Bregman_1990_ASA_Ch3_SimultaneousIntegration.pdf` | ✓ Cataloged |
| 5/5 | Bregman (1990) - Chapter 4: Schema-Based Segregation and Integration | Top-down processing and knowledge-based analysis. Attention and learning contributions to auditory organization. | `papers/benchmark/Bregman_1990_ASA_Ch4_SchemaBasedSegregation.pdf` | ✓ Cataloged |
| 5/5 | Bregman (1990) - Chapter 6: Auditory Organization in Speech Perception | Application of primitive and schema-based processes to speech. Distinction between primitive grouping (universal) and schema-based grouping (speech-specific). | `papers/benchmark/Bregman_1990_ASA_Ch6_SpeechPerception.pdf` | ✓ Cataloged |
| 5/5 | Bregman (1990) - Chapter 8: Summary and Conclusions | Comprehensive summary of what is known and unknown about ASA. Key conclusions and future directions. | `papers/benchmark/Bregman_1990_ASA_Ch8_Conclusions.pdf` | ✓ Cataloged |
| 4/5 | Bregman (1990) - Notes | Reference notes with citations to supporting experimental work. Includes key studies by van Noorden, Deutsch, Treisman, Warren, and others. | `papers/benchmark/Bregman_1990_ASA_Notes.pdf` | ✓ Cataloged |
| 3/5 | Bregman (1990) - Front Matter | Title page and publication information. | `papers/benchmark/Bregman_1990_ASA_FrontMatter.pdf` | ✓ Cataloged |

### Pillar 3: Cognitive Neuroscience (Architecture View)

| Importance | Reference | Notes | File Path | Status |
|------------|-----------|-------|-----------|--------|
| 5/5 | Rauschecker, J. P., & Scott, S. K. (2009). Maps and streams in the auditory cortex: nonhuman primates illuminate human speech processing. *Nature Neuroscience*, 12(6), 718-724. DOI: 10.1038/nn.2331 | **Pillar 3 Foundation**. Dual Stream Hypothesis for auditory processing. Ventral "What" stream (object identification) vs. Dorsal "Where/How" stream (spatial localization, sensorimotor). Critical for benchmark structural validity - ensures separation of recognition vs. spatial/action tasks. | `papers/benchmark/Rauschecker_2009_MapsAndStreams.pdf` | ✓ Read & Summarized |

### Pillar 4: Clinical Audiology (Stress-Test View)

| Importance | Reference | Notes | File Path | Status |
|------------|-----------|-------|-----------|--------|
| 3/5 | Katz, J. (2025). The Buffalo Model—a comprehensive approach to evaluate and remediate auditory processing disorders. *Audiology Today*, 37(1), 18-25. | Modern retrospective article about the Buffalo Model (original: Katz 1992). Describes 4 diagnostic categories: Decoding, Tolerance-Fading Memory, Integration, Organization. Useful for understanding model development, but **NOT the original 1992 foundational paper**. | `papers/benchmark/Katz_2025_BuffaloModelRetrospective.pdf` | ✓ Read & Summarized |

### General Frameworks

| Importance | Reference | Notes | File Path | Status |
|------------|-----------|-------|-----------|--------|
| 5/5 | Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2024). Cognitive Architectures for Language Agents. *Transactions on Machine Learning Research*. | **Foundational Framework**. Proposes CoALA (Cognitive Architectures for Language Agents). It's an 'agentic OS' that orchestrates an LLM using explicit Memory modules (Working, Episodic, Semantic, Procedural) and a Decision Cycle (perceive-plan-act). Highly relevant for designing AI architectures for audio reasoning tasks. | `papers/benchmark/Sumers_2024_CognitiveArchitecturesForLanguageAgents.pdf` | ✓ Read & Summarized |

---

## Supporting Papers

### Critical Reviews & Meta-Analysis

| Importance | Reference | Notes | File Path | Status |
|------------|-----------|-------|-----------|--------|
| 3/5 | Nicolson, R. I. (1990). Book Review: Auditory Scene Analysis: The Perceptual Organization of Sound by Albert S. Bregman. *Journal of Environmental Psychology*, 10(3), 293-296. | Scholarly review of Bregman's ASA book. Provides external perspective on ASA theory's contributions and limitations. Useful for understanding reception and critique of foundational work. | `papers/benchmark/Nicolson_1990_BregmanASABookReview.pdf` | ✓ Read & Summarized |

---

## Missing Core Papers

These foundational papers are referenced in the project but not yet acquired locally:

| Priority | Reference | Notes | Status |
|----------|-----------|-------|--------|
| HIGH | Katz, J. (1992). Classification of auditory processing disorders. In J. Katz, N. Stecker, & D. Henderson (Eds.), *Central Auditory Processing: A Transdisciplinary View* (pp. 81-91). Mosby Year Book. | **Original Buffalo Model paper** - Currently only have 2025 retrospective. This is the foundational Pillar 4 paper. | ⚠ Not acquired |
| MEDIUM | Cherry, E. C. (1953). Some experiments on the recognition of speech, with one and with two ears. *The Journal of the Acoustical Society of America*, 25(5), 975-979. | Original "Cocktail Party Effect" paper - Referenced in Layer 2 (Selective Attention) task design. | ⚠ Not acquired |
| MEDIUM | Broadbent, D. E. (1958). *Perception and Communication*. Pergamon Press. | Divided Attention theory - Referenced in Layer 2 (Cognitive Control) task design. | ⚠ Not acquired |
| LOW | Scherer, K. R. (2003). Vocal communication of emotion: A review of research paradigms. *Speech Communication*, 40(1-2), 227-256. | Paralinguistics and emotion recognition - Referenced in Layer 3 (Inferential) task design. | ⚠ Not acquired |
| LOW | Ballas, J. A. (1993). Common factors in the identification of an assortment of brief everyday sounds. *Journal of Experimental Psychology: Human Perception and Performance*, 19(2), 250-267. | Causal reasoning from environmental sounds - Referenced in Layer 3 (Inferential) task design. | ⚠ Not acquired |

---

## Statistics

**Total Papers Processed**: 12
- Core Pillar Papers: 2 (Gaver 1993, Rauschecker 2009)
- Bregman ASA Chapters: 8 (comprehensive Pillar 2 coverage)
- Supporting Papers: 2 (Katz 2025 retrospective, Nicolson 1990 review)

**Pillar Coverage**:
- ✅ Pillar 1 (Ecological): Complete (Gaver 1993)
- ✅ Pillar 2 (CASA): Complete (Bregman 1990 - 8 chapters)
- ✅ Pillar 3 (Neuro): Complete (Rauschecker & Scott 2009)
- ⚠ Pillar 4 (Clinical): Incomplete (Need original Katz 1992 paper)

---

## Notes

- All files follow academic naming convention: `Author_Year_ShortTitle.pdf`
- All processed files located in `papers/benchmark/`
- Metadata extraction completed using `extract_pdf_metadata.py` script
- Full identification summary available in `.claude/temp/pdf_identification_summary.md`
