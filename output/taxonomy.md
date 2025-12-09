# Auditory Perception Taxonomies: The Four Pillars

**Generated**: December 8, 2025 **Source**: Processed benchmark papers from audio-ml project

------------------------------------------------------------------------

## Executive Summary

This document presents four foundational taxonomies that structure the field of auditory perception and cognition. Each taxonomy represents a distinct theoretical "pillar" that together form a comprehensive framework for understanding how humans process, organize, and interpret sound

### The Four Pillars

1.  **Pillar 1: Ecological Psychology (Physics View)** - Gaver's taxonomy of sound-producing events
2.  **Pillar 2: Computational Auditory Scene Analysis (Grouping View)** - Bregman's ASA framework
3.  **Pillar 3: Cognitive Neuroscience (Architecture View)** - Rauschecker & Scott's dual stream hypothesis
4.  **Pillar 4: Clinical Audiology (Stress-Test View)** - Katz's Buffalo Model APD categories

------------------------------------------------------------------------

## Taxonomy 1: Gaver's Ecological Sound Taxonomy

**Source**: Gaver, W. W. (1993). What in the world do we hear? An ecological approach to auditory event perception. *Ecological Psychology*, 5(1), 1-29.

### Overview

Gaver proposes an ecological approach to "everyday listening" - the experience of hearing **events** rather than sounds per se. The taxonomy organizes sound-producing events by the **physics of their material sources**, not by their acoustic properties.

### Core Framework

**Tripartite Division by Material Type:**

``` mermaid
graph TD
    A[Sound-Producing Events] --> B[Vibrating Solids]
    A --> C[Liquids]
    A --> D[Aerodynamics/Gases]

    B --> B1[Impact]
    B --> B2[Scraping]
    B --> B3[Rolling]

    C --> C1[Dripping]
    C --> C2[Pouring]
    C --> C3[Splashing]

    D --> D1[Explosions]
    D --> D2[Hissing]
    D --> D3[Aerodynamic Flow]

    style A fill:#e1f5ff
    style B fill:#ffe1e1
    style C fill:#e1ffe1
    style D fill:#fff5e1
```

### Hierarchical Organization

``` mermaid
graph LR
    A[Simple Interactions] --> B[Basic Level Events]
    B --> C[Temporal Patterning]
    B --> D[Compound Sources]
    B --> E[Hybrid Sources]
    C --> F[Complex Events]
    D --> F
    E --> F

    style A fill:#e1f5ff
    style F fill:#ffe1e1
```

### Key Principles

1.  **Source Attributes Over Sound Attributes**
    -   Focus on properties of the **event** (size, force, material)
    -   Not on properties of the **sound** (pitch, loudness, timbre)
2.  **Perceptual Information in Structured Energy**
    -   Sound conveys information about events at locations in environment
    -   "What in the world do we hear?" (events) vs. "What sounds do we hear?" (sensations)
3.  **Ecological Validity**
    -   Based on naturally occurring sound-producing events
    -   Contrasts with traditional psychoacoustics focus on musical sounds

### Relevance to Benchmark

-   **Physics Engine**: Reasoning about sound-producing events based on physical laws
-   **Layer 3 Inferential Tasks**: Causal reasoning from environmental sounds
-   **Complementary to CASA**: Provides source taxonomy while CASA provides grouping mechanisms

------------------------------------------------------------------------

## Taxonomy 2: Bregman's Auditory Scene Analysis (ASA) Framework

**Source**: Bregman, A. S. (1990). *Auditory Scene Analysis: The Perceptual Organization of Sound*. MIT Press.

### Overview

Bregman's ASA framework addresses the fundamental problem: How does the auditory system **organize** mixed acoustic energy into separate mental representations of distinct sound sources? The taxonomy distinguishes between **primitive** (automatic) and **schema-based** (knowledge-driven) processes.

### Core Framework: Two Processing Modes

