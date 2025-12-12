# Audio Cognition Benchmark - Project Overview

## Executive Summary

This project develops a comprehensive benchmark to evaluate Audio Large Language Models (AudioLLMs) on **higher-order reasoning tasks**, moving beyond simple transcription and classification. The core innovation is bridging the gap between what AI models currently excel at (**Perception** - identifying "dog bark") and what they struggle with (**Reasoning** - inferring "The dog is barking behind a wall, so I cannot see it").

**Current Status**: Phase 1 - Literature Review & Taxonomy Mapping (90% Complete)

**Repository**: https://github.com/jtv199/audio-cognition-benchmark

---

## Project Goals

### Primary Objective
Define the theoretical boundaries of "Human Auditory Capability" to construct a valid evaluation benchmark for "Audio Reasoning" in AI models by:

1. **Referencing multiple cognitive frameworks** from psychology and neuroscience to identify the full spectrum of auditory cognition tasks
2. **Mapping these tasks** across existing AI audio benchmarks (AIR-Bench, AudioBench, MMAU-Pro, WavCaps)
3. **Identifying gaps** in current benchmark coverage that represent missing capabilities in AI evaluation
4. **Establishing a systematic taxonomy** that can guide future benchmark development

### Key Research Question
*"How do different scientific fields categorize the hierarchy of human hearing, and what does this reveal about missing capabilities in current AI audio evaluation?"*

---

## Theoretical Framework: The Four Pillars

Our multi-disciplinary approach ensures comprehensive coverage from physics to pathology:

### Pillar 1: Ecological Psychology (The Physics View)
**Source**: Gaver, W. (1993) - *Taxonomy of Everyday Listening*

**Key Concept**: Humans hear **events**, not just frequencies.

**Core Categories**:
- **Vibrating Solids**: Impact, Scraping, Rolling → Mass/Texture detection
- **Liquids**: Dripping, Pouring → Viscosity/Volume detection
- **Aerodynamics**: Exploding, Hissing → Pressure/Force detection

**Benchmark Application**: Tests the AI's "Physics Engine" - Can it infer material properties (wood vs. metal) or causal states (is the bottle full?) from sound alone?

---

### Pillar 2: Computational Auditory Scene Analysis (The Grouping View)
**Source**: Bregman, A. (1990) - *Auditory Scene Analysis*

**Key Concept**: Separation of signal from noise via Primitive vs. Schema-based mechanisms.

**Core Categories**:
- **Primitive Segregation**: Automatic grouping by pitch/temporal proximity (bottom-up)
- **Schema-Based Segregation**: Attention-driven grouping using learned patterns (top-down)

**Benchmark Application**: Tests the AI's "Attention Engine" - Can it use a specific prompt (a schema) to "hear out" a target signal in a "cocktail party" scenario when signals overlap?

---

### Pillar 3: Cognitive Neuroscience (The Architecture View)
**Source**: Rauschecker & Scott (2009) - *Dual Stream Hypothesis*

**Key Concept**: The brain splits processing into Identity and Action/Space pathways.

**Core Categories**:
- **Ventral Stream ("What")**: Object identification and semantic mapping
- **Dorsal Stream ("Where/How")**: Spatial localization and sensorimotor reproduction

**Benchmark Application**: Validates structural integrity - Ensures the benchmark scores "Object Recognition" (Ventral) separately from "Spatial Tracking/Action" (Dorsal), preventing a single metric from hiding specific deficits.

---

### Pillar 4: Clinical Audiology (The Stress-Test View)
**Source**: Katz (1992) - *The Buffalo Model*

**Key Concept**: Processing is defined by its **failure modes** under stress.

**Core Categories**:
- **Decoding**: Speed of processing
- **Tolerance-Fading Memory**: Performance in noise + short-term memory load
- **Integration**: Multimodal synthesis

**Benchmark Application**: Design of adversarial samples - Uses "Tolerance-Fading Memory" to stress-test AI's context window with noise, measuring at what point reasoning collapses.

---

## Three-Layer Task Hierarchy

### Layer 1: Foundational (Perception & Schema) 🦎
**Goal**: Test the model's ability to parse auditory scenes and understand environmental context.

**Example Tasks**:
- **Stream Segregation**: Separating a target voice from background noise/other speakers
- **Schema Congruity**: Identifying sounds that are contextually inappropriate (e.g., chainsaw in a library)
- **Material Identification**: Inferring object material from impact sound (wood vs. metal)
- **Harmonic Grouping**: Identifying which frequency components belong together

**Analogy**: "Lizard Brain" - Basic perception, automatic processing, immediate pattern recognition

