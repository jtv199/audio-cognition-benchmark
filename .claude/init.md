Project Log: AI Audio Reasoning Benchmark
Date: December 8, 2025 Phase: Phase 1 - Literature Review & Taxonomy Selection Objective: Define the theoretical boundaries of "Human Auditory Capability" to construct a valid evaluation benchmark for "Audio Reasoning" in AI models.

1. Core Research Question
Current AI audio models excel at Perception (classifying "Dog bark"), but lack Reasoning (inferring "The dog is barking behind a wall, so I cannot see it"). To bridge this gap, this project analyzes how four distinct scientific fields categorize the hierarchy of human hearing to identify missing capabilities in current AI evaluation.

2. Theoretical Framework (The 4 Pillars)
We have established a multi-disciplinary taxonomy to ensure the benchmark covers the full spectrum of auditory cognition, from physics to pathology.

A. Ecological Psychology (The Physics View)
Source Taxonomy: Taxonomy of Everyday Listening (Gaver, 1993).   

Key Concept: Humans hear events, not just frequencies.

Core Categories:

Vibrating Solids: Impact, Scraping, Rolling (Mass/Texture detection).

Liquids: Dripping, Pouring (Viscosity/Volume detection).

Aerodynamics: Exploding, Hissing (Pressure/Force detection).

Benchmark Application: Tests the AI's "Physics Engine." Can the model infer material properties (wood vs. metal) or causal states (is the bottle full?) from sound alone?

B. Computational Auditory Scene Analysis (The Grouping View)
Source Taxonomy: Auditory Scene Analysis (Bregman, 1990).   

Key Concept: The separation of signal from noise via Primitive vs. Schema-based mechanisms.

Core Categories:

Primitive Segregation: Automatic grouping by pitch/temporal proximity (Bottom-up).

Schema-Based Segregation: Attention-driven grouping using learned patterns (Top-down).

Benchmark Application: Tests the AI's "Attention Engine." Can the model use a specific prompt (a schema) to "hear out" a target signal in a "cocktail party" scenario, or does it fail when signals overlap?

C. Cognitive Neuroscience (The Architecture View)
Source Taxonomy: Dual Stream Hypothesis (Rauschecker & Scott, 2009).   

Key Concept: The brain splits processing into Identity and Action/Space.

Core Categories:

Ventral Stream ("What"): Object identification and semantic mapping.

Dorsal Stream ("Where/How"): Spatial localization and sensorimotor reproduction.

Benchmark Application: Validates structural integrity. Ensures the benchmark scores "Object Recognition" (Ventral) separately from "Spatial Tracking/Action" (Dorsal), preventing a single metric from hiding specific deficits.

D. Clinical Audiology (The Stress-Test View)
Source Taxonomy: The Buffalo Model (Katz, 1992).   

Key Concept: Processing is defined by its Failure Modes under stress.

Core Categories:

Decoding: Speed of processing.

Tolerance-Fading Memory: Performance in noise + Short-term memory load.

Integration: Multimodal synthesis.

Benchmark Application: Design of "Adversarial" samples. We will use the "Tolerance-Fading Memory" concept to stress-test the AI's context window with noise, measuring at what point reasoning collapses.

3. Summary of Strategic Direction
The research indicates that to test Reasoning (rather than just classification), the benchmark must prioritize Ecological and CASA taxonomies.

Perception Tasks (Current State of AI): Identifying a sound (Ventral Stream).

Reasoning Tasks (Goal of Benchmark):

Causal Inference: "What made this sound?" (Ecological - Gaver).

Contextual Selection: "Find the specific voice in the crowd." (CASA - Bregman).

Spatial Logic: "Where is the object going?" (Neuro - Dorsal Stream).

4. Next Steps
[ ] Data Generation: Synthesize audio samples corresponding to Gaver’s interaction types (e.g., scrape vs. roll).

[ ] Task Design: Create "Schema" prompts for CASA tests (e.g., "Ignore the siren, track the footsteps").

[ ] Stress Testing: Apply noise layers derived from the Buffalo Model (Tolerance) to baseline datasets.

This summary captures the core components of your project plan and the key discussion points for your next session.

Project Title: Measuring Auditory Cognition

Core Objective: Develop a benchmark to evaluate Audio Large Language Models (AudioLLMs) on their ability to perform higher-order reasoning tasks, moving beyond simple transcription.

Taxonomy of Tasks: The project is structured around a three-layer cognitive hierarchy derived from the project proposal.

Layer 1: Foundational (Perception & Schema)

Goal: Test the model's ability to parse auditory scenes and understand environmental context.