``` mermaid
graph TD
    A[Auditory Scene Analysis] --> B[Primitive Scene Analysis]
    A --> C[Schema-Based Analysis]

    B --> B1[Bottom-Up]
    B --> B2[Automatic/Innate]
    B --> B3[No Conscious Control]
    B --> B4[Acoustic Cues Only]

    C --> C1[Top-Down]
    C --> C2[Uses Prior Learning]
    C --> C3[Voluntary Attention]
    C --> C4[Knowledge-Driven]

    style A fill:#e1f5ff
    style B fill:#ffe1e1
    style C fill:#fff5e1
```

### Two Dimensions of Grouping

``` mermaid
graph LR
    A[Auditory Grouping] --> B[Sequential Integration]
    A --> C[Simultaneous Integration]

    B --> B1[Temporal Dimension]
    B --> B2[Stream Segregation]
    B --> B3[Sequential Properties:<br/>Melody, Rhythm]

    C --> C1[Spectral Dimension]
    C --> C2[Spectral Partitioning]
    C --> C3[Spectral Properties:<br/>Timbre, Pitch]

    style A fill:#e1f5ff
    style B fill:#ffe1e1
    style C fill:#e1ffe1
```

### Sequential Integration: Stream Segregation

**Factors Influencing Segregation:**

``` mermaid
graph TD
    A[Stream Segregation] --> B[Frequency Separation]
    A --> C[Temporal Rate]
    A --> D[Spatial Location]
    A --> E[Onset Synchrony]

    B --> F{Segregation<br/>Strength}
    C --> F
    D --> F
    E --> F

    F --> G[Single Stream<br/>Coherent Melody]
    F --> H[Multiple Streams<br/>Separate Sources]

    style A fill:#e1f5ff
    style G fill:#e1ffe1
    style H fill:#ffe1e1
```

### Simultaneous Integration: Fusion vs. Segregation

**Onset Synchrony Principle:**

``` mermaid
graph TD
    A[Two Concurrent Tones] --> B{Onset Timing?}

    B -->|Synchronous| C[Fusion]
    B -->|Asynchronous| D[Segregation]

    C --> C1[Rich Complex Tone]
    C --> C2[Single Perceived Source]
    C --> C3[Combined Timbre]

    D --> D1[Two Pure Tones]
    D --> D2[Separate Perceived Sources]
    D --> D3[Individual Timbres]

    style A fill:#e1f5ff
    style C fill:#e1ffe1
    style D fill:#ffe1e1
```

### Key Grouping Principles

``` mermaid
graph LR
    A[Grouping<br/>Principles] --> B[Common Fate]
    A --> C[Onset Synchrony]
    A --> D[Frequency Proximity]
    A --> E[Spatial Proximity]
    A --> F[Temporal Continuity]
    A --> G[Harmonic Relations]

    B --> H[Components that<br/>change together<br/>belong together]
    C --> I[Simultaneous onsets<br/>promote fusion]
    D --> J[Similar frequencies<br/>group together]
    E --> K[Same location<br/>promotes grouping]
    F --> L[Continuous patterns<br/>maintain streams]
    G --> M[Harmonic series<br/>indicates single source]

    style A fill:#e1f5ff
```

### Primitive vs. Schema-Based: Distinguishing Characteristics

| Property        | Primitive                    | Schema-Based             |
|-----------------|------------------------------|--------------------------|
| **Control**     | Automatic                    | Voluntary attention      |
| **Learning**    | Innate                       | Requires prior knowledge |
| **Speed**       | Fast                         | Can be slower            |
| **Flexibility** | Fixed rules                  | Context-dependent        |
| **Examples**    | Frequency proximity grouping | Phonemic restoration     |

### Relevance to Benchmark

-   **Attention Engine**: Layer 2 tasks test stream segregation under cognitive load
-   **Layer 1 Foundational**: Primitive segregation mechanisms
-   **Layer 2 Cognitive Control**: Schema-based segregation with attention
-   **Layer 3 Inferential**: Knowledge-driven scene analysis

------------------------------------------------------------------------

## Taxonomy 3: Rauschecker & Scott's Dual Stream Hypothesis

