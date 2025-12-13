# Research Connections: Baldwin (2012) → Audio Cognition Benchmark

This document maps specific sections from Baldwin's "Auditory Cognition and Human Performance" to the Audio Cognition Benchmark project's Four Pillars and Three-Layer taxonomy.

---

## Chapter 6: Direct Task Implementations

**File**: [Chapter_14.md](Chapter_14.md) - Chapter 6: Auditory Tasks in Cognitive Research

### Layer 2 (Cognitive Control) - Core Tasks

| **Benchmark Task** | **Baldwin Section** | **Page References** | **Implementation Notes** |
|--------------------|---------------------|---------------------|--------------------------|
| **Selective Attention (Cocktail Party)** | §6.3 Dichotic Listening Tasks | pp. 97-98 | Use different speaker genders for 30 dB S/N advantage. Test schema-based segregation. |
| **Divided Attention** | §6.15 Auditory Oddball Paradigm | pp. 106-107 | 80% distractor, 20% target tones. Measure P300-equivalent attention metrics in AI. |
| **Attention Switching** | §6.9 Psychological Refractory Period | pp. 102-104 | Dual-task with varying SOA. 60% of humans fail to inhibit low-priority task. |
| **Working Memory** | §6.7 Listening Span | pp. 99-101 | Process sentences + make judgment + recall words. PL manipulation for stress testing. |
| **Working Memory** | §6.8 Auditory n-Back | pp. 101-102 | Identity (ventral) vs. Spatial (dorsal) variants validate Dual Stream. |

### Buffalo Model (Pillar 4) - Stress Testing

