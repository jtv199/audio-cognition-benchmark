# Research Methodology

**Project**: AI Audio Reasoning Benchmark
**Last Updated**: December 8, 2025

---

## Overview

This methodology follows a systematic multi-stage approach to develop a benchmark for evaluating Audio Large Language Models (AudioLLMs) on higher-order reasoning tasks, moving beyond simple transcription and classification.

**Core Research Question**: How do different scientific fields categorize "auditory cognition" and what does it mean for sound to "make sense"?

---

## Stage 1: Multi-Field Taxonomy Identification

**Status**: ✓ **COMPLETE**

### Objective
Identify distinct taxonomies from different scientific fields that define human auditory capability from complementary perspectives.

### Approach
- **Do NOT** merge fields into a single unified hierarchy
- **Do NOT** map to generic "Perception vs. Cognition"
- Preserve the **native taxonomies** used within each specific field

### Output: The 4 Pillars Framework

1. **Ecological Psychology (Physics View)**
   - Source: Gaver, W. W. (1993) - Taxonomy of Everyday Listening
   - Framework: Vibrating Solids, Liquids, Aerodynamics
   - Tests: AI's "Physics Engine" - material properties, causal states

2. **Computational Auditory Scene Analysis (Grouping View)**
   - Source: Bregman, A. S. (1990) - Auditory Scene Analysis
   - Framework: Primitive vs. Schema-based Segregation
   - Tests: AI's "Attention Engine" - signal separation, cocktail party

3. **Cognitive Neuroscience (Architecture View)**
   - Source: Rauschecker & Scott (2009) - Dual Stream Hypothesis
   - Framework: Ventral ("What") vs. Dorsal ("Where/How") streams
   - Tests: Structural integrity - prevents single metrics hiding deficits

4. **Clinical Audiology (Stress-Test View)**
   - Source: Katz (1992) - The Buffalo Model
   - Framework: Decoding, Tolerance-Fading Memory, Integration
   - Tests: Failure modes under adversarial conditions

---

## Stage 2: Deep Literature Analysis

**Status**: → **IN PROGRESS**

### Objective
Systematically review, catalog, and rate papers across the 4 pillars and supporting literature.

### 2.1: AI-Assisted Deep Analysis

**Tool**: Gemini (or other LLM research assistants)

**Tasks**:
- Generate abstracts for papers
- Rate importance (X/5 scale)
- Identify linking papers
- Extract key concepts and frameworks

**Deliverable**: Annotated bibliography with importance ratings

### 2.2: Citation Network Analysis