**Source**: Rauschecker, J. P., & Scott, S. K. (2009). Maps and streams in the auditory cortex: nonhuman primates illuminate human speech processing. *Nature Neuroscience*, 12(6), 718-724.

### Overview

The dual stream hypothesis describes **parallel processing pathways** in auditory cortex, analogous to the visual "what/where" streams. This neuroanatomical framework separates **object identification** from **spatial/action processing**.

### Core Framework: Two Streams

``` mermaid
graph TD
    A[Primary Auditory Cortex<br/>Core: A1] --> B[Ventral What Stream]
    A --> C[Dorsal Where/How Stream]

    B --> B1[Anterior Belt: AL]
    B --> B2[Anterior Superior<br/>Temporal Cortex]
    B --> B3[Ventrolateral PFC]

    C --> C1[Posterior Belt: CL]
    C --> C2[Posterior Superior<br/>Temporal pST]
    C --> C3[Ventral Inferior<br/>Parietal VIP]
    C --> C4[Dorsolateral PFC]

    B1 --> B4[Object Identification]
    B2 --> B5[Speech Recognition]
    B3 --> B6[Categorization]

    C1 --> C5[Sound Localization]
    C2 --> C6[Spatial Processing]
    C3 --> C7[Sensorimotor]
    C4 --> C8[Action Planning]

    style A fill:#e1f5ff
    style B fill:#ffe1e1
    style C fill:#fff5e1
    style B4 fill:#ffcccc
    style B5 fill:#ffcccc
    style B6 fill:#ffcccc
    style C5 fill:#ffffcc
    style C6 fill:#ffffcc
    style C7 fill:#ffffcc
    style C8 fill:#ffffcc
```

### Ventral "What" Stream: Hierarchical Processing

``` mermaid
graph TD
    A[Core: A1<br/>Tonotopic Maps] --> B[Belt Areas<br/>Band-pass Noise]
    B --> C[Parabelt<br/>Complex Patterns]
    C --> D[Anterior STG<br/>Speech Sounds]
    D --> E[Voice Areas<br/>Speaker Identity]
    D --> F[VLPFC<br/>Categories]

    A --> A1[Simple:<br/>Pure Tones]
    B --> B1[Intermediate:<br/>Noise Bursts]
    C --> C1[Complex:<br/>Words]
    D --> D1[Linguistic:<br/>Sentences]
    E --> E1[Invariant:<br/>Voice Recognition]
    F --> F1[Abstract:<br/>Semantic Categories]

    style A fill:#e1f5ff
    style F fill:#ffe1e1
```

**Key Functions:** - **Auditory Object Identification**: Pattern recognition - **Speech Perception**: Hierarchical encoding of phonemes → syllables → words - **Voice Perception**: Speaker recognition and vocal characteristics - **Invariance**: Perceptual constancy despite acoustic variation - **Categorization**: Formation of abstract auditory categories

### Dorsal "Where/How" Stream: Spatial and Sensorimotor Processing

``` mermaid
graph TD
    A[Core: A1] --> B[Caudal Lateral Belt: CL]
    B --> C[Posterior Superior<br/>Temporal: pST]
    C --> D[Ventral Inferior<br/>Parietal: VIP]
    D --> E[Dorsolateral PFC]

    B --> B1[Spatial Selectivity]
    C --> C1[Location Analysis]
    D --> D1[Auditory-Motor<br/>Integration]
    E --> E1[Action Planning]

    style A fill:#e1f5ff
    style E fill:#ffe1e1
```

**Key Functions:** - **Sound Localization**: Where is the sound coming from? - **Auditory Motion**: Direction and velocity of moving sounds - **Sensorimotor Integration**: Linking perception to action - **Speech Production**: Auditory-motor mapping for vocalization

### Hierarchical Organization Principles