| **Stress Dimension** | **Baldwin Section** | **Page References** | **Implementation Notes** |
|----------------------|---------------------|---------------------|--------------------------|
| **Tolerance-Fading Memory** | §6.12 Delayed Digit Recall | p. 105 | Add noise layers, measure recall degradation. Proven sensitive to environmental stress. |
| **Tolerance-Fading Memory** | §6.13 Mental Arithmetic | pp. 105-106 | Secondary task probe. Two-digit subtraction variant most sensitive. |
| **Decoding Speed** | §6.18 PASAT | pp. 108-109 | Serial addition under time pressure. Human baselines available. |
| **Extreme Stress (Gap #6)** | SCIT: PL Manipulation | pp. 94, 100, 112-113 | Test at 55, 65, 75 dB SPL. Plot performance degradation curves. |

### Layer 1 (Foundational) - Automatic Processing

| **Benchmark Task** | **Baldwin Section** | **Page References** | **Implementation Notes** |
|--------------------|---------------------|---------------------|--------------------------|
| **Automatic Change Detection** | §6.27 Mismatch Negativity | pp. 111-112 | Deviant stimuli in repetitive stream. Tests primitive segregation without attention. |
| **Rhythm/Temporal Grouping** | §6.22 Seashore Rhythm Test | p. 109 | Discriminate rhythmic patterns. Maps to Gap #2 (Onset Synchrony Detection). |

---

## Chapter 4: Theoretical Foundation for Layer 2

**File**: [Chapter_12.md](Chapter_12.md) - Chapter 4: Auditory Cognition

### Pillar 2 (CASA) - Attention Theory

| **Concept** | **Relevant Section** | **Benchmark Application** |
|-------------|----------------------|---------------------------|
| **Broadbent's Early Filter** | §4.6 | Basis for selective attention tasks. Tests whether AI filters early or late. |
| **Treisman's Attenuation** | §4.7 | Unattended channel partially processed. Relevant for schema-based segregation. |
| **Primitive vs. Schema-Based** | §4.18-4.19 (implied) | Layer 1 (automatic) vs. Layer 2 (controlled) distinction. |
| **Echoic Memory** | §4.17-4.21 | Short-term auditory store. Tests memory trace duration. |
| **Working Memory Components** | §4.22-4.28 | Phonological loop, articulatory rehearsal. Maps to listening span tasks. |

### Key Methodological Warning

**SCIT (Sensory-Cognitive Interaction Theory)**: Throughout Chapter 4, Baldwin emphasizes that:
- Sensory effort depletes cognitive resources
- Must control and report presentation level (PL)
- Individual differences in hearing acuity confound cognitive measures

**Action**: All benchmark tasks must report acoustic parameters and test at multiple PLs.

---

## Chapter 3: Pillar 2 (CASA) & Pillar 3 (Dual Stream)

**File**: [Chapter_11.md](Chapter_11.md) - Chapter 3: Auditory Pattern Perception

### Core CASA Concepts

| **Concept** | **Relevant Section** | **Benchmark Application** |
|-------------|----------------------|---------------------------|
| **Auditory Scene Analysis** | §3.18 | Theoretical foundation for stream segregation tasks (Layer 1). |
| **Stream Segregation** | §3.19 | Frequency/temporal proximity. Test automatic grouping mechanisms. |
| **Cerebral Lateralization** | §3.12 | Left/right hemisphere specialization. Validates separating task types. |
| **Sound Localization** | §3.16 | Spatial processing. Excluded from benchmark (requires binaural), but validates Dual Stream. |

### Dual Stream Hypothesis (Pillar 3)

**Neuroanatomical Evidence**:
- Ventral Stream ("What") - Object identification → Identity n-Back, listening span
- Dorsal Stream ("Where/How") - Spatial/action → Spatial n-Back, sound localization (excluded)

**Validation**: Design separate identity vs. spatial tasks to prove Dual Stream independence in AI models.

---

## Chapter 5: Buffalo Model (Pillar 4) Implementation

**File**: [Chapter_13.md](Chapter_13.md) - Chapter 5: Mental Workload Assessment

### Multiple Resource Theory

| **Concept** | **Relevant Section** | **Benchmark Application** |
|-------------|----------------------|---------------------------|
| **Multiple Resource Theory** | §5.3 | Justifies separating task types (visual/auditory, verbal/spatial). |
| **Working Memory Processes** | §5.5 | Executive function measurement under load. |
| **Secondary Task Paradigm** | §5.13-5.15 | Use mental arithmetic or digit recall as probe while primary task runs. |
| **Dual-Task Performance** | Throughout | Measure interference between tasks to assess resource competition. |

### Stress Testing Framework

**Key Principle**: Performance degrades gracefully under increasing load in humans. Does AI show similar patterns?

**Implementation**:
1. **Baseline**: Optimal conditions (clear audio, no noise, single task)
2. **Degraded Sensory**: Add noise, reduce PL, reverb (Tolerance dimension)
3. **Cognitive Load**: Add secondary task (Decoding + Tolerance-Fading Memory)
4. **Time Pressure**: Reduce response window (Decoding dimension)
5. **Integration**: Combine modalities (Integration dimension - may exclude if unimodal focus)

---

## Chapter 7: Pillar 1 (Ecological Psychology) Implementation

**File**: [Chapter_15.md](Chapter_15.md) - Chapter 7: Nonverbal Sounds and Workload

### Gaver's Ecological Acoustics

| **Concept** | **Relevant Section** | **Benchmark Application** |
|-------------|----------------------|---------------------------|
| **Ecological Acoustics** | §7.6 | Gaver's taxonomy: Vibrating Solids, Liquids, Aerodynamics (your Pillar 1). |
| **Auditory Object Recognition** | §7.4-7.6 | Material identification from impact sounds (wood vs. metal). |
| **Music and Cognition** | §7.7-7.26 | Background music effects. You've excluded, but provides context. |
| **Noise Effects** | §7.27-7.37 | Irrelevant speech disrupts visual-verbal tasks. Relevant for Tolerance testing. |

### Layer 1 Physics-Based Reasoning

**Tasks**:
- Infer material properties from impact sounds (solid vibration category)
- Detect liquid viscosity from pouring sounds (liquid category)
- Estimate pressure/force from aerodynamic sounds (aerodynamic category)

---

## Chapter 8: Layer 1 & Layer 3 Speech Tasks

**File**: [Chapter_16.md](Chapter_16.md) - Chapter 8: Speech Processing and Workload

### Phonemic Restoration (Gap #1 - Priority 5/5)

| **Concept** | **Relevant Section** | **Benchmark Application** |
|-------------|----------------------|---------------------------|
| **Speech in Degraded Conditions** | Throughout Ch. 8 | Basis for phonemic restoration task design. |
| **Acoustic Environment Effects** | §8.24 | Noise, reverberation effects. Tests schema-based completion (Layer 2/3). |
| **Contextual Factors** | §8.26-8.27 | Speaker familiarity, predictability aid restoration. |

**Gap Priority**: Chapter 8 provides theoretical backing for **phonemic restoration** as a schema-based, Layer 2/3 task that tests both CASA principles and higher-level linguistic knowledge.

---

## Chapter 9: Integration Tasks (Buffalo Model)

**File**: [Chapter_17.md](Chapter_17.md) - Chapter 9: Cross-Modal Influences

### Integration Dimension (Pillar 4 - Buffalo Model)

| **Concept** | **Relevant Section** | **Benchmark Application** |
|-------------|----------------------|---------------------------|
| **Audiovisual Speech** | §9.10 | McGurk effect. May inform multimodal integration if scope expands. |
| **Cross-Modal Attention** | §9.11-9.12 | Spatial cuing across modalities. Currently out of scope (unimodal focus). |
| **Time-Sharing Audio/Visual** | §9.14-9.15 | Dual-task interference. Relevant if testing AI with visual+audio inputs. |

**Current Status**: Integration tasks deprioritized (unimodal audio focus), but Chapter 9 provides foundation if scope expands.

---

## Critical Methodological Requirements (From Chapter 6)

### **Always Report These Parameters**

1. **Presentation Level (PL)**: Loudness in dB SPL
   - Directly affects working memory capacity (p. 100)
   - Older listeners especially sensitive (SCIT principle)
   - Test at multiple levels: 55, 65, 75 dB SPL

2. **Signal-to-Noise Ratio (SNR)**: If noise present
   - Dichotic presentation = 30 dB SNR advantage (p. 98)
   - Different speaker genders improve separation (p. 98)

3. **Temporal Parameters**: SOA, ISI, stimulus duration
   - Critical for PRP (attention switching) tasks (pp. 102-104)
   - Affects n-back difficulty (pp. 101-102)

4. **Acoustic Characteristics**: Frequency, timbre, spatial location
   - Similarity increases difficulty (p. 98)
   - Relevant for stream segregation (Layer 1)

### **Sensory-Cognitive Interaction Theory (SCIT)**

**Core Principle** (appears pp. 94, 100, 108, 112-113):
> "The additional mental effort required to process degraded sensory stimuli may deplete resources from other stages of processing."

**Implication**:
- Always control hearing acuity (for humans)
- Test AI at multiple acoustic degradation levels
- Plot performance curves, not just binary pass/fail

---

## Human Baseline Data Sources

From Chapter 6 neuropsychological tests:

| **Test** | **Human Norms Available** | **Notes** |
|----------|---------------------------|-----------|
| PASAT | Yes (clinical populations) | Information processing speed |
| RAVLT | Yes (extensive aging literature) | Verbal learning and memory |
| Seashore Rhythm | Yes (clinical epilepsy studies) | Attentional processing |
| Listening Span | Yes (Daneman & Carpenter 1980) | Working memory capacity |
| n-Back | Yes (developmental literature) | Ages 6-13 developmental norms |
| Dichotic Listening | Yes (classic Cherry 1953) | Selective attention |

**Action**: Cite these tests when establishing human performance baselines for benchmark validation.

---

## Summary: Chapter → Benchmark Mapping

| **Chapter** | **Primary Contribution** | **Benchmark Layer/Pillar** |
|-------------|--------------------------|----------------------------|
| **Ch. 3** | Auditory scene analysis, stream segregation | Layer 1 (Foundational), Pillar 2 (CASA) |
| **Ch. 4** | Attention theories, echoic/working memory | Layer 2 (Cognitive Control), Pillar 2 (CASA) |
| **Ch. 5** | Mental workload, multiple resource theory | Layer 2, Pillar 4 (Buffalo Model) |
| **Ch. 6** ⭐ | Concrete task implementations, SCIT | All Layers, All Pillars (Methodological backbone) |
| **Ch. 7** | Ecological acoustics (Gaver), noise effects | Layer 1, Pillar 1 (Ecological Psychology) |
| **Ch. 8** | Speech in degraded conditions | Layer 1, Layer 3, Gap #1 (Phonemic Restoration) |
| **Ch. 9** | Cross-modal integration | Pillar 4 (Integration dimension) - out of scope |

---

## Next Steps

1. **Verify Chapter 3-5, 7-8 extraction**: Read extracted chapters to confirm all relevant sections present
2. **Extract key quotes**: From Chapters 3, 4, 5, 7, 8 for citations in benchmark specification
3. **Design task protocols**: Use Baldwin's task descriptions to write formal evaluation protocols
4. **Map human baselines**: Compile performance data from cited literature (PASAT, RAVLT, etc.)
5. **Draft acoustic parameter guidelines**: Formalize PL, SNR, temporal parameter requirements

---

*Created: December 12, 2025*
*Last Updated: December 12, 2025*