---

### Layer 2: Cognitive Control (Attention & Load) 🐕
**Goal**: Test executive function, inhibition, and resource management.

**Example Tasks**:
- **Selective Attention**: "Cocktail Party Effect" - focusing on one speaker while ignoring distractors
- **Divided Attention**: Monitoring two streams simultaneously (multitasking)
- **Attention Switching**: Rapidly shifting focus between different audio sources
- **Phonemic Restoration**: Filling in missing speech segments based on context

**Analogy**: "Dog Brain" - Attention control, working memory, cognitive flexibility

---

### Layer 3: Inferential (Reasoning & Theory of Mind) 🐵
**Goal**: Test high-level social and causal reasoning.

**Example Tasks**:
- **Paralinguistics**: Interpreting intent/emotion (e.g., sarcasm) from prosody
- **Causal Reasoning**: Inferring narrative sequence from environmental sounds (footsteps → door open)
- **Theory of Mind**: Understanding speaker intentions and mental states
- **Environmental Reasoning**: Inferring broader context from soundscape

**Analogy**: "Monkey Brain" - Abstract reasoning, social cognition, causal inference

---

## Methodology & Accomplishments

### Phase 1: Literature Review & Taxonomy Mapping (December 2025)

#### Week 1 Deliverables (✅ Complete)

1. **[taxonomy.md](output/taxonomy.md)** - Complete 4-Pillar taxonomy with 14 mermaid diagrams visualizing each framework

2. **[taxonomy-overview.md](output/taxonomy-overview.md)** - 88 example questions across 35 leaf nodes from all four cognitive frameworks

3. **[analogies.md](output/analogies.md)** - Evolutionary framework (Lizard→Dog→Monkey) mapping cognitive complexity

4. **[benchmark-tasks.md](output/benchmark-tasks.md)** - Comprehensive catalog of existing benchmark tasks:
   - **B1 (AIR-Bench)**: 19 tasks (B1.T1-T19) - Audio/speech understanding
   - **B2 (AudioBench)**: 8 tasks (B2.T1-T8) - Core audio capabilities
   - **B3 (MMAU-Pro)**: 38 tasks (B3.T1-T38) - Music, sound, and speech skills
     - Music Domain: T1-T14 (Perceptual T1-T7, Reasoning T8-T14)
     - Sound Domain: T15-T22 (Perceptual T15-T17, Reasoning T18-T22)
     - Speech Domain: T23-T38 (Perceptual T23-T30, Reasoning T31-T38)
     - Plus 7 novel dimensions: long-form audio, multi-audio reasoning, spatial audio, multicultural music, voice QA, open-ended QA, instruction following

5. **[combined-taxonomy-table.md](output/combined-taxonomy-table.md)** - **Master document** mapping:
   - Full range of auditory cognition tasks organized by cognitive layers
   - Benchmark coverage analysis across AIR-Bench, AudioBench, MMAU-Pro, WavCaps
   - Task classifications based on all four cognitive frameworks (P1-P4)
   - **6 identified gaps** in current benchmark coverage with priority ratings

6. **Text Extraction Pipeline** - Automated extraction of first 2000 words from 12 research papers

7. **Session Documentation** - Detailed research logs in [.claude/](.claude/) directory tracking all decisions and findings

#### Key Statistics
- **35 leaf nodes** identified across 4 taxonomies
- **88 example questions** created for task prototyping
- **12 papers** processed and cataloged
- **4 frameworks** with complete mermaid visualizations
- **3 benchmarks** comprehensively analyzed (65 total tasks cataloged)
- **6 high-priority gaps** identified for novel task development

---

## Benchmark Competitive Analysis

### MMAU-Pro (Most Comprehensive)
**Strengths**:
- 38 explicitly defined skills with clear task IDs
- Organized by domain (music/sound/speech) and type (perceptual/reasoning)
- 7 novel testing dimensions (long-form, multi-audio, spatial, etc.)
- Strong coverage of Layer 3 (Inferential) tasks

**Gaps**:
- Limited Layer 2 (Cognitive Control) tasks
- No phonemic restoration or auditory stroop tests
- Minimal attention-switching or divided attention tasks

### AIR-Bench
**Strengths**:
- Foundation vs. Chat tiers for model capability assessment
- "Mixed Audio" tasks combining multiple sources

**Gaps**:
- Focuses heavily on Layer 1 (Perception)
- Limited higher-order reasoning tasks
- No explicit cognitive control tasks

### AudioBench
**Strengths**:
- Standardized task format
- "Speech Instruction" modality (spoken commands)