Included Tasks:

Stream Segregation: Separating a target voice from background noise/other speakers. (Ref: Bregman, 1990)

Schema Congruity: Identifying sounds that are contextually inappropriate (e.g., chainsaw in a library). (Ref: Gaver, 1993)

Layer 2: Cognitive Control (Attention & Load)

Goal: Test executive function, inhibition, and resource management.

Included Tasks:

Selective Attention: The "Cocktail Party Effect"—focusing on one speaker while ignoring distractors. (Ref: Cherry, 1953)

Divided Attention: Monitoring two streams simultaneously (multitasking). (Ref: Broadbent, 1958)

Layer 3: Inferential (Reasoning & Theory of Mind)

Goal: Test high-level social and causal reasoning.

Included Tasks:

Paralinguistics: Interpreting intent/emotion (e.g., sarcasm) from prosody. (Ref: Scherer, 2003)

Causal Reasoning: Inferring a narrative sequence from environmental sounds (e.g., footsteps -> door open). (Ref: Ballas, 1993)

Excluded Domains:

Spatial Audio: Localization (requires binaural data).

Music Cognition: Melodic structure/theory (too specialized).

Low-Level Psychoacoustics: Gap detection/thresholds (likely trivial for models).

Key Discussion Points & Open Questions:

Strategic Differentiation:

Question: Should the project "double up" on foundational tasks covered by existing benchmarks (AIR-Bench, AudioBench) to prove robustness, or aggressively focus on the under-explored "Control" and "Inferential" layers?

Dataset Construction Methodology:

Question: For "Cocktail Party" tasks, is it better to synthetically mix clean datasets (perfect ground truth) or use "in-the-wild" recordings (realistic but hard to validate)?

Baselines:

Question: Do we need to run our own human trials for baselines, or can we rely on literature values?

Roadmap Risks:

Question: What are the typical "kill steps" or high-risk phases in this type of project (Data Gen vs. Inference vs. Eval)?

AI Usage Policy:

Question: What are the guidelines for using LLMs for research assistance (summarizing, formatting)?

Relevant Benchmarks Analyzed:

AIR-Bench: Focuses on "Foundation" vs. "Chat" tiers; introduces "Mixed Audio" tasks.

AudioBench: Focuses on standardizing tasks; introduces "Speech Instruction" (spoken commands).

MMAU: Focuses on "Expert Reasoning" and specific skills (e.g., role mapping, emotion flip); uses strict Multiple Choice format.

Role: You are a Senior Principal Researcher in Auditory Cognitive Science and Psychoacoustics.

Objective: I am developing a new AI benchmark for "Audio Reasoning." To ensure validity, I need to understand how established scientific fields categorize human auditory capabilities.

Constraint: Do NOT attempt to merge these fields into a single unified hierarchy. Do NOT map them to "Perception vs. Cognition." I need to see the distinct, native taxonomies used within each specific field.

Task: Conduct a deep literature review and present the specific taxonomies/frameworks used in the following four domains:

1. Clinical Audiology (The "Disorder" View)
   - Search for: Taxonomies of Central Auditory Processing Disorder (CAPD/APD).
   - Specific Models: Look for the "Buffalo Model" (Katz) or the ASHA (American Speech-Language-Hearing Association) classification of skills.
   - Question: How do clinicians categorize specific failure modes in hearing? (e.g., Decoding vs. Integration vs. Tolerance).

2. Cognitive Neuroscience (The "Anatomy" View)
   - Search for: The "Dual Stream Hypothesis" of the auditory cortex.
   - Key Authors: Rauschecker & Scott (2009).
   - Question: How do neuroscientists divide auditory processing pathways? (e.g., The "What" stream vs. The "Where/How" stream). What specific tasks belong to each stream?

3. Ecological Psychology (The "Physics" View)
   - Search for: "Ecological Psychoacoustics" and "Everyday Listening."
   - Key Author: William Gaver (1993).
   - Question: How does Gaver categorize sound based on the physics of the sound-producing event? (e.g., Solids vs. Liquids vs. Aerodynamics; Impact vs. Scraping).

4. Computational Auditory Scene Analysis (The "Grouping" View)
   - Search for: Albert Bregman’s framework for Auditory Scene Analysis (ASA).
   - Question: How does Bregman distinguish between "Primitive Grouping" (automatic) and "Schema-Based Grouping" (learned/attentional)?

Output Format:
For each of the 4 fields, provide:
- The Name of the Taxonomy/Model.
- The Core Categories (The list of skills/layers).
- A concrete example of a task or test used in that field for each category.
- Key Reference Paper/Citation.