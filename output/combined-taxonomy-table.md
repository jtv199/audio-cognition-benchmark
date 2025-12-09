# Combined Taxonomy Table: Email Tasks + 4-Pillar Framework + Benchmark Coverage

**Generated**: December 8, 2025
**Purpose**: Integrate original email taxonomy with systematic 4-Pillar framework and map to existing audio benchmarks

---

## Executive Summary

This document addresses Ting's feedback: _"Is there any systematic definition of human hearing capabilities? What you listed covers most cases, but the points seem scattered. A systematic framework to categorize this would be very helpful."_

**What We Did**:
1. **Referenced 4 different taxonomies** to identify what tasks constitute auditory cognition
2. **Sorted tasks into tables** with benchmark coverage analysis across 4 benchmarks (AIR-Bench, AudioBench, MMAU-Pro, and WavCaps)
3. **Verified benchmark tasks comprehensively** (MMAU-Pro most thoroughly verified with 38 explicit skills)
4. **Identified potential gaps** in existing benchmark coverage → [See Potential Gaps section](#potential-gaps-after-mmau-pro)

**Solution**: The **4-Pillar Framework** provides systematic organization of human auditory cognition from four complementary scientific perspectives:

1. **Pillar 1: Ecological Psychology (Physics View)** - What physical events produce sounds?
2. **Pillar 2: Computational Auditory Scene Analysis (Grouping View)** - How are sounds organized?
3. **Pillar 3: Cognitive Neuroscience (Architecture View)** - Where/how does the brain process sound?
4. **Pillar 4: Clinical Audiology (Stress-Test View)** - What breaks down under stress?

Together, these pillars provide the **systematic framework** for categorizing the original email tasks and identifying gaps in existing benchmarks. **MMAU-Pro emerges as the most comprehensive benchmark** with 38 explicitly defined skills across music, sound, and speech domains, plus 7 novel testing dimensions (long-form audio, multi-audio reasoning, spatial audio, etc.).

---

## Main References

### Foundational Papers (The 4 Pillars)

| Pillar             | Paper                                                                                                                                                                                 | Field                  | Contribution                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------- |
| **P1: Ecological** | Gaver, W. W. (1993). What in the world do we hear? An ecological approach to auditory event perception. _Ecological Psychology_, 5(1), 1-29.                                          | Ecological Psychology  | Taxonomy of sound-producing events by material physics (solids, liquids, gases) |
| **P2: CASA**       | Bregman, A. S. (1990). _Auditory Scene Analysis: The Perceptual Organization of Sound_. MIT Press.                                                                                    | Cognitive Psychology   | Primitive vs. schema-based segregation; stream formation                        |
| **P3: Neuro**      | Rauschecker, J. P., & Scott, S. K. (2009). Maps and streams in the auditory cortex: nonhuman primates illuminate human speech processing. _Nature Neuroscience_, 12(6), 718-724.      | Cognitive Neuroscience | Dual stream hypothesis (ventral "what" vs. dorsal "where/how")                  |
| **P4: Clinical**   | Katz, J. (1992). Classification of auditory processing disorders. In J. Katz, N. Stecker, & D. Henderson (Eds.), _Central Auditory Processing: A Transdisciplinary View_ (pp. 81-91). | Clinical Audiology     | Buffalo Model: 4 APD categories (Decoding, TFM, Integration, Organization)      |

### Benchmark Papers (Comparison Sources)

| Benchmark      | Paper                                                                                                                                                                                     | Key Statistics                                                                       | Link                                                 |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| **AIR-Bench**  | Yang, Q., Xu, J., Liu, W., et al. (2024). AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension. _ACL 2024_.                                                   | 19 foundation tasks, ~19k questions; 2k chat instances                               | [arXiv:2402.07729](https://arxiv.org/abs/2402.07729) |
| **AudioBench** | Wang, B., Zou, X., Lin, G., et al. (2025). AudioBench: A Universal Benchmark for Audio Large Language Models. _NAACL 2025_.                                                               | 8 tasks, 26 datasets (7 new)                                                         | [arXiv:2406.16020](https://arxiv.org/abs/2406.16020) |
| **MMAU-Pro**   | Kumar, S., Sedláček, Š., Lokegaonkar, V., López, F., et al. (2025). MMAU-Pro: A Challenging and Comprehensive Benchmark for Holistic Evaluation of Audio General Intelligence. Pre-print. | 5,305 instances, 49 skills; long-form (10 min), spatial audio, multi-audio reasoning | [arXiv:2508.13992](https://arxiv.org/abs/2508.13992) |

**Source Verification Note**: Benchmark coverage assessments below are based on published task lists from the papers above. AIR-Bench and AudioBench task lists were directly verified from official documentation. MMAU-Pro's 49 skills are documented in the full paper with detailed skill distribution and example questions.

**Task Reference**:

- **Detailed task tables**: Complete task-by-task breakdown with descriptions, examples, and framework mappings → [benchmark-tasks.md](benchmark-tasks.md)
- **Benchmark metadata**: Official sources, citations, and cross-benchmark comparison → [../papers/benchmark/benchmark_reference.md](../papers/benchmark/benchmark_reference.md)

### Supporting References (Original Email Tasks)

| Task                | Reference                                                                                                                        | Notes                                  |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Stream Segregation  | Bregman (1990) _Auditory Scene Analysis_                                                                                         | Foundation of CASA (P2)                |
| Schema Congruity    | Gaver (1993) _What in the world do we hear?_                                                                                     | Foundation of Ecological approach (P1) |
| Selective Attention | Cherry, E. C. (1953). Some experiments on the recognition of speech, with one and with two ears. _JASA_, 25(5), 975-979.         | Original "Cocktail Party Effect" paper |
| Divided Attention   | Broadbent, D. E. (1958). _Perception and Communication_. Pergamon Press.                                                         | Divided attention theory               |
| Paralinguistics     | Scherer, K. R. (2003). Vocal communication of emotion: A review of research paradigms. _Speech Communication_, 40(1-2), 227-256. | Emotional prosody                      |
| Causal Reasoning    | Ballas, J. A. (1993). Common factors in the identification of an assortment of brief everyday sounds. _JEPP_, 19(2), 250-267.    | Environmental sound reasoning          |

---

## Framework Explanations: Four Field Perspectives

### Pillar 1: Ecological Psychology (Physics View)

**Question**: _What physical events in the world produce sounds?_

**Field Origin**: Ecological psychology, pioneered by J.J. Gibson

**Core Insight**: Humans don't hear "frequencies" - they hear **events** (impacts, pouring, footsteps). Sound is structured energy carrying information about material properties, forces, and environmental states.

**Taxonomy**: Organized by **material physics**:

- **Vibrating Solids**: Impact, scraping, rolling
- **Liquids**: Dripping, pouring, splashing
- **Aerodynamics**: Explosions, hissing, flow

**Benchmark Application**: Tests whether models can infer:

- Material properties (wood vs. metal)
- Object states (full bottle vs. empty)
- Forces (heavy impact vs. light tap)

---

### Pillar 2: Computational Auditory Scene Analysis (Grouping View)

**Question**: _How does the auditory system organize mixed acoustic energy?_

**Field Origin**: Cognitive psychology, computational modeling

**Core Insight**: The "cocktail party problem" - separating signal from noise requires both:

- **Primitive segregation** (automatic, bottom-up): Grouping by onset synchrony, frequency proximity
- **Schema-based segregation** (attention-driven, top-down): Using learned patterns and attention to extract targets

**Taxonomy**: Organized by **processing mode**:

- **Primitive**: Common fate, onset synchrony, frequency proximity, spatial proximity, temporal continuity, harmonic relations
- **Schema-based**: Voluntary attention, prior learning, phonemic restoration

**Benchmark Application**: Tests whether models can:

- Segregate overlapping sources
- Use attention to select targets
- Maintain stable representations under interference

---

### Pillar 3: Cognitive Neuroscience (Architecture View)

**Question**: _Where and how does the brain process sound?_

**Field Origin**: Neuroscience, functional neuroimaging

**Core Insight**: The brain uses **parallel processing streams** analogous to vision:

- **Ventral "What" stream** (anterior-ventral): Object identification, speech, voice, semantics
- **Dorsal "Where/How" stream** (posterior-dorsal): Spatial localization, motion, sensorimotor integration

**Taxonomy**: Organized by **neural pathway**:

- **Ventral**: Object ID → Speech perception → Voice perception → Invariance → Categorization
- **Dorsal**: Localization → Motion → Sensorimotor → Speech production

**Benchmark Application**: Tests whether models have:

- Separate "what" and "where" capabilities
- Hierarchical processing (simple → complex)
- Invariant representations

---

### Pillar 4: Clinical Audiology (Stress-Test View)

**Question**: _What breaks down under stress or pathology?_

**Field Origin**: Clinical audiology, neuropsychology

**Core Insight**: Auditory processing is best understood by its **failure modes** under stress (noise, load, damage). The Buffalo Model identifies 4 breakdown patterns:

- **Decoding**: Basic phonemic analysis fails
- **Tolerance-Fading Memory**: Performance collapses in noise or with memory load
- **Integration**: Difficulty combining information across ears/modalities
- **Organization**: Higher-order sequencing and reasoning fails

**Taxonomy**: Organized by **clinical deficit category**:

- Decoding, Tolerance-Fading Memory, Integration, Organization

**Benchmark Application**: Tests model robustness:

- Performance under noise
- Working memory capacity
- Stress testing and adversarial conditions

---

## Combined Taxonomy Table

### Original Email Tasks Mapped to 4-Pillar Framework

| Task/Example                                                                          | Layer                       | Original Scientific Domain     | Frameworks Involved                                                                                                                                                                    | Framework-Specific Concepts                                                                                                                   | Benchmark Coverage                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------- | --------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stream Segregation**: Separating target speaker from background talkers             | Layer 1 (Foundational)      | Auditory Scene Analysis (ASA)  | **P2** (CASA): Primitive & Schema-based<br/>**P3** (Neuro): Ventral stream object identification<br/>**P4** (Clinical): Integration                                                    | P2: Frequency proximity, onset synchrony, spatial proximity<br/>P3: Ventral stream hierarchical processing<br/>P4: Integration across sources | ⚠ B1.T8 (Speaker number verification - related)<br/>⚠ B2.T2 (SQA - may include multi-speaker)<br/>✓ B3.T29 (Speech Activity & Turn-Taking), B3.T4 (Spatial Sound Perception)                                                           |
| **Schema Congruity**: Detecting chainsaw sound anomalous in library                   | Layer 1 (Foundational)      | Ecological Psychoacoustics     | **P1** (Ecological): Event-environment mismatch<br/>**P2** (CASA): Schema-based expectations<br/>**P3** (Neuro): Ventral stream semantic categorization                                | P1: Environmental context reasoning<br/>P2: Schema violation detection<br/>P3: Semantic incongruity                                           | ⚠ B1.T12 (Acoustic scene classification - partial)<br/>✗ B2 (No explicit schema tasks)<br/>✓ B3.T18 (Acoustic Scene Reasoning), B3.T34 (Contextual/Causal Scenario Reasoning)                                                          |
| **Selective Attention**: Cocktail party - transcribe one speaker, suppress distractor | Layer 2 (Cognitive Control) | Cognitive Control / Inhibition | **P2** (CASA): Schema-based attention<br/>**P3** (Neuro): Dorsal stream attention<br/>**P4** (Clinical): Tolerance-Fading Memory                                                       | P2: Voluntary attention, stream selection<br/>P3: Dorsal stream spatial attention<br/>P4: TFM - performance in noise                          | ✗ B1 (No explicit attention tasks)<br/>⚠ B2.T1 (ASR with LibriSpeech-Other includes noise)<br/>⚠ B3 (Novel dimensions: Instruction Following, Multi-audio - partial)                                                                   |
| **Divided Attention**: Monitor two news streams simultaneously for keywords           | Layer 2 (Cognitive Control) | Working Memory / Load          | **P2** (CASA): Schema-based multi-stream tracking<br/>**P3** (Neuro): Dorsal stream parallel processing<br/>**P4** (Clinical): Tolerance-Fading Memory, Organization                   | P2: Divided attention across streams<br/>P3: Working memory capacity<br/>P4: TFM - memory load, Organization - sequencing                     | ✗ B1 (No multi-stream tasks)<br/>✗ B2 (No divided attention tasks)<br/>✓ B3 (Novel dimensions: Long-form audio up to 10 min, Multi-audio)                                                                                              |
| **Paralinguistics**: Detecting sarcasm (mocking tone contradicts text)                | Layer 3 (Inferential)       | Social Cognition / Prosody     | **P3** (Neuro): Ventral stream high-level inference<br/>**P4** (Clinical): Organization                                                                                                | P3: Emotional prosody, theory of mind<br/>P4: Organization - integrating prosody + semantics                                                  | ⚠ B1.T4, B1.T19 (Emotion recognition - basic only)<br/>⚠ B2.T6 (ER - basic emotion, not sarcasm)<br/>✓ B3.T28 (Paralinguistic/Emotion Recognition), B3.T25 (Prosody Detection), B3.T12 (Expression and Emotion Interpretation - music) |
| **Causal Reasoning**: Footsteps→creak→shatter = intrusion sequence                    | Layer 3 (Inferential)       | Environmental Reasoning        | **P1** (Ecological): Event physics + causality<br/>**P2** (CASA): Schema-based integration<br/>**P3** (Neuro): Ventral stream high-level reasoning<br/>**P4** (Clinical): Organization | P1: Event sequence physics<br/>P2: Temporal integration<br/>P3: Causal inference<br/>P4: Organization - sequencing                            | ⚠ B1.T13 (Sound QA - may include)<br/>⚠ B2.T4 (AQA - limited causal)<br/>✓ B3.T34 (Contextual/Causal Scenario Reasoning), B3.T35 (Temporal & Ordering Reasoning - speech), B3.T22 (Temporal Reasoning - sound)                         |

**Legend:**

- ✓ = Well covered (task explicitly listed in benchmark)
- ⚠ = Partially covered (related task exists, but not identical)
- ✗ = Not covered (no similar task found in verified task list)

---

## Extended Taxonomy: Additional Tasks from 4-Pillar Framework

### Layer 1: Foundational Tasks (Not in Original Email)

| Task/Example                                                         | Frameworks Involved                          | Framework-Specific Concepts                  | Benchmark Coverage                                                                                                                                                 |
| -------------------------------------------------------------------- | -------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Material Identification**: "Is this wood or metal impact?"         | P1 (Ecological), P3 (Neuro: Ventral)         | P1: Material timbre from impact physics      | ⚠ B1.T11 (Vocal sound classification - partial)<br/>⚠ B2.T4 (AQA - may include, limited)<br/>✓ B3.T15 (Acoustic Source Characterization)                           |
| **Onset Synchrony Detection**: "Did these two tones start together?" | P2 (CASA: Primitive)                         | P2: Onset synchrony → fusion vs. segregation | ✗ B1 (No temporal grouping tasks)<br/>✗ B2 (No explicit grouping tasks)<br/>⚠ B3.T35 (Temporal & Ordering Reasoning - speech), B3.T22 (Temporal Reasoning - sound) |
| **Harmonic Grouping**: "Is this a single note or multiple notes?"    | P2 (CASA: Primitive)                         | P2: Harmonic relations → pitch perception    | ✓ B1.T16 (Music note analysis-pitch)<br/>✗ B2 (No harmonic tasks)<br/>✓ B3.T1 (Harmony Perception and Analysis)                                                    |
| **Basic Phoneme Recognition**: "Is this /ba/ or /pa/?"               | P3 (Neuro: Ventral), P4 (Clinical: Decoding) | P3: Speech hierarchy, P4: Decoding           | ✓ B1.T6 (Speech entity recognition)<br/>✓ B2.T1 (ASR - all 9 datasets)<br/>✓ B3.T26 (Lexical & Phrase-Level Recognition)                                           |

### Layer 2: Cognitive Control Tasks (Not in Original Email)

| Task/Example                                                              | Frameworks Involved                                | Framework-Specific Concepts                                                  | Benchmark Coverage                                                                                                                                                                  |
| ------------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Speech-in-Noise**: "Understand sentence with background babble"         | P2 (CASA), P3 (Neuro), P4 (Clinical: TFM)          | P2: Schema-based segregation<br/>P3: Attention<br/>P4: TFM - noise tolerance | ⚠ B1.T1, B1.T6 (Speech grounding + entities - may include noise)<br/>✓ B2.T1 (ASR with LibriSpeech-Other, noise conditions)<br/>✓ B3 (Novel dimensions: Voice-Chat QA, Multi-audio) |
| **Spatial Attention**: "Follow sound from left speaker"                   | P2 (CASA), P3 (Neuro: Dorsal)                      | P2: Spatial proximity<br/>P3: Dorsal stream localization                     | ⚠ B1.T10 (Audio grounding - may include spatial)<br/>✗ B2 (No spatial tasks)<br/>✓ B3.T4 (Spatial Sound Perception), B3 (Novel dimension: 3D spatial audio)                         |
| **Working Memory Load**: "Remember sequence while processing distractors" | P2 (CASA), P4 (Clinical: TFM)                      | P2: Sequential integration<br/>P4: TFM - memory load                         | ✗ B1 (No working memory tasks)<br/>✗ B2 (No working memory tasks)<br/>✓ B3 (Novel dimension: Long-form audio up to 10 min)                                                          |
| **Stream Segregation Under Load**: "Track two melodies simultaneously"    | P2 (CASA), P3 (Neuro), P4 (Clinical: Organization) | P2: Frequency proximity + attention<br/>P4: Organization                     | ✗ B1 (No multi-stream tracking)<br/>✗ B2 (No multi-stream tracking)<br/>✓ B3.T29 (Speech Activity & Turn-Taking), B3 (Novel dimension: Multi-audio, B3.T35)                         |

### Layer 3: Inferential Tasks (Not in Original Email)

| Task/Example                                                                     | Frameworks Involved                                                       | Framework-Specific Concepts                                                                  | Benchmark Coverage                                                                                                                                                                               |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Mass Inference**: "Is this object heavy or light?" (from impact)               | P1 (Ecological), P3 (Neuro: Ventral)                                      | P1: Force/mass inference from physics                                                        | ✗ B1 (No physics inference)<br/>✗ B2 (No physics inference)<br/>⚠ B3.T15 (World Knowledge Integration - may include)                                                                             |
| **Environmental Reasoning**: "Are you in kitchen, bathroom, or garage?"          | P1 (Ecological), P2 (CASA), P3 (Neuro: Ventral)                           | P1: Event taxonomy + environment<br/>P2: Schema matching<br/>P3: High-level categorization   | ⚠ B1.T12 (Acoustic scene classification)<br/>⚠ B2.T4 (AQA - may include environmental context)<br/>✓ B3.T18 (Acoustic Scene Reasoning)                                                           |
| **Event Sequence Inference**: "What happened: pouring→splashing→glass breaking?" | P1 (Ecological), P2 (CASA), P4 (Clinical: Organization)                   | P1: Event physics + causality<br/>P2: Temporal integration<br/>P4: Organization - sequencing | ✗ B1 (No event sequence tasks)<br/>✗ B2 (No event sequence tasks)<br/>✓ B3.T35 (Temporal & Ordering Reasoning - speech), B3.T22 (Temporal Reasoning - sound)                                     |
| **Phonemic Restoration**: "Restore missing phoneme from context"                 | P2 (CASA: Schema-based), P3 (Neuro: Ventral), P4 (Clinical: Organization) | P2: Schema-based integration<br/>P3: High-level linguistic processing                        | ✗ B1 (No restoration tasks)<br/>✗ B2 (No restoration tasks)<br/>⚠ B3.T26 ( Lexical & Phrase-Level Recognition - related but not restoration) #gap                                                |
| **Voice Emotion Recognition**: "Does speaker sound happy or sad?"                | P3 (Neuro: Ventral)                                                       | P3: Emotional prosody, voice perception                                                      | ✓ B1.T4, B1.T19 (Emotion recognition: speech + music)<br/>✓ B2.T6 (ER - IEMOCAP, MELD)<br/>✓ B3.T12 (Expression and Emotion Interpretation - music), B3.T28 (Paralinguistic/Emotion Recognition) |
| **Theory of Mind**: "Is speaker being sarcastic?"                                | P3 (Neuro: Ventral), P4 (Clinical: Organization)                          | P3: Social cognition, theory of mind                                                         | ✗ B1 (Basic emotion only)<br/>✗ B2 (Basic emotion only)<br/>✓ B3.T12 (Expression and Emotion Interpretation - music)                                                                             |

---

## Benchmark Gap Analysis

### AIR-Bench Coverage

**Strengths**:

- ✓ Strong Layer 1 coverage (classification, ASR, captioning)
- ✓ Some Layer 2 coverage (speech-in-noise, mixed audio)
- ✓ Introduces "Foundation" vs. "Chat" tiers

**Gaps**:

- ✗ No Layer 3 reasoning tasks
- ✗ No causal inference
- ✗ Limited schema-based tasks
- ✗ No working memory or attention control tests
- ✗ Missing ecological/physics-based reasoning

**Framework Coverage**: Strong P3 (Neuro: Ventral), Weak P1 (Ecological), Partial P2 (CASA), Weak P4 (Clinical)

---

### AudioBench Coverage

**Strengths**:

- ✓ Diverse task coverage (speech, music, audio, reasoning)
- ✓ Strong emotion recognition
- ✓ Scene classification
- ✓ Standardized task definitions

**Gaps**:

- ✗ No attention/cognitive control tasks
- ✗ No working memory tests
- ✗ Limited causal reasoning
- ✗ No stress testing (noise, load)
- ✗ Missing ecological physics reasoning
- ✗ No explicit stream segregation tasks

**Framework Coverage**: Partial P3 (Neuro), Weak P1 (Ecological), Weak P2 (CASA), Weak P4 (Clinical)

---

### MMAU-Pro Coverage

**Strengths**:

- ✓ **Most comprehensive benchmark to date** (38 explicitly named skills in Tables 7-12, 5,305 instances)
- ✓ Strong Layer 2 coverage: Long-form audio (10 min), multi-audio reasoning (novel dimensions)
- ✓ Strong Layer 3 coverage: B3.T34 (Contextual/Causal), B3.T35/T22 (Temporal reasoning), B3.T36 (World knowledge)
- ✓ **Novel capabilities**: B3.T4 (Spatial Sound Perception) + 3D spatial audio dimension, Multicultural music dimension, Instruction following dimension
- ✓ Speech segregation: B3.T29 (Speech Activity & Turn-Taking)
- ✓ Advanced emotion reasoning: B3.T28 (Paralinguistic), B3.T25 (Prosody), B3.T12 (Emotion Interpretation)
- ✓ Material sound recognition: B3.T15 (Acoustic Source Characterization), B3.T18 (Acoustic Scene Reasoning)
- ✓ Open-ended QA format (not just multiple choice)

**Remaining Gaps**:

- ⚠ Primitive segregation mechanisms (onset synchrony, harmonic grouping) - limited explicit testing
- ⚠ Phonemic restoration - not explicit
- ⚠ Explicit attention switching tasks - partial (instruction following tests some aspects)
- ⚠ Stress testing at extreme SNR levels - unclear

**Framework Coverage**: Strong P1 (Ecological - material sounds, scene reasoning), Strong P2 (CASA - source separation, multi-audio), Strong P3 (Neuro - comprehensive), Strong P4 (Clinical - working memory via long-form audio)

---

## Key Findings: What's Missing or Under-Represented Across All Benchmarks

### Potential Gaps (After MMAU-Pro)

**Note**: MMAU-Pro (B3) significantly closes many gaps from earlier benchmarks, but some specific capabilities remain underserved:

| Importance | Example Task                                                             | Missing Capability                                | Layer   | Frameworks | Coverage Status                                                               |
|------------|--------------------------------------------------------------------------|---------------------------------------------------|---------|------------|-------------------------------------------------------------------------------|
| **5/5** | "The [NOISE] was loud" - restore the missing word from context           | **Phonemic Restoration**                          | 2, 3    | P2, P3, P4 | ✗ Not explicitly tested in any benchmark                                      |
| **4/5** | "Hear 'HIGH' in low pitch - identify pitch while ignoring word meaning" | **Auditory Stroop / Cross-Dimensional Conflict**  | 2       | P2, P3, P4 | ✗ Not explicitly tested in any benchmark                                      |
| **3/5** | "First, attend to left speaker; now switch to right speaker"             | **Attention Switching**                           | 2       | P2, P3, P4 | ⚠ B3 has instruction following but not explicit attention switching           |
| **3/5** | "Monitor two speakers simultaneously and detect when either says 'fire'" | **Explicit Divided Attention** | 2       | P2, P3, P4 | ⚠ B3 has multi-audio but not explicit divided attention with specific targets |
| **2/5** | "Did these two tones start at exactly the same time?"                    | **Onset Synchrony Detection**  | 1       | P2         | ✗ Primitive CASA mechanisms not explicitly tested                             |
| **1/5** | "Understand this sentence with -10dB SNR white noise"                    | **Extreme Stress Testing**     | 1, 2, 3 | P4         | ⚠ Unclear if B3 tests extreme SNR levels                                      |

### Capabilities Well-Covered by MMAU-Pro (B3)

These were previously identified as gaps but are now addressed:

- ✓ **Working Memory Under Load**: Novel dimension: Long-form audio up to 10 minutes
- ✓ **Causal Event Reasoning**: B3.T34 (Contextual/Causal Scenario Reasoning), B3.T35 (Temporal & Ordering - speech), B3.T22 (Temporal Reasoning - sound)
- ✓ **Physics-Based Inference**: B3.T15 (Acoustic Source Characterization), B3.T36 (World Knowledge Integration)
- ✓ **Schema Reasoning**: B3.T18 (Acoustic Scene Reasoning), B3.T34 (Contextual reasoning)
- ✓ **Stream Segregation**: B3.T29 (Speech Activity & Turn-Taking), B3.T4 (Spatial Sound Perception)
- ✓ **Spatial Reasoning**: B3.T4 (Spatial Sound Perception), Novel dimension: 3D spatial audio

---

## Differentiation Strategy: Our Benchmark vs. Existing (Updated with MMAU-Pro)

### Revised Landscape Analysis

**Key Update**: MMAU-Pro (B3, 2025) significantly raises the bar with 49 skills, long-form audio, spatial reasoning, and multi-audio tasks. This changes our differentiation strategy.

### Areas of Necessary Overlap (Validation)

**Why**: Establish credibility by showing competitive performance on known tasks

**Tasks to Include**:

- Stream segregation (all benchmarks, including B3.T29 Speech Activity & Turn-Taking)
- Speech-in-noise (all benchmarks, B3 has voice-chat QA dimension)
- Emotion recognition (all benchmarks, B3.T28 Paralinguistic, B3.T12 Emotion Interpretation)
- Scene classification (B1, B2, B3.T18 Acoustic Scene Reasoning)
- Working memory (B3 novel dimension: long-form audio up to 10 min)
- Spatial reasoning (B3.T4 Spatial Sound Perception + 3D spatial audio dimension)

**Coverage**: ~40-50% of our benchmark (increased due to B3's comprehensiveness)

---

### Remaining Areas of Strategic Differentiation

**Why**: Address specific gaps that remain even after MMAU-Pro

**Priority 1 - Explicit Cognitive Control Mechanisms**: ⚠ **Still underserved**

- **Attention switching**: Explicit cued switching between streams
- **Divided attention with specific targets**: "Monitor both speakers and detect when either says X"
- **Controlled comparison**: Before/after attention manipulation

**Priority 2 - Primitive CASA Mechanisms**: ⚠ **Missing from all benchmarks**

- **Onset synchrony detection**: "Did these tones start together?" (tests fusion/segregation boundary)
- **Harmonic grouping**: "One note or multiple notes?" (tests primitive integration)
- **Common fate grouping**: Explicit tests of Gestalt principles

**Priority 3 - Schema-Based Integration**: ⚠ **Limited explicit testing**

- **Phonemic restoration**: "The [NOISE] was loud" - restore missing speech
- **Continuity illusion**: Detecting vs. restoring occluded sounds
- **Schema violation**: Explicit incongruity detection tasks

**Priority 4 - Extreme Stress Testing**: ⚠ **Unclear coverage**

- **SNR sweep**: Performance curves from +10 dB to -10 dB SNR
- **Degradation analysis**: Where do models break vs. humans?

**Coverage**: ~50-60% of our benchmark (reduced focus on areas B3 covers)

---

## Recommended Task Distribution

### Proposed Benchmark Composition

```
Total: 100 tasks

Layer 1 (Foundational): 25 tasks (25%)
├─ Overlap with existing benchmarks: 10 tasks (stream segregation, basic classification)
└─ Novel CASA/Ecological tasks: 15 tasks (onset synchrony, schema congruity, material ID)

Layer 2 (Cognitive Control): 45 tasks (45%) ⭐ PRIORITY
├─ Overlap with existing benchmarks: 10 tasks (speech-in-noise, spatial attention)
└─ Novel attention/load tasks: 35 tasks (working memory, attention switching, divided attention)

Layer 3 (Inferential): 30 tasks (30%) ⭐ PRIORITY
├─ Overlap with existing benchmarks: 5 tasks (emotion recognition, basic scene reasoning)
└─ Novel reasoning tasks: 25 tasks (causal events, physics inference, theory of mind)
```

**Rationale**:

- **Layer 1 (25%)**: Establish credibility (overlap) + fill CASA gaps
- **Layer 2 (45%)**: Biggest gap in field - differentiates our work
- **Layer 3 (30%)**: Tests true intelligence - strong differentiation

---

## Framework Distribution Analysis

### Our Benchmark vs. Existing Benchmarks (Updated with B3: MMAU-Pro)

| Framework          | B1+B2 Coverage (before MMAU-Pro)         | B3: MMAU-Pro Coverage                                                          | Our Benchmark (Proposed)                                                     |
| ------------------ | ---------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| **P1: Ecological** | ⚠ Very Weak (scene classification only)  | ✓ Strong (B3.T15 Acoustic Source, B3.T18 Scene Reasoning, B3.T17 Eco-acoustic) | ✓ Strong (explicit physics reasoning, schema violation)                      |
| **P2: CASA**       | ⚠ Weak (implicit stream segregation)     | ✓ Strong (B3.T29 Turn-taking, multi-audio dimension, B3.T1 Harmony)            | ✓ Strong (explicit primitive mechanisms: onset synchrony, harmonic grouping) |
| **P3: Neuro**      | ✓ Moderate (ventral strong, dorsal weak) | ✓ Very Strong (balanced ventral + dorsal via B3.T4 Spatial + 3D dimension)     | ✓ Strong (maintain ventral/dorsal balance)                                   |
| **P4: Clinical**   | ✗ Very Weak (noise in ASR only)          | ✓ Strong (long-form audio dimension = working memory stress)                   | ✓ Strong (extreme SNR testing, attention switching)                          |

**Key Insight**: MMAU-Pro (B3) significantly narrows the differentiation space. Our benchmark should focus on **explicit mechanisms** (CASA primitives, attention switching) rather than broad coverage.

---

## Conclusion: The Systematic Framework Value

### What the 4-Pillar Framework Provides

1. **Systematic Organization**: Resolves Ting's feedback - provides structure for scattered tasks
2. **Gap Identification**: Reveals what existing benchmarks miss, even after comprehensive B3 (MMAU-Pro)
   - **Remaining gaps**: Primitive CASA mechanisms (onset synchrony, harmonic grouping), explicit attention switching, phonemic restoration, extreme stress testing
3. **Theoretical Grounding**: Every task justified by scientific theory
4. **Updated Differentiation Strategy**:
   - **Before MMAU-Pro**: 70-75% novel tasks needed (B1+B2 had major gaps)
   - **After MMAU-Pro**: 50-60% novel tasks (B3 closes many gaps, focus shifts to explicit mechanisms)
5. **Comprehensive Coverage**: All aspects of human auditory cognition represented across 4 complementary perspectives

### Strategic Recommendations

**Immediate**:

1. ✅ Use 4-Pillar framework as systematic backbone (addresses Ting's request)
2. ✅ Create combined table showing overlap + differentiation (addresses Ting's request)
3. ⏳ Focus task design on Layer 2 (45%) and Layer 3 (30%) for differentiation

**Next Phase**: 4. Map tasks to available datasets (Ting's request) 5. Identify human baseline tests for each task (Ting's request) 6. Design novel tasks for underserved areas (Layer 2-3, P1-P2-P4)

---

## Appendix: Complete Benchmark Task Lists

For detailed benchmark task information, see these companion documents:

### 1. Detailed Task Tables with Examples

**[benchmark-tasks.md](benchmark-tasks.md)** - Complete task-by-task breakdown in table format:

- **B1 (AIR-Bench)**: 19 foundation tasks organized by Speech (9), Audio (4), Music (6)
  - Each task includes: ID, name, description, layer, framework mapping, example question
- **B2 (AudioBench)**: 8 tasks across 26 datasets organized by Speech Understanding (4), Audio Scene (2), Paralinguistics (3)
  - Each task includes: ID, name, datasets, description, layer, framework mapping, example test
- **B3 (MMAU-Pro)**: 38 skills (B3.T1-T38) organized by domain (Music, Sound, Speech) and skill type (Perceptual, Reasoning), plus 7 novel testing dimensions
  - Each skill includes: Task ID, name, description, layer, framework mapping, example question
  - Music: B3.T1-T14 (7 perceptual + 7 reasoning)
  - Sound: B3.T15-T22 (3 perceptual + 5 reasoning)
  - Speech: B3.T23-T38 (8 perceptual + 8 reasoning)
  - Plus cross-benchmark comparison tables and layer/framework coverage analysis

### 2. Benchmark Metadata and Citations

**[../papers/benchmark/benchmark_reference.md](../papers/benchmark/benchmark_reference.md)** - Official sources and cross-benchmark comparison:

- All benchmark citations and official links (arXiv, GitHub, websites)
- Cross-benchmark comparison table (task coverage by category)
- Performance benchmarks from papers
- Proper citation formats

---

**End of Combined Taxonomy Table**

_For detailed framework information, see [taxonomy.md](taxonomy.md)_
_For leaf node examples, see [taxonomy-overview.md](taxonomy-overview.md)_
_For evolutionary analogies, see [analogies.md](analogies.md)_
_For paper references, see [../structure/local-references.md](../structure/local-references.md)_