**Gaps**:
- Only 8 core tasks (least comprehensive)
- Limited coverage of Layer 2 and Layer 3
- Missing ecological/physics-based reasoning tasks

---

## Identified Gaps (Priority-Ranked)

| Priority | Task | Layer | Status | Rationale |
|----------|------|-------|--------|-----------|
| **5/5** | Phonemic Restoration | 2, 3 | ✗ Not in any benchmark | Core schema-based processing, critical for speech understanding |
| **4/5** | Auditory Stroop Test | 2 | ✗ Not in any benchmark | Cross-dimensional conflict (pitch vs. semantic meaning), tests cognitive control |
| **3/5** | Attention Switching | 2 | ⚠ B3 partial coverage | Rapid focus shifts between sources, essential for real-world listening |
| **3/5** | Explicit Divided Attention | 2 | ⚠ B3 partial coverage | True multitasking with dual-task paradigm |
| **2/5** | Onset Synchrony Detection | 1 | ✗ Not in any benchmark | Temporal binding, Gestalt grouping |
| **1/5** | Extreme Stress Testing | 1, 2, 3 | ⚠ B3 unclear | Buffalo Model "Tolerance" - performance degradation curves |

---

## Excluded Domains (With Justification)

### Sound Localization / Spatial Audio
**Reason**: Requires binaural recording (stereo with head-related transfer functions). Most datasets are mono. While MMAU-Pro includes spatial audio as a novel dimension, it's not systematically tested as a core capability.

### Music Cognition / Melodic Structure
**Reason**: Too specialized for general audio reasoning. MMAU-Pro covers music extensively (14 skills), providing sufficient coverage for this domain.

### Low-Level Psychoacoustics
**Reason**: Gap detection, frequency discrimination thresholds likely trivial for modern models. More relevant for testing audio encoder quality than reasoning.

---

## Strategic Direction & Next Steps

### Immediate Priorities (Week 2-3)

1. **Source Verification** ⏳
   - Verify all citations in taxonomy-overview.md using Google Scholar
   - Review audio cognition research books for additional frameworks
   - Comprehensive verification of AIR-Bench and AudioBench tasks (currently only AI-summarized)

2. **Dataset Availability Mapping** ⏳
   - Identify which tasks have existing datasets
   - Determine which tasks require custom dataset creation
   - Assess data generation feasibility (synthetic vs. in-the-wild)

3. **Human Baseline Research** ⏳
   - Map each task to established human cognition tests
   - Identify literature values for human performance baselines
   - Determine if custom human trials are needed

### Short-term (Month 1-2)

4. **Gap Task Prototyping**
   - Design evaluation protocols for 6 identified gaps
   - Create pilot datasets for top 2 priority gaps (Phonemic Restoration, Auditory Stroop)
   - Validate task difficulty with human subjects

5. **Benchmark Specification Document**
   - Formalize task definitions, evaluation metrics, and scoring
   - Define dataset requirements and quality standards
   - Establish human baseline comparisons

### Medium-term (Month 3-4)

6. **Data Generation Pipeline**
   - Synthesize audio samples for Gaver's interaction types (impact, scraping, rolling, etc.)
   - Create schema prompts for CASA tests ("Ignore siren, track footsteps")
   - Apply noise layers from Buffalo Model for stress testing

7. **Pilot Evaluation**
   - Test 2-3 AudioLLMs on initial task set
   - Validate evaluation pipeline and metrics
   - Iterate on task design based on model performance

---

## Key Open Questions

### Scientific Questions
1. **Differentiation Strategy**: Should we "double up" on foundational tasks to prove robustness, or aggressively focus on under-explored Layer 2/3 tasks?
   - *Ting's feedback*: "Different perspective, not 'double up.' Create comparison table." ✅ Addressed via combined-taxonomy-table.md

2. **Dataset Construction**: For "Cocktail Party" tasks, synthetic mixing (perfect ground truth) vs. in-the-wild recordings (realistic but hard to validate)?

3. **Baselines**: Run custom human trials or rely on literature values?

### Practical Questions
4. **Roadmap Risks**: What are typical "kill steps" in this project type? (Data Gen vs. Inference vs. Eval?)

5. **Collaboration Tools**: GitHub for documentation pooling + Notion for task organization

---

## Team Collaboration Setup

