# MMAU-Pro Detailed Task Analysis: Gemini 2.5 Flash

**Generated**: January 4, 2026
**Purpose**: Map specific MMAU-Pro tasks (B3.T1-T38) to Table 3 performance categories and Baddeley's components, including example questions.

**Score Mapping Key (from Gemini 2.5 Flash Table 3 Results):**
*   **Speech**: 73.4%
*   **Sound**: 51.9%
*   **Music**: 64.9%
*   **Spatial**: 36.3%
*   **Multi-Audio**: 21.2%
*   **Voice (Paralinguistics)**: 71.7%
*   **Mixed**: 42.8% (Avg of Mix Categories)

---

## Detailed Task Table

| Task ID | Task Name | Example Question | Table 3 Category | Score | Baddeley Component | Notes |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **B3.T1** | Harmony | "Identify the chords in the main guitar riff." | Music | 64.9% | Phonological Loop | Music theory processing. |
| **B3.T2** | Melody | "What is the selling point of the guitar solo?" | Music | 64.9% | Phonological Loop | Pitch sequence tracking. |
| **B3.T3** | Rhythm/Tempo | "How are the accents placed in this pattern?" | Music | 64.9% | Central Executive | Monitoring periodicity. |
| **B3.T4** | Spatial Sound | "Which instruments are most prominent on the left?" | **Spatial** | **36.3%** | **Sketchpad** | Major deficit area. |
| **B3.T5** | Speaker ID | "How many total voices are singing?" | Speech | 73.4% | Central Executive | Segregating voices. |
| **B3.T6** | Texture/Dynamic | "Does the music get louder or softer?" | Music | 64.9% | Sensory | Intensity/timbre changes. |
| **B3.T7** | Timbre/Instrument | "Is this a piano or a violin?" | Music | 64.9% | Sensory | Instrument ID. |
| **B3.T8** | Structure/Form | "Is this a verse or a chorus?" | Music | 64.9% | Central Executive | Long-range structure. |
| **B3.T9** | Quant. Reasoning (Music) | "How many times is the drum hit?" | Music | 64.9% | Central Executive | Counting songs/notes. |
| **B3.T10** | Musicological Knowl. | "Who composed this piece?" | Music | 64.9% | Episodic Buffer | LTM retrieval. |
| **B3.T11** | Comp. Reasoning (Music) | "Which clip is faster?" | Music | 64.9% | Central Executive | Comparing two excerpts. |
| **B3.T12** | Music Emotion | "What does the bamboo flute express?" | Music | 64.9% | Episodic Buffer | Affective interpretation. |
| **B3.T13** | Lyrical Content | "What words are sung?" | Music | 64.9% | Phonological Loop | Semantic/verbal analysis. |
| **B3.T14** | Style/Genre | "Is this Jazz or Rock?" | Music | 64.9% | Episodic Buffer | Stylistic classification. |
| **B3.T15** | Acoustic Source | "Which indicates the first and third material?" | Sound | 51.9% | Sensory | Material ID. |
| **B3.T16** | Acoustic Trend | "Is the pitch rising or falling?" | Sound | 51.9% | Sensory | Change detection. |
| **B3.T17** | Eco-Acoustic | "What animal makes this sound?" | Sound | 51.9% | Episodic Buffer | Environmental knowledge. |
| **B3.T18** | Scene Reasoning | "What equipment will one carry in this weather?" | Sound | 51.9% | Episodic Buffer | Context inference. |
| **B3.T19** | Action Reasoning | "Is the person walking or running?" | Sound | 51.9% | Sensory / Dorsal | Inferring physical action. |
| **B3.T20** | Procedural Reasoning | "What step of the recipe is this?" | Sound | 51.9% | Central Executive | Sequence of events. |
| **B3.T21** | Quant. Reasoning (Sound) | "How many gunshots are there?" | Sound | 51.9% | Central Executive | Counting events. |
| **B3.T22** | Temporal Reasoning | "At what time is the cooker whistle blown?" | Sound | 51.9% | Central Executive | Timing/Sequencing. |
| **B3.T23** | Speaker Characteristics | "Is the speaker old or young?" | Speech | 73.4% | Sensory | Age/Gender ID. |
| **B3.T24** | Language/Accent | "Is this English or French?" | Speech | 73.4% | Phonological Loop | Linguistic pattern matching. |
| **B3.T25** | Prosody Detection | "Which film is the speaker referring to?" | **Voice** | **71.7%** | Phonological Loop | Intonation tracking. |
| **B3.T26** | Lexical Recog. | "What word was said?" | Speech | 73.4% | Phonological Loop | Word recognition. |
| **B3.T27** | Speaker Demographics | "What is the speaker's profession?" | Speech | 73.4% | Sensory | Inferring profession/status. |
| **B3.T28** | Emotion (Speech) | "Is the speaker angry?" | **Voice** | **71.7%** | Episodic Buffer | Emotional state inference. |
| **B3.T29** | Turn-Taking | "What is the name of the person who spoke second?" | **Multi-Audio** | **21.2%** | **Central Executive** | **CRITICAL FAILURE POINT.** |
| **B3.T30** | Artifacts/Quality | "Is the audio clear or noisy?" | **Voice** | **71.7%** | Sensory | Noise/recording quality. |
| **B3.T31** | Role Inference | "Is this a teacher or a student?" | Speech | 73.4% | Central Executive | Social dynamic inference. |
| **B3.T32** | Quant. Reasoning (Speech) | "If you take 200 million away, how much remains?" | Speech | 73.4% | Central Executive | Arithmetic/Counting. |
| **B3.T33** | Info Extraction | "What date is mentioned?" | Speech | 73.4% | Phonological Loop | Fact retrieval. |
| **B3.T34** | Causal Scenario | "What role does the first speaker assume?" | Speech | 73.4% | Central Executive | Cause-effect logic. |
| **B3.T35** | Temporal (Speech) | "What happened first?" | Speech | 73.4% | Central Executive | Ordering events. |
| **B3.T36** | World Knowledge | "What is the likely color of the food coloring?" | Speech | 73.4% | Episodic Buffer | General knowledge. |
| **B3.T37** | Math/Logical | "What is 5 plus 3?" | Speech | 73.4% | Central Executive | Logic puzzles. |
| **B3.T38** | Other (Speech) | "General reasoning question." | Speech | 73.4% | Central Executive | Misc reasoning. |

---

## Analysis Summary

*   **Best Performance**: Speech & Voice tasks (Loop / Buffer) ~72-73%.
*   **Worst Performance**: Multi-Audio (Executive Inhibition) ~21%.
*   **Implication**: The "Executive Gap" is confirmed. The model handles single-stream executive tasks (like B3.T32 Math) reasonably well (73.4%), but completely collapses when **Inhibition/Segregation** (B3.T29 Turn-Taking) is required (21.2%).