``` mermaid
graph LR
    A[Lower Areas] --> B[Higher Areas]

    A --> A1[Simple RFs]
    A --> A2[Local Processing]
    A --> A3[Tonotopic]

    B --> B1[Complex RFs]
    B --> B2[Convergent Processing]
    B --> B3[Invariant Representations]

    style A fill:#e1ffe1
    style B fill:#ffe1e1
```

### Dual Interpretation: What/Where vs. Perception/Action

| Framework             | Ventral Stream  | Dorsal Stream    |
|-----------------------|-----------------|------------------|
| **What/Where**        | Object Identity | Spatial Location |
| **Perception/Action** | Perception      | Sensorimotor/How |
| **Emphasis**          | Recognition     | Action Planning  |

### Relevance to Benchmark

-   **Task Structure**: Separates recognition tasks (ventral) from spatial tasks (dorsal)
-   **Ensures Validity**: Ventral stream tasks should not require spatial processing
-   **Layer 1**: Hierarchical processing from simple to complex
-   **Layer 2**: Dorsal stream involvement in attention and cognitive control
-   **Layer 3**: Ventral stream's role in high-level categorization and inference

------------------------------------------------------------------------

## Taxonomy 4: Katz's Buffalo Model (APD Categories)

**Source**: Katz, J. (2025). The Buffalo Model—a comprehensive approach to evaluate and remediate auditory processing disorders. *Audiology Today*, 37(1), 18-25.

**Note**: This is a retrospective of the original 1992 model.

### Overview

The Buffalo Model provides a **clinical diagnostic framework** for categorizing Auditory Processing Disorders (APD). Based on multidimensional scoring from three core tests, it identifies **four distinct categories** of auditory dysfunction.

### Core Framework: Four APD Categories

``` mermaid
graph TD
    A[Buffalo Model<br/>APD Categories] --> B[Category 1:<br/>Decoding]
    A --> C[Category 2:<br/>Tolerance-Fading Memory]
    A --> D[Category 3:<br/>Integration]
    A --> E[Category 4:<br/>Organization]

    B --> B1[Basic auditory<br/>processing]
    B --> B2[Sound-symbol<br/>relationships]
    B --> B3[Phonemic analysis]

    C --> C1[Auditory memory<br/>deficits]
    C --> C2[Problems in<br/>noise]
    C --> C3[Tolerance for<br/>background]

    D --> D1[Interhemispheric<br/>integration]
    D --> D2[Combining info<br/>from both ears]
    D --> D3[Corpus callosum<br/>function]

    E --> E1[Sequencing]
    E --> E2[Organization of<br/>auditory info]
    E --> E3[Higher-level<br/>processing]

    style A fill:#e1f5ff
    style B fill:#ffe1e1
    style C fill:#e1ffe1
    style D fill:#fff5e1
    style E fill:#ffe1ff
```

### Three-Test Battery

``` mermaid
graph LR
    A[Buffalo Model<br/>Test Battery] --> B[Phonemic<br/>Synthesis Test<br/>PST]
    A --> C[Staggered<br/>Spondaic Word<br/>SSW]
    A --> D[Words-in-Noise<br/>Test]

    B --> B1[Phonemic<br/>blending skill]
    C --> C1[Central auditory<br/>function mapping]
    D --> D1[Speech-in-noise<br/>performance]

    B1 --> E[Multidimensional<br/>Scoring]
    C1 --> E
    D1 --> E

    E --> F[Four Category<br/>Classification]

    style A fill:#e1f5ff
    style E fill:#fff5e1
    style F fill:#ffe1e1
```

### Staggered Spondaic Word (SSW) Test Structure

``` mermaid
graph TD
    A[SSW Test Item] --> B[Right Ear:<br/>Up Stairs]
    A --> C[Left Ear:<br/>Down Town]

    B --> B1[R-NC: Up]
    B --> B2[R-C: Stairs]

    C --> C1[L-C: Down]
    C --> C2[L-NC: Town]

    B1 --> D{Four Conditions}
    B2 --> D
    C1 --> D
    C2 --> D

    D --> E[Regional Signs:<br/>20+ diagnostic<br/>indicators]

    style A fill:#e1f5ff
    style D fill:#fff5e1
    style E fill:#ffe1e1
```