### Current Repository Structure
```
audio-cognition-benchmark/
├── output/                      # Main deliverables
│   ├── combined-taxonomy-table.md    # Master mapping document
│   ├── benchmark-tasks.md            # Task reference (B1-B3)
│   ├── taxonomy-overview.md          # 88 example questions
│   ├── taxonomy.md                   # 4-Pillar framework with diagrams
│   └── analogies.md                  # Evolutionary framework
├── papers/                      # Source research papers
│   ├── benchmark/               # Benchmark papers
│   └── extracted_text/          # PDF text extractions
├── .claude/                     # Daily research session logs
│   ├── 2025-12-08.md           # Taxonomy extraction session
│   ├── 2025-12-09.md           # B3 task IDs and updates
│   └── 2025-12-09-2.md         # Executive summary and gaps
├── references.md                # Bibliography
└── README.md                   # Project overview
```

### Collaboration Workflow
1. **GitHub Repository**: Code, documentation, and version control
2. **Notion (Planned)**: Task organization, meeting notes, progress tracking
3. **Session Logs**: All research decisions documented in `.claude/` with date stamps

### How to Contribute
- Email Jack (jtv199@gmail.com) with your GitHub username for repository access
- Review [combined-taxonomy-table.md](output/combined-taxonomy-table.md) for current taxonomy state
- Check [.claude/](.claude/) for latest research session notes
- Propose additions/changes via GitHub issues or pull requests

---

## Timeline & Milestones

### Phase 1: Literature Review & Taxonomy Mapping (December 2025) ✅ 90% Complete
- [x] Extract taxonomies from 4 cognitive frameworks
- [x] Create comprehensive task catalog across 3 benchmarks
- [x] Identify and prioritize gaps
- [ ] Verify all sources and citations
- [ ] Dataset availability mapping

### Phase 2: Task Design & Specification (January 2026)
- [ ] Design evaluation protocols for gap tasks
- [ ] Create pilot datasets for top 2 priority gaps
- [ ] Formalize benchmark specification document
- [ ] Establish human baseline comparisons

### Phase 3: Data Generation (February-March 2026)
- [ ] Synthesize audio samples for Ecological tasks
- [ ] Create schema-based CASA test prompts
- [ ] Build stress-testing pipeline with noise layers
- [ ] Quality validation and human testing

### Phase 4: Pilot Evaluation (April 2026)
- [ ] Test 2-3 AudioLLMs on initial task set
- [ ] Validate evaluation metrics
- [ ] Iterate on task design
- [ ] Prepare for full benchmark release

---

## Key References

### Foundational Papers
- **Bregman, A.** (1990). *Auditory Scene Analysis*. MIT Press.
- **Gaver, W.** (1993). "What in the World Do We Hear: An Ecological Approach to Auditory Event Perception." *Ecological Psychology*, 5(1), 1-29.
- **Rauschecker, J. P., & Scott, S. K.** (2009). "Maps and Streams in the Auditory Cortex." *Nature Neuroscience*, 12(6), 718-724.
- **Katz, J.** (1992). "Classification of Auditory Processing Disorders." In *Central Auditory Processing: A Transdisciplinary View*.

### Benchmark Papers
- **AIR-Bench**: Foundation vs. Chat evaluation tiers
- **AudioBench**: Standardized audio understanding tasks
- **MMAU-Pro**: Multi-modal audio understanding with expert reasoning (38 skills)

### Additional References
- Cherry, E. C. (1953). "Some Experiments on the Recognition of Speech, with One and with Two Ears." *Journal of the Acoustical Society of America*.
- Broadbent, D. E. (1958). *Perception and Communication*.
- Scherer, K. R. (2003). "Vocal Communication of Emotion." *Social Science Information*.
- Ballas, J. A. (1993). "Common Factors in the Identification of an Assortment of Brief Everyday Sounds." *Journal of Experimental Psychology*.

---

## Contact & Next Meeting

**Project Lead**: Jack
**Email**: jtv199@gmail.com
**Repository**: https://github.com/jtv199/audio-cognition-benchmark

**Next Meeting Topics**:
1. Review of comprehensive taxonomy and gap analysis
2. Discussion of dataset construction strategy (synthetic vs. in-the-wild)
3. Human baseline methodology
4. Task prioritization for Phase 2 prototyping
5. Collaboration workflow (GitHub + Notion setup)

---

## Acknowledgments

This research synthesizes insights from four distinct scientific traditions - ecological psychology, computational auditory scene analysis, cognitive neuroscience, and clinical audiology - to create a comprehensive framework for evaluating audio reasoning in AI systems.

Special thanks to the research team for feedback and guidance throughout Phase 1.

---

*Document Version: 1.0*
*Last Updated: December 9, 2025*
*Status: Phase 1 - Literature Review 90% Complete*
