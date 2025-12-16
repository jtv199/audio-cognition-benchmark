# Cognitive Auditory Benchmark (CAB) Task List - MMAU-Pro Coverage Analysis

**Generated**: December 13, 2025
**Purpose**: Map clinical auditory cognition tests (with healthy adult norms) to MMAU-Pro benchmark coverage

---

## Overview

This document cross-references standardized clinical tests used for audio processing assessment in healthy adults against MMAU-Pro tasks. These tests have verified human baseline scores and stress cognitive mechanisms (working memory, selective attention, temporal resolution) that current AI audio benchmarks may not explicitly test.

---

## CAB Task List with MMAU-Pro Coverage

| CAB Task Name | Specific Example (Input/Instruction) | Healthy Human Score / Limit | Importance | Potentially Related MMAU-Pro Test |
|---------------|--------------------------------------|----------------------------|------------|-----------------------------------|
| **PASAT-AI** (Paced Auditory Serial Addition) | **Input:** Stream of digits every 2.0s. **Task:** "Add the last two digits heard." | **~44-65% Accuracy** at 2.0s pacing. Performance drops ~15-20% from 3.0s to 2.0s intervals. [1] | **5/5** | ⚠ **Partial:** B3.T32 (Quantitative Reasoning - Counting/Arithmetic) + Long-form audio dimension. *Gap: No serial updating task with paced timing.* |
| **Forced-Left Dichotic Listening** | **Input:** Different CV syllables (/ba/, /ga/) in each ear. **Task:** "Ignore Right ear, report Left ear." | **~64-73% Accuracy** (CV syllables). Digit tests easier (~85%), but CV syllables reveal cognitive bottleneck. [2] | **5/5** | ⚠ **Partial:** B3.T4 (Spatial Sound Perception) + 3D Spatial Audio dimension + B3.T29 (Speech Activity & Turn-Taking). *Gap: No explicit ear-inhibition/selective attention task.* |
| **QuickSIN** (Informational Masking) | **Input:** Sentences in 4-talker babble. **Task:** Identify keywords. | **SNR-50: +2.0 dB**. Signal must be 2dB louder than noise for 50% correct. Scores > +3dB indicate deficit. [3] | **5/5** | ⚠ **Partial:** Voice-Chat QA dimension + B3.T29 (Speech Activity & Turn-Taking) + Multi-audio Reasoning dimension. *Gap: No clinical SNR measurement; no explicit "select target from babble" task.* |
| **Time-Compressed Speech** | **Input:** Speech accelerated to CR 0.4 (~2.5x speed). **Task:** Transcribe sentences. | **~100% Accuracy** until CR 0.4, then cliff to **<50%** at CR 0.3. [4] | **4/5** | ✗ **Not Covered:** No time-compressed/accelerated speech tasks in MMAU-Pro. |
| **Interrupted "Gated" Speech** | **Input:** Speech interrupted by silence at 2-4 Hz. **Task:** Transcribe sentences. | **~50-86% Accuracy** with "4Hz Notch" effect. Humans struggle specifically at syllabic rates (4Hz). [5] | **4/5** | ✗ **Not Covered:** B3.T26 (Lexical & Phrase-Level Recognition) is related. *Gap: No phonemic restoration task.* |
| **Reverberant Speech (RT60)** | **Input:** Speech with RT60 = 1.0-2.0s. **Task:** Comprehension/Transcription. | **<80% Accuracy** at RT60=1.0s; **~60% Accuracy** at RT60=2.0s. Cliff for healthy adults >0.8s. [6] | **4/5** | ✗ **Not Covered:** B3.T30 (Audio Quality & Artifacts) detects recording conditions. *Gap: No explicit reverberant stress testing at controlled RT60 levels.* |
| **Auditory 3-Back** | **Input:** Continuous stream of letters. **Task:** "Match letter from 3 steps ago." | **~73-77% Accuracy**. Significant drop from 2-back (~80%). [7] | **3/5** | ✗ **Not Covered:** B3.T35 (Temporal & Ordering Reasoning). *Gap: No explicit n-back paradigm.* |

---

## Coverage Summary

| Coverage Level | Count | Tasks |
|----------------|-------|-------|
| ✓ Well Covered | **0** | — |
| ⚠ Partially Covered | **3** | PASAT-AI, Dichotic Listening, QuickSIN |
| ✗ Not Covered | **4** | Time-Compressed Speech, Interrupted Speech, Reverberant Speech, Auditory 3-Back |

---

## Importance Scoring Criteria

Importance scores (1-5) based on two factors:

1. **Cognitive Load**: How much the task stresses "reasoning/attention" vs. simple "hearing"
2. **AI Failure Potential**: How likely a current Audio LLM is to fail in a non-human way (e.g., hallucinating during silence or failing to prioritize spatial streams)

---

## Key Gaps Identified

These clinical tests stress cognitive mechanisms that MMAU-Pro does not explicitly test:

| Gap Category | Missing Capability | CAB Tasks Affected |
|--------------|-------------------|-------------------|
| **Paced Serial Processing** | Working memory updating under time pressure | PASAT-AI |
| **Selective Attention / Inhibition** | Suppressing dominant channel to attend to weaker | Dichotic Listening |
| **Clinical SNR Measurement** | Calibrated speech-in-noise thresholds | QuickSIN |
| **Temporal Resolution Limits** | Performance at extreme time compression | Time-Compressed Speech |
| **Phonemic Restoration** | Filling in masked/interrupted speech | Interrupted Speech |
| **Reverberant Stress Testing** | Controlled RT60 degradation curves | Reverberant Speech |
| **N-Back Paradigm** | Explicit working memory load manipulation | Auditory 3-Back |

---

## References

1. Brooks, J. B. B., et al. (2011). Paced auditory serial addition test (PASAT): a very difficult test even for individuals with high intellectual capability. *Arquivos de Neuro-Psiquiatria*, 69(3).

2. Tanaka, K., et al. (2021). Neurophysiological Evaluation of Right-Ear Advantage During Dichotic Listening. *Frontiers in Psychology*, 12.

3. Killion, M. C., et al. (2004). Development of a quick speech-in-noise test for measuring signal-to-noise ratio loss in normal-hearing and hearing-impaired listeners. *JASA*, 116(4).

4. Versfeld, N. J., & Dreschler, W. A. (2002). The relationship between the intelligibility of time-compressed speech and speech in noise in young and elderly listeners. *JASA*, 111(1).

5. Shafiro, V., et al. (2016). The influence of age and hearing loss on the perception of interrupted speech. *Trends in Hearing*, 20.

6. Lee, H., & Jeon, J. Y. (2022). Investigation of the Appropriate Reverberation Time in Learning Spaces for Effective Speech Intelligibility. *Sustainability*, 14.

7. Miller, K. M., et al. (2009). Is the N-Back Task a Valid Neuropsychological Measure for Assessing Working Memory? *Archives of Clinical Neuropsychology*, 24(7).

---

## Related Documents

- [benchmark-tasks.md](benchmark-tasks.md) - Complete MMAU-Pro task list
- [combined-taxonomy-table.md](combined-taxonomy-table.md) - 4-Pillar framework mapping

---

**End of CAB-MMAU-Pro Coverage Analysis**