**Key**: NC = Non-Competing, C = Competing

### Multidimensional Scoring Approach

``` mermaid
graph TD
    A[Multidimensional<br/>Scoring] --> B[Multiple Diagnostic<br/>Indicators per Test]

    B --> C[SSW:<br/>20+ Regional Signs]
    B --> D[PST:<br/>Phonemic Patterns]
    B --> E[WiN:<br/>Noise Tolerance]

    C --> F[Backup Support]
    D --> F
    E --> F

    F --> G[Expanded Diagnostic<br/>Information]

    G --> H[Academic Problems]
    G --> I[Communication<br/>Problems]

    style A fill:#e1f5ff
    style G fill:#fff5e1
```

### Diagnostic Flow

``` mermaid
graph LR
    A[Patient] --> B[Three-Test<br/>Battery]

    B --> C[PST Scores]
    B --> D[SSW Scores]
    B --> E[WiN Scores]

    C --> F[Pattern Analysis]
    D --> F
    E --> F

    F --> G{Category<br/>Assignment}

    G --> H[Decoding]
    G --> I[TFM]
    G --> J[Integration]
    G --> K[Organization]

    H --> L[Targeted<br/>Remediation]
    I --> L
    J --> L
    K --> L

    style A fill:#e1f5ff
    style F fill:#fff5e1
    style G fill:#ffe1e1
    style L fill:#e1ffe1
```

### Relevance to Benchmark

-   **Stress-Test View**: Clinical populations reveal breakdown patterns
-   **Diagnostic Categories**: Map potential failure modes in ML systems
-   **Multidimensional Scoring**: Suggests multiple metrics needed for comprehensive evaluation
-   **Layer Mapping**:
    -   **Decoding** → Layer 1 (Foundational)
    -   **Tolerance-Fading Memory** → Layer 2 (Cognitive Control under load)
    -   **Integration** → Layer 1-2 (Binaural/bilateral processing)
    -   **Organization** → Layer 2-3 (Sequencing and higher-order reasoning)

------------------------------------------------------------------------

## Cross-Taxonomy Integration

### Mapping Across the Four Pillars

``` mermaid
graph TD
    A[Auditory Perception<br/>Framework] --> B[Pillar 1:<br/>Ecological<br/>Gaver]
    A --> C[Pillar 2:<br/>CASA<br/>Bregman]
    A --> D[Pillar 3:<br/>Neuroscience<br/>Rauschecker]
    A --> E[Pillar 4:<br/>Clinical<br/>Katz]

    B --> B1[Physics View:<br/>What events<br/>produce sounds?]

    C --> C1[Grouping View:<br/>How are sounds<br/>organized?]

    D --> D1[Architecture View:<br/>Where/how does<br/>brain process?]

    E --> E1[Stress-Test View:<br/>What breaks<br/>down?]

    B1 --> F[Comprehensive<br/>Framework]
    C1 --> F
    D1 --> F
    E1 --> F

    style A fill:#e1f5ff
    style F fill:#ffe1e1
```

### Pillar Interactions

| Interaction | Description | Example |
|---------------------------|---------------------------|-------------------|
| **Gaver + Bregman** | Physical events produce acoustic cues that ASA uses for grouping | Impact sound onset synchrony → fusion |
| **Bregman + Rauschecker** | Sequential integration maps to dorsal stream; simultaneous integration to ventral stream | Stream segregation involves both what and where |
| **Rauschecker + Katz** | Neural architecture predicts breakdown patterns | Integration deficits suggest corpus callosum dysfunction |
| **Katz + Gaver** | Clinical deficits reveal ecological listening challenges | Decoding problems affect everyday event recognition |

### Unified Processing Model

