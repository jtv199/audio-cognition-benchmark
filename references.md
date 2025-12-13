# References

## Benchmark Papers

| Importance | Reference | Notes | File |
|------------|-----------|-------|------|
| 5/5 | Gaver, W. W. (1993). What in the world do we hear?: An ecological approach to auditory event perception. *Ecological Psychology*, 5(1), 1-29. | Foundational taxonomy for everyday listening. Core framework for Layer 1 (Physics View). Establishes categories: Vibrating Solids, Liquids, Aerodynamics. | `papers/benchmark/Gaver_1993_WhatInTheWorldDoWeHear.pdf` |
| 5/5 | Bregman, A. S. (1990). *Auditory Scene Analysis: The Perceptual Organization of Sound*. MIT Press. | Foundational work on Computational Auditory Scene Analysis (CASA). Defines Primitive vs. Schema-based segregation. Essential for attention tasks. | - |
| 5/5 | Rauschecker, J. P., & Scott, S. K. (2009). Maps and streams in the auditory cortex: nonhuman primates illuminate human speech processing. *Nature Neuroscience*, 12(6), 718-724. | Dual Stream Hypothesis (Ventral "What" vs. Dorsal "Where/How"). Provides neuroanatomical validation for separating task types. | - |
| 5/5 | Katz, J. (1992). Classification of auditory processing disorders. In J. Katz, N. Stecker, & D. Henderson (Eds.), *Central Auditory Processing: A Transdisciplinary View* (pp. 81-91). Mosby Year Book. | Buffalo Model for Clinical Audiology. Defines Decoding, Tolerance-Fading Memory, Integration. Framework for stress-testing AI models. | - |

## Cognitive Psychology References

| Importance | Reference | Notes | File |
|------------|-----------|-------|------|
| 4/5 | Cherry, E. C. (1953). Some experiments on the recognition of speech, with one and with two ears. *The Journal of the Acoustical Society of America*, 25(5), 975-979. | Original "Cocktail Party Effect" study. Foundation for selective attention tasks in Layer 2. | - |
| 4/5 | Broadbent, D. E. (1958). *Perception and Communication*. Pergamon Press. | Filter theory of attention. Basis for divided attention tasks. | - |
| 4/5 | Scherer, K. R. (2003). Vocal communication of emotion: A review of research paradigms. *Speech Communication*, 40(1-2), 227-256. | Framework for paralinguistics and prosodic interpretation. Essential for Layer 3 inferential tasks. | - |
| 3/5 | Ballas, J. A. (1993). Common factors in the identification of an assortment of brief everyday sounds. *Journal of Experimental Psychology: Human Perception and Performance*, 19(2), 250-267. | Causal reasoning from environmental sounds. Supports narrative sequence tasks. | - |
| 4/5 | Baldwin, C. L. (2012). Auditory tasks in cognitive research. In *Auditory Cognition and Human Performance* (Chapter 6). CRC Press. | Comprehensive review of auditory tasks across cognitive domains. Critical emphasis on mental workload, presentation level (PL), and sensory-cognitive interaction. Covers working memory (listening span, n-back), attention (dichotic listening, PRP), and neuropsychological assessments (PASAT, RAVLT). Essential methodological guidance for auditory benchmark design. | `papers/Baldwin_Auditory_Tasks_in_Cognitive_Research_Chapter6.pdf` <br> Summary: `papers/reference-texts/Baldwin_2012_Auditory_Tasks_in_Cognitive_Research_Summary.md` |

## Existing AI Audio Benchmarks

| Importance | Reference | Notes | File |
|------------|-----------|-------|------|
| 4/5 | AIR-Bench | Foundation vs. Chat tiers. Introduces "Mixed Audio" tasks. Key competitor for comparison. | - |
| 4/5 | AudioBench | Standardizes audio tasks. Introduces "Speech Instruction" (spoken commands). | - |
| 3/5 | MMAU | Focuses on "Expert Reasoning" with strict Multiple Choice format. Tests role mapping and emotion flip. | - |
| 5/5 | Google MSEB (Massive Sound Embedding Benchmark) (2024+) | Tests 8 core capabilities: retrieval, reasoning, classification, transcription, segmentation, clustering, reranking, reconstruction. Includes Simple Voice Questions dataset (177k multilingual queries, 26 locales). Unique focus: single general-purpose embedding for all tasks. Model-agnostic evaluation framework. | Blog: https://research.google/blog/from-waveforms-to-wisdom-the-new-benchmark-for-auditory-intelligence/ |

## To Be Added

| Category | Status |
|----------|--------|
| Spatial Audio Research | Excluded from current scope (requires binaural data) |
| Music Cognition | Excluded from current scope (too specialized) |
| Low-Level Psychoacoustics | Excluded from current scope (trivial for models) |

---

*Last Updated: December 12, 2025*