**Tool**: Connected Papers (https://www.connectedpapers.com/)

**Tasks**:
- Map citation networks for 4 pillar papers
- Identify highly-cited related work
- Find "bridge" papers connecting fields
- Discover recent extensions/critiques

**Deliverable**: Citation graphs showing research lineages

### Documentation System

**Files**:
- [`references.md`](../references.md) - Master bibliography (all references)
- [`local-references.md`](../local-references.md) - Local file catalog with status tracking

**Status Indicators**:
- ✓ Read & Summarized
- ⚠ Needs Review
- TBD (to be determined)

**Importance Scale**:
- 5/5: Foundational papers (defines core framework)
- 4/5: High importance (essential concepts)
- 3/5: Medium importance (supporting evidence)
- 2/5: Low importance (peripheral relevance)
- 1/5: Reference only (context/comparison)

---

## Stage 3: Taxonomy Consolidation

**Status**: → **IN PROGRESS**

### Objective
Determine which taxonomies/concepts are most critical for the benchmark design.

### Current Progress
- ✓ Foundational papers identified (4 pillars)
- ✓ Supporting literature mapped (Cherry, Broadbent, Scherer, Ballas)
- ⚠ 12 local papers need review/cataloging
- ⚠ Importance ratings needed for unreviewed papers

### Action Items
- [ ] Identify MIT Press book chapters (ISBN: 9780262269209) - likely Bregman chapters
- [ ] Review and catalog Elsevier article (doi: 1-s2.0-S0272494405801914)
- [ ] Review ArXiv preprints in tokenizer folder (2505.16845v1, 2506.22023v1)
- [ ] Assign importance ratings to all papers
- [ ] Add notes on relevance to project pillars/layers

---

## Stage 4: Cross-Taxonomy Comparison

**Status**: → **CURRENT SESSION GOAL**

### Goal 1: Cross-Field Taxonomy Analysis

**Objective**: Reference and analyze taxonomies from other scientific fields **beyond** the core 4 pillars to identify:
- Alternative categorization frameworks for auditory cognition
- Complementary perspectives that could strengthen benchmark validity
- Potential gaps in current theoretical coverage

**Deliverable**: Comparative analysis of taxonomies with assessment of their applicability to AI audio reasoning evaluation

**Candidate Fields to Explore**:
- Speech Perception Research
- Psycholinguistics
- Music Cognition (selectively - not full musicology)
- Animal Bioacoustics
- Acoustic Engineering
- Human-Computer Interaction (Auditory Display)

### Goal 2: Benchmark Competitive Analysis

**Objective**: Deep dive into existing AI audio benchmarks (AIR-Bench, AudioBench, MMAU, others) to map:
- **What they do**: Specific tasks and evaluation methods
- **Why they chose these tasks**: Underlying theoretical justification or gaps
- **What they lack**: Missing capabilities relative to human auditory cognition (using our 4-pillar framework as reference)

**Deliverable**: Gap analysis matrix showing opportunities for differentiation and areas of necessary overlap

**Benchmarks to Analyze**:
- AIR-Bench: Foundation vs. Chat tiers; "Mixed Audio" tasks
- AudioBench: Task standardization; "Speech Instruction" (spoken commands)
- MMAU: "Expert Reasoning"; Multiple Choice format; role mapping, emotion flip
- Others: [To be identified in competitive landscape search]

---

## Stage 5+: Task Design & Dataset Generation

**Status**: Not Yet Started

### Planned Future Stages

1. **Task Design**
   - Map 4 pillars to 3-layer hierarchy (Foundational, Cognitive Control, Inferential)
   - Define evaluation protocols
   - Create prompt schemas for CASA tests

2. **Dataset Generation**
   - Synthesize audio samples for Gaver's interaction types
   - Mix signals for cocktail party scenarios
   - Apply noise layers (Buffalo Model stress tests)

3. **Evaluation Framework**
   - Define metrics for each layer
   - Establish human baselines
   - Design validation studies

---

## Methodological Principles

### Multi-Tool Triangulation
- **You (Human)**: Strategic direction, critical analysis
- **Claude Code (Me)**: Literature review, synthesis, documentation
- **Gemini**: Deep paper analysis, importance rating
- **Connected Papers**: Citation network exploration

### Importance Rating Criteria

| Rating | Criteria | Role in Project |
|--------|----------|-----------------|
| 5/5 | Defines core theoretical framework; foundational taxonomy | **Essential** - Pillar papers |
| 4/5 | Essential concepts; validates framework; widely cited | **High Priority** - Supporting theory |
| 3/5 | Supporting evidence; extends specific concepts | **Medium Priority** - Task design |
| 2/5 | Peripheral relevance; provides context | **Low Priority** - Background |
| 1/5 | Reference only; comparison/contrast | **Optional** - Situating work |

### Documentation Standards

**File Naming Convention** (for local papers):
```
Author_Year_ShortTitle.pdf
```
Example: `Gaver_1993_WhatInTheWorldDoWeHear.pdf`

**Status Tracking System**:
- ✓ Read & Summarized - Full review completed, notes added
- ⚠ Needs Review - File present but not yet analyzed
- TBD - Requires identification/acquisition

**Version Control**:
- All methodology files timestamped
- Session logs maintained in `.claude/YYYY-MM-DD.md`
- Changes tracked in git

---

## Current Phase Summary

**We are here**: Between Stage 3 and Stage 4

**What's Done**:
- ✓ 4 Pillars established with foundational papers
- ✓ Documentation system created
- ✓ Local file inventory completed
- ✓ Session goals defined

**What's Next**:
1. Complete Stage 2 literature analysis (identify unknown papers)
2. Execute Stage 4 comparative analysis (cross-field taxonomies + benchmark gaps)
3. Move to Stage 5 task design

---

## Open Questions

### Strategic Differentiation
Should the project "double up" on foundational tasks covered by existing benchmarks (AIR-Bench, AudioBench) or aggressively focus on under-explored "Control" and "Inferential" layers?

### Dataset Construction
For "Cocktail Party" tasks, is it better to synthetically mix clean datasets (perfect ground truth) or use "in-the-wild" recordings (realistic but hard to validate)?

### Baselines
Do we need to run our own human trials for baselines, or can we rely on literature values?

### Roadmap Risks
What are the typical "kill steps" or high-risk phases in this type of project (Data Gen vs. Inference vs. Eval)?

---

*This methodology is a living document and will be updated as the project evolves.*