``` mermaid
graph TD
    A[Acoustic Input] --> B[Physical Event<br/>Properties<br/>Gaver]

    B --> C{Primitive<br/>Segregation<br/>Bregman}

    C --> D[Sequential<br/>Grouping<br/>Temporal Streams]
    C --> E[Simultaneous<br/>Grouping<br/>Spectral Fusion]

    D --> F[Dorsal Stream<br/>Where/How<br/>Rauschecker]
    E --> G[Ventral Stream<br/>What<br/>Rauschecker]

    F --> H{Clinical<br/>Breakdown?<br/>Katz}
    G --> H

    H -->|Normal| I[Successful<br/>Perception]
    H -->|Decoding| J[Category 1<br/>Deficit]
    H -->|TFM| K[Category 2<br/>Deficit]
    H -->|Integration| L[Category 3<br/>Deficit]
    H -->|Organization| M[Category 4<br/>Deficit]

    style A fill:#e1f5ff
    style I fill:#e1ffe1
    style J fill:#ffe1e1
    style K fill:#ffe1e1
    style L fill:#ffe1e1
    style M fill:#ffe1e1
```

------------------------------------------------------------------------

## Implications for Benchmark Design

### Layer 1: Foundational (Perception & Schema)

**Pillar Contributions:** - **Gaver**: Test recognition of basic sound-producing events (impacts, liquids, aerodynamics) - **Bregman**: Test primitive segregation (onset synchrony, frequency proximity) - **Rauschecker**: Test hierarchical processing (simple tones → complex patterns → objects) - **Katz**: Baseline decoding abilities

**Example Tasks:** - Identify material type from impact sound (Gaver) - Segregate concurrent tones by onset asynchrony (Bregman) - Recognize increasingly complex auditory patterns (Rauschecker) - Phonemic synthesis without background (Katz)

### Layer 2: Cognitive Control (Attention & Load)

**Pillar Contributions:** - **Gaver**: Recognize events in complex environments (multiple simultaneous sources) - **Bregman**: Schema-based stream segregation under attention - **Rauschecker**: Dorsal stream spatial attention; ventral stream selective attention - **Katz**: Tolerance-Fading Memory (speech-in-noise)

**Example Tasks:** - Cocktail party effect: follow one speaker among many - Stream segregation under cognitive load - Spatial attention to target sound source - Words-in-noise recognition

### Layer 3: Inferential (Reasoning & Theory of Mind)

**Pillar Contributions:** - **Gaver**: Causal reasoning about sound-producing events - **Bregman**: Schema-based integration using world knowledge - **Rauschecker**: High-level categorization in ventral stream - **Katz**: Organization category (sequencing, higher-order processing)

**Example Tasks:** - Infer event sequence from complex soundscape (Gaver) - Phonemic restoration using linguistic context (Bregman) - Categorize sounds by semantic meaning (Rauschecker) - Detect anomalous sequences in auditory narratives (Katz)

------------------------------------------------------------------------

## Taxonomy Sources Summary

| Pillar | Paper | Taxonomy Type | Key Contribution |
|---------------|---------------|-------------------|-----------------------|
| **1: Ecological** | Gaver (1993) | Material-based classification | Physics of sound sources |
| **2: CASA** | Bregman (1990) | Process-based classification | Grouping mechanisms |
| **3: Neuro** | Rauschecker & Scott (2009) | Architecture-based classification | Neural processing streams |
| **4: Clinical** | Katz (2025/1992) | Deficit-based classification | Clinical breakdown patterns |

------------------------------------------------------------------------

## Conclusion

These four taxonomies provide complementary perspectives on auditory perception:

1.  **Gaver** tells us **what we hear** (events in the world)
2.  **Bregman** tells us **how we organize** what we hear (grouping processes)
3.  **Rauschecker** tells us **where and how the brain processes** what we hear (neural architecture)
4.  **Katz** tells us **what can go wrong** (clinical deficits)

Together, they form a **comprehensive framework** for designing ecologically valid, theoretically grounded, and clinically informed benchmarks for audio machine learning systems.

------------------------------------------------------------------------

**End of Taxonomy Report**

*For full paper details, see [local-references.md](../structure/local-references.md)*