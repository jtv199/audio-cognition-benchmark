# Benchmark Task Reference

**Generated**: December 8, 2025
**Purpose**: Complete task lists from existing audio benchmarks with labeled IDs for precise reference

---

## Benchmark 1 (B1): AIR-Bench

**Full Name**: AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension
**Authors**: Yang, Q., Xu, J., Liu, W., et al.
**Publication**: ACL 2024
**Source**: [arXiv:2402.07729](https://arxiv.org/abs/2402.07729), [GitHub](https://github.com/OFA-Sys/AIR-Bench)
**Verified**: December 8, 2025

### Foundation Tier: 19 Tasks (~19k single-choice questions)

#### Speech Tasks (9)

| ID | Task Name | Description |
|----|-----------|-------------|
| **B1.T1** | Speech grounding | Locating or identifying specific speech segments |
| **B1.T2** | Spoken language identification | Determining which language is spoken |
| **B1.T3** | Speaker gender recognition | Classifying speaker gender from audio |
| **B1.T4** | Emotion recognition | Detecting emotional tone in speech |
| **B1.T5** | Speaker age prediction | Estimating speaker age from vocal characteristics |
| **B1.T6** | Speech entity recognition | Identifying named entities within spoken content |
| **B1.T7** | Intent classification | Categorizing speaker intent or purpose |
| **B1.T8** | Speaker number verification | Determining if a specific number of speakers are present |
| **B1.T9** | Synthesized voice detection | Distinguishing artificial from natural speech |

#### Audio Tasks (4)

| ID | Task Name | Description |
|----|-----------|-------------|
| **B1.T10** | Audio grounding | Locating sound events within audio files |
| **B1.T11** | Vocal sound classification | Categorizing vocal sounds |
| **B1.T12** | Acoustic scene classification | Identifying environmental settings from sound |
| **B1.T13** | Sound question answering | Answering questions about sound content |

#### Music Tasks (6)

| ID | Task Name | Description |
|----|-----------|-------------|
| **B1.T14** | Music instruments classification | Identifying instruments in music |
| **B1.T15** | Music genre classification | Categorizing musical genre |
| **B1.T16** | Music note analysis-pitch | Analyzing pitch characteristics of musical notes |
| **B1.T17** | Music note analysis-velocity | Analyzing velocity/dynamics of notes |
| **B1.T18** | Music question answering | Answering questions about musical content |
| **B1.T19** | Music emotion detection | Identifying emotional expression in music |

### Chat Tier: ~2k open-ended Q&A instances

**Description**: Assesses comprehension of complex audio and capacity to follow instructions through open-ended question-and-answer format. Evaluated using GPT-4 for scoring.

### Key Characteristics
- **Evaluation**: Generative comprehension (models generate hypotheses directly)
- **Audio Types**: Human speech, natural sounds, music
- **Strengths**: Broad coverage across audio types; two-tier design (foundation + chat)
- **Gaps**: No explicit cognitive control (attention, working memory); no causal reasoning tasks

---

## Benchmark 2 (B2): AudioBench

**Full Name**: AudioBench: A Universal Benchmark for Audio Large Language Models
**Authors**: Wang, B., Zou, X., Lin, G., et al.
**Publication**: NAACL 2025
**Source**: [arXiv:2406.16020](https://arxiv.org/abs/2406.16020), [GitHub](https://github.com/AudioLLMs/AudioBench)
**Verified**: December 8, 2025 (from arXiv HTML version)

### 8 Tasks Across 26 Datasets (7 newly proposed)

#### Speech Understanding (4 tasks, 15 datasets)

| ID | Task Name | Datasets | Description |
|----|-----------|----------|-------------|
| **B2.T1** | ASR (Automatic Speech Recognition) | LibriSpeech-Clean, LibriSpeech-Other, CommonVoice-15, PeoplesSpeech, GigaSpeech, Tedlium3, Tedlium3-Longform, Earning-21, Earning-22 | Converting spoken content to text; tests robustness across environments, accents, noise |
| **B2.T2** | SQA (Speech Question Answering) | CN-College-Listen, SLUE-P2-SQA5, DREAM-TTS, Public-SG-SpeechQA | Responding to questions based on speech content (monologue and dialogue) |
| **B2.T3** | SI (Speech Instruction) | OpenHermes-Audio, ALPACA-Audio | Following direct instructions via audio input; tests natural human-computer interaction |

**Note**: B2.T1 includes noisy environments (LibriSpeech-Other) which may involve some attention capability but is not explicitly designed as an attention task.

#### Audio Scene Understanding (2 tasks, 5 datasets)

| ID | Task Name | Datasets | Description |
|----|-----------|----------|-------------|
| **B2.T4** | AQA (Audio Question Answering) | Clotho-AQA, WavCaps-QA, AudioCaps-QA | Answering questions about environmental context and non-speech sounds |
| **B2.T5** | AC (Audio Captioning) | WavCaps, AudioCaps | Generating descriptions for audio clips |

#### Voice Understanding / Paralinguistics (3 tasks, 6 datasets)

| ID | Task Name | Datasets | Description |
|----|-----------|----------|-------------|
| **B2.T6** | ER (Emotion Recognition) | IEMOCAP-Emotion, MELD-Sentiment, MELD-Emotion | Identifying emotional states conveyed through speech |
| **B2.T7** | AR (Accent Recognition) | VoxCeleb1-Accent | Recognizing speaker's likely origin based on accent |
| **B2.T8** | GR (Gender Recognition) | VoxCeleb1-Gender, IEMOCAP-Gender | Identifying gender based on vocal characteristics |

### Key Characteristics
- **Evaluation**: Task-specific metrics (WER for ASR, accuracy for classification, etc.)
- **Categories**: Speech understanding (4), Audio scene understanding (2), Voice understanding (3)
- **Strengths**: Standardized task definitions; comprehensive speech and emotion coverage
- **Gaps**: No attention/cognitive control tasks; no working memory tests; limited causal reasoning; no stress testing

---

## Benchmark 3 (B3): MMAU

**Full Name**: MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark
**Authors**: Sakshi, S., et al.
**Publication**: ICLR 2025
**Source**: [arXiv:2410.19168](https://arxiv.org/abs/2410.19168), [Website](https://mmaubench.github.io/)
**Verified**: December 8, 2025 (from arXiv abstract - full task list not publicly available)

### 27 Distinct Skills (12 Info-Retrieval + 15 Reasoning)

**⚠️ IMPORTANT**: The full enumeration of all 27 skills is not available in publicly accessible sources. The paper abstract and website describe the benchmark scope but do not list all tasks individually.

#### Confirmed Tasks (from abstract/website mentions)

| ID | Task/Skill Name | Category | Description |
|----|-----------------|----------|-------------|
| **B3.T1** | Role Mapping | Reasoning | Expert-level skill requiring role identification/mapping |
| **B3.T2** | Emotion Flip | Reasoning | Detecting contradictory or complex emotional states |
| **B3.T3** | Action Recognition | Reasoning | Identifying actions from audio cues |
| **B3.T4** | Phonemic Stress Pattern Analysis | Info-Retrieval or Reasoning | Analyzing phonemic stress patterns in speech |
| **B3.T5** | Temporal Reasoning | Reasoning | Reasoning about temporal relationships in audio |
| **B3.T6-T27** | [Additional 22 skills] | Mixed | **Requires full paper access to enumerate** |

#### General Characteristics

- **Total Questions**: 10k carefully curated audio clips with human-annotated Q&A
- **Domains**: Speech, environmental sounds, music
- **Question Types**:
  - Information Extraction: 3,499 questions (12 distinct skill types)
  - Reasoning: 6,501 questions (15 distinct skill types)
- **Format**: Multiple choice (reduces evaluation complexity)
- **Difficulty**: Expert-level knowledge and complex reasoning required

### Key Characteristics
- **Evaluation**: Multiple choice format
- **Emphasis**: Expert reasoning, domain-specific knowledge
- **Strengths**: Complex reasoning tasks; explicit "Reasoning" category; high difficulty
- **Gaps**: Full task list requires paper access; no explicit attention/working memory; limited stream segregation

### Performance Benchmarks (from paper)
- **Best proprietary model** (Gemini 2.0 Flash): 59.93% accuracy
- **Best open-source model** (Qwen2-Audio): 52.50% accuracy

---

## Benchmark 4 (B4): MMAU-Pro

**Full Name**: MMAU-Pro: A Challenging and Comprehensive Benchmark for Holistic Evaluation of Audio General Intelligence
**Authors**: Kumar, S., Sedláček, Š., Lokegaonkar, V., López, F., et al. (22+ authors)
**Publication**: Pre-print (Under Review, August 2025)
**Source**: [arXiv:2508.13992](https://arxiv.org/abs/2508.13992), [Website](https://sonalkum.github.io/mmau-pro)
**Verified**: December 8, 2025 (from arXiv full text)
**Local File**: `papers/benchmark/MMAU-Pro_2508.13992v1.pdf`

### 49 Distinct Skills Across Multiple Complex Dimensions

**⚠️ IMPORTANT**: MMAU-Pro significantly extends MMAU (B3) with more challenging scenarios including long-form audio (up to 10 minutes), multi-audio reasoning, spatial audio understanding, multicultural music, and instruction-following tasks. All audio is sourced "from the wild" rather than existing datasets.

#### Key Innovations Beyond Prior Benchmarks

| Dimension | Description |
|-----------|-------------|
| **Long-form Audio** | Audio clips up to 10 minutes duration (vs. typical short clips in other benchmarks) |
| **Multi-audio Reasoning** | Questions requiring reasoning across multiple audio clips simultaneously |
| **Spatial Audio** | 3D audio positioning and spatial reasoning tasks |
| **Multicultural Music** | Music from diverse cultural traditions beyond Western canon |
| **Open-ended QA** | Mix of multiple-choice AND open-ended response formats |
| **Instruction Following** | Multimodal instruction-following tasks with specific constraints |
| **Voice-Chat QA** | Understanding conversational audio with turn-taking and overlaps |
| **STEM Reasoning** | Questions requiring scientific, mathematical knowledge applied to audio |

#### Task Categories (49 Skills Total)

**Perceptual Skills** (Examples from paper):
- Speaker Role & Relationship Inference
- Speaker Characteristics & Demographics
- Prosody Detection
- Paralinguistic/Emotion Recognition
- Speech Activity & Turn-Taking Detection
- Acoustic Scene Reasoning
- Acoustic Source Characterization
- Acoustic Trend Estimation
- Material Sound Recognition
- Spatial Sound Perception
- Pitch & Melody Perception
- Harmony Perception & Analysis
- Rhythmic Pattern & Tempo Recognition
- Timbre Perception & Instrument Recognition
- Texture & Dynamic Range Perception
- Auditory Source Separation
- Audio Quality & Artifacts Detection

**Reasoning Skills** (Examples from paper):
- Temporal & Ordering Reasoning
- Quantitative Reasoning (Counting/Arithmetic)
- Contextual/Causal Scenario Reasoning
- Mathematical & Logical Reasoning
- World Knowledge Integration
- Action-Based Reasoning
- Procedural Reasoning
- Comparative Reasoning
- Emotion Interpretation
- Lyrical Content Analysis
- Musicological Knowledge
- Structure & Form Analysis
- Style & Genre Recognition
- Eco-Acoustic Knowledge
- Language/Accent Identification

**⚠️ Note**: Full enumeration of all 49 skills requires detailed analysis of the paper. The above lists represent confirmed skills visible in the paper's skill distribution figures and example questions.

#### Dataset Statistics

- **Total Instances**: 5,305 expert-annotated question-answer pairs
- **Audio Duration**: Up to 10 minutes per clip
- **Question Types**: Multiple-choice AND open-ended formats
- **Domains**: Speech, environmental sounds, music, and their mixtures
- **Source**: Audio collected "from the wild" (not from existing benchmark datasets)
- **Difficulty**: Designed to require multi-hop reasoning and expert-level knowledge

### Key Characteristics
- **Evaluation**: Multiple-choice (accuracy) + open-ended (retrieval-based framework proposed)
- **Audio Types**: Speech, environmental sounds, music, and complex mixtures
- **Strengths**: Most comprehensive benchmark to date; long-form audio; spatial reasoning; multi-audio tasks; multicultural content; instruction-following; open-ended QA
- **Novel Contributions**:
  - First benchmark with 10-minute audio clips
  - First to systematically test spatial audio reasoning
  - First to include multicultural music understanding
  - Introduces retrieval-based evaluation for open-ended responses

### Performance Benchmarks (from paper)

**Proprietary Models**:
- **Gemini 2.5 Flash**: 59.2% accuracy (best overall)
- Other proprietary models evaluated

**Open-source Models**:
- **Audio Flamingo 3**: 51.7% accuracy (best open-source)
- **Qwen2.5-Omni-7B-Instruct**: 52.2% accuracy (best open-weights omni model)

**Key Finding**: Even state-of-the-art models approach random performance in multiple categories, revealing significant gaps in current audio intelligence capabilities.

### Identified Model Limitations (from paper analysis)

- Shallow audio grounding
- Degradation in text-only and STEM reasoning when audio is involved
- Poor performance in multi-audio reasoning
- Limited spatial reasoning capabilities
- Weak understanding of multicultural music
- Difficulty with long-form audio comprehension

---

## Cross-Benchmark Summary

### Task Coverage by Category

| Category | B1 (AIR-Bench) | B2 (AudioBench) | B3 (MMAU) | B4 (MMAU-Pro) |
|----------|---------------|----------------|-----------|---------------|
| **Speech Recognition/Understanding** | ✓ Strong (9 tasks) | ✓ Strong (4 tasks, 15 datasets) | ✓ Included | ✓ Advanced (Voice-Chat QA, Turn-Taking) |
| **Audio Scene/Environmental** | ⚠ Moderate (4 tasks) | ⚠ Moderate (2 tasks) | ✓ Included | ✓ Advanced (Material Sounds, Eco-Acoustic) |
| **Music** | ✓ Strong (6 tasks) | ✗ Minimal | ✓ Included | ✓ Advanced (Multicultural Music) |
| **Emotion/Paralinguistics** | ⚠ Basic (2 tasks) | ⚠ Basic (1 task) | ✓ Advanced (Emotion Flip) | ✓ Advanced (Prosody, Emotion Interpretation) |
| **Reasoning/Inference** | ✗ Weak (QA only) | ✗ Weak (QA only) | ✓ Strong (15 reasoning types) | ✓ Very Strong (Multi-hop, STEM, World Knowledge) |
| **Attention/Cognitive Control** | ✗ None | ✗ None | ❓ Unknown | ⚠ Partial (Instruction Following, Multi-audio) |
| **Working Memory** | ✗ None | ✗ None | ❓ Unknown | ✓ Strong (Long-form audio up to 10 min) |
| **Stream Segregation** | ⚠ Implicit (speaker number) | ⚠ Implicit (multi-speaker QA) | ❓ Unknown | ✓ Explicit (Auditory Source Separation) |
| **Spatial Reasoning** | ✗ None | ✗ None | ✗ None | ✓ Novel (3D Spatial Audio tasks) |
| **Causal Reasoning** | ✗ None | ✗ None | ⚠ Partial (Action Recognition, Temporal) | ✓ Strong (Contextual/Causal Scenario Reasoning) |
| **Temporal Reasoning** | ⚠ Implicit (sequences) | ⚠ Implicit (sequences) | ✓ Explicit | ✓ Advanced (Temporal & Ordering) |

---

## Usage Notes

### Referencing Tasks in Analysis

When referencing benchmark tasks in the main combined-taxonomy-table.md or other documents, use the following format:

**Example**:
```
✓ B1.T12 (Acoustic scene classification)
⚠ B2.T4 (AQA - may include material sounds)
❓ B3 (Requires verification - task list not public)
✓ B4 (Spatial Audio reasoning, Long-form audio)
```

**Note**: B4 (MMAU-Pro) tasks are referenced by skill category rather than individual task IDs, as the 49 skills are organized thematically rather than sequentially numbered.

### Citation Format

**AIR-Bench**:
> Yang, Q., Xu, J., Liu, W., Chu, Y., Jiang, Z., Zhou, X., Leng, Y., Lv, Y., Zhao, Z., Zhou, C., & Zhou, J. (2024). AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024)* (pp. 1979–1998). https://arxiv.org/abs/2402.07729

**AudioBench**:
> Wang, B., Zou, X., Lin, G., Sun, S., Liu, Z., Zhang, W., Liu, Z., Aw, A. T., & Chen, N. F. (2025). AudioBench: A Universal Benchmark for Audio Large Language Models. In *Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2025)*. https://arxiv.org/abs/2406.16020

**MMAU**:
> Sakshi, S., et al. (2025). MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark. In *Proceedings of the 13th International Conference on Learning Representations (ICLR 2025)*. https://arxiv.org/abs/2410.19168

**MMAU-Pro**:
> Kumar, S., Sedláček, Š., Lokegaonkar, V., López, F., Yu, W., Anand, N., Ryu, H., Chen, L., Plička, M., Hlaváček, M., Ellingwood, W. F., Udupa, S., Hou, S., Ferner, A., Barahona, S., Bolaños, C., Rahi, S., Herrera-Alarcón, L., Dixit, S., Patil, S., Deshmukh, S., Koroshinadze, L., Liu, Y., Garcia Perera, L. P., Zanou, E., Stafylakis, T., Chung, J. S., Harwath, D., Zhang, C., Manocha, D., Lozano-Diez, A., Kesiraju, S., Ghosh, S., & Duraiswami, R. (2025). MMAU-Pro: A Challenging and Comprehensive Benchmark for Holistic Evaluation of Audio General Intelligence. Pre-print under review. https://arxiv.org/abs/2508.13992

---

**End of Benchmark Reference**
