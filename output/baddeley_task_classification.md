# Benchmark Classification: Baddeley's Model

**Generated**: January 4, 2026
**Purpose**: Classify existing benchmark tasks (B1-B4) according to Baddeley's Working Memory components using the established Decision Rules.

---

## Benchmark 1 (B1): AIR-Bench

| Task ID | Task Name | Task Example | Baddeley Component | Primary Decision Rule | Confidence | Notes |
|---------|-----------|--------------|--------------------|-----------------------|------------|-------|
| B1.T1 | Speech grounding | "At what timestamp does the speaker mention 'climate change'?" | **Episodic Buffer** | **Binding Rule**: Linking semantic content ("climate change") to a temporal timestamp. | 8/10 | Requires scanning LTM/Buffer for a match. |
| B1.T2 | Language ID | "Is this speaker speaking Mandarin, Spanish, or French?" | **Phonological Loop** | **Phonological Store**: Matching acoustic patterns to stored phonological templates. | 9/10 | LTM access, but primarily phonological pattern matching. |
| B1.T3 | Speaker Gender | "Is the speaker male or female?" | **Sensory / Pre-Cog** | **Threshold Rule**: Basic pitch/timbre detection, low cognitive load. | 9/10 | "Voice sensitive area" task, pre-executive. |
| B1.T4 | Emotion (Basic) | "Is the speaker happy, sad, angry, or neutral?" | **Sensory / Buffer** | **Threshold Rule**: Detecting prosodic features (pitch/speed). | 7/10 | Basic emotion is often automatic; complex is inferential. |
| B1.T5 | Speaker Age | "Is the speaker a child, young adult, middle-aged, or elderly?" | **Sensory / Pre-Cog** | **Threshold Rule**: Pitch/Timbre analysis. | 9/10 | Similar to gender. |
| B1.T6 | Entity Recog. | "What names or locations are mentioned in this audio?" | **Phonological Loop** | **Automatic Access Rule**: Speech enters the loop; requires recognizing specific lexical items. | 8/10 | Identifying "Names" requires LTM access (Buffer). |
| B1.T7 | Intent Class. | "Is the speaker asking a question, making a statement, or giving a command?" | **Episodic Buffer** | **Chunking Rule**: Synthesizing the *meaning* of the whole sentence (question vs. command). | 8/10 | Requires integrating prosody + semantics. |
| B1.T8 | Speaker Count | "Are there 1, 2, 3, or more speakers in this audio?" | **Central Executive** | **Inhibition Rule**: Segregating overlapping streams; "counting" is an executive process. | 9/10 | Must inhibit stream B to count stream A. |
| B1.T9 | Synth Voice Det. | "Is this voice real or synthetically generated?" | **Sensory / Pre-Cog** | **Threshold Rule**: Detecting subtle acoustic artifacts. | 9/10 | Fine-structure analysis. |
| B1.T10 | Audio Grounding | "At what timestamp does the dog bark?" | **Episodic Buffer** | **Binding Rule**: Linking sound event ("dog bark") to time. | 8/10 | Similar to T1. |
| B1.T11 | Vocal Sound Class. | "Is this a laugh, cough, sneeze, or cry?" | **Sensory / Pre-Cog** | **Threshold Rule**: Categorizing acoustic patterns (laugh/cough). | 9/10 | |
| B1.T12 | Acoustic Scene | "Is this audio from a restaurant, street, office, or park?" | **Episodic Buffer** | **Binding Rule**: Integrating multiple sound cues to form a "Scene" (Episode). | 8/10 | |
| B1.T13 | Sound QA | "What caused the loud crash in this audio?" | **Central Executive** | **Task Set Rule**: Reasoning about causal factors ("What caused the crash?"). | 7/10 | High-level reasoning requires CE manipulation. |
| B1.T14 | Instruments | "Which instruments are playing: piano, guitar, violin, or drums?" | **Sensory / Pre-Cog** | **Threshold Rule**: Timbre identification. | 9/10 | |
| B1.T15 | Genre Class. | "Is this jazz, classical, rock, or hip-hop?" | **Episodic Buffer** | **Binding Rule**: Integrating rhythm, instrumentation, and tempo into a style. | 8/10 | |
| B1.T16 | Note Pitch | "What is the pitch sequence of these notes?" | **Sensory / Pre-Cog** | **Threshold Rule**: Frequency detection. | 9/10 | |
| B1.T17 | Note Velocity | "Which note is played loudest?" | **Sensory / Pre-Cog** | **Threshold Rule**: Amplitude detection. | 9/10 | |
| B1.T18 | Music QA | "What is the tempo of this piece?" | **Central Executive** | **Task Set Rule**: Reasoning about musical structure. | 7/10 | |
| B1.T19 | Music Emotion | "Does this music convey joy, sadness, tension, or calm?" | **Episodic Buffer** | **Binding Rule**: Integrating musical features to infer mood. | 8/10 | |

---

## Benchmark 2 (B2): AudioBench

| Task ID | Task Name | Task Example | Baddeley Component | Primary Decision Rule | Confidence | Notes |
|---------|-----------|--------------|--------------------|-----------------------|------------|-------|
| B2.T1 | ASR (Clean) | "Transcribe this audio clip" | **Phonological Loop** | **Automatic Access Rule**: Transcribing speech is the primary function of the Loop. | 9/10 | |
| B2.T1 | ASR (Noisy) | "Transcribe this audio clip (in noisy environment)" | **Central Executive** | **Inhibition Rule**: Suppressing background noise to attend to speech. | 9/10 | The "Noisy" condition shifts this from PL to CE. |
| B2.T2 | Speech QA | "Based on the lecture, what year was the treaty signed?" | **Central Executive** | **Task Set Rule**: Holding a question in mind while searching audio content. | 8/10 | |
| B2.T3 | Speech Instruct. | "Please summarize the key points from this audio" | **Central Executive** | **Task Set Rule**: "Follow these instructions" creates a procedural program. | 10/10 | Core definition of CE function. |
| B2.T4 | Audio QA | "What is the weather like in this audio?" | **Central Executive** | **Task Set Rule**: General reasoning about audio. | 8/10 | |
| B2.T5 | Audio Captioning | "Describe what is happening in this audio" | **Episodic Buffer** | **Binding Rule**: Translating auditory events into a verbal narrative (Cross-modal). | 8/10 | |
| B2.T6 | Emotion Recog. | "Is the speaker happy, sad, angry, or neutral?" | **Episodic Buffer** | **Binding Rule**: Prosody + Context. | 7/10 | |
| B2.T7 | Accent Recog. | "What is the speaker's accent: American, British, Australian?" | **Phonological Loop** | **Phonological Store**: Matching nuance to stored phonological templates. | 8/10 | |
| B2.T8 | Gender Recog. | "Is the speaker male or female?" | **Sensory / Pre-Cog** | **Threshold Rule**: Pitch/Timbre. | 9/10 | |

---

## Benchmark 3 (B3): MMAU-Pro

| Task ID | Task Name | Task Example | Baddeley Component | Primary Decision Rule | Confidence | Notes |
|---------|-----------|--------------|--------------------|-----------------------|------------|-------|
| B3.T1 | Harmony | "Identify the chords in the main guitar riff starting the song" | **Phonological Loop** | **No-Chaining Rule**: Tracking simultaneity (chords) vs. sequence. | 7/10 | Music often uses the Loop (or a musical analogue). |
| B3.T2 | Melody | "What is the selling point of the guitar solo around 2:45?" | **Phonological Loop** | **No-Chaining Rule**: Serial order of pitch (The "Tune"). | 8/10 | |
| B3.T3 | Rhythm/Tempo | "How are the accents placed in this 8th-note hi-hat pattern?" | **Central Executive** | **Task Set Rule**: Monitoring periodicity and beat structure. | 7/10 | Rhythm often involves motor planning (CE/Dorsal). |
| B3.T4 | Spatial Sound | "Which instruments are most prominent on the left side of the mix?" | **Sketchpad** | **Spatial Rule**: Localizing sources ("Left/Right"). | 10/10 | Classic Visuo-Spatial Sketchpad (Spatial sub-system). |
| B3.T5 | Speaker ID | "How many total voices are singing?" | **Central Executive** | **Inhibition Rule**: Segregating voices in a mix. | 8/10 | |
| B3.T12 | Music Emotion | "What does the bamboo flute express?" | **Episodic Buffer** | **Binding Rule**: Integrated interpretation. | 8/10 | |
| B3.T15 | Material ID | "If cubes made of different materials are thrown on the ground, which indicates the first and third material?" | **Sensory / Pre-Cog** | **Threshold Rule**: Spectral signature (Wood vs. Metal). | 9/10 | |
| B3.T18 | Scene Reasoning | "What equipment will one carry while traveling in this weather?" | **Episodic Buffer** | **Binding Rule**: Inferring context ("Travel") from sound ("Car"). | 8/10 | |
| B3.T22 | Temporal Reason. | "At what time is the cooker whistle blown?" | **Central Executive** | **Task Set Rule**: "At what time did X happen?" requires sequencing. | 9/10 | |
| B3.T25 | Prosody | "Which film is the speaker referring to?" | **Phonological Loop** | **Phonological Store**: Intonation contour analysis. | 8/10 | |
| B3.T29 | Turn-Taking | "What is the name of the person who spoke second?" | **Central Executive** | **Inhibition Rule**: Tracking speaker switches ("Who spoke 2nd?"). | 9/10 | |
| B3.T32 | Counting | "If you take 200 million away, how much remains?" | **Central Executive** | **Task Set Rule**: Holding a count while monitoring input. | 10/10 | Classic Working Memory load task. |
| B3.T34 | Causal Scenario | "What role does the first speaker assume?" | **Central Executive** | **Task Set Rule**: Inferring cause-and-effect chains. | 8/10 | |
| B3.T36 | World Knowledge | "What is the likely color of the food coloring?" | **Episodic Buffer** | **Closure Rule**: Linking sound to LTM knowledge. | 9/10 | |

---

## Benchmark 4 (B4): MMAR

| Task ID | Task Name | Task Example | Baddeley Component | Primary Decision Rule | Confidence | Notes |
|---------|-----------|--------------|--------------------|-----------------------|------------|-------|
| B4.T1 | Acoustic Quality | "During which attempt is the extended length of the metal ruler longest?" | **Sensory / Pre-Cog** | **Threshold Rule**: Analyzing raw signal properties. | 9/10 | |
| B4.T2 | Anomaly Det. | "Is the scream in the audio from the music?" | **Central Executive** | **Inhibition Rule**: Detecting deviations from a pattern (Oddball). | 8/10 | Requires maintaining a "standard" and flagging deviations. |
| B4.T3 | Audio Difference | "What type of keyboard made the first sound?" | **Sensory / Loop** | **Threshold Rule**: Fine discrimination. | 8/10 | |
| B4.T4 | Spatial Analysis | "Is the boat approaching or moving away?" | **Sketchpad** | **Spatial Rule**: Localization / Motion. | 10/10 | |
| B4.T5 | Temporal Analysis | "Where is the sports game being watched?" | **Central Executive** | **Task Set Rule**: Sequencing events. | 9/10 | |
| B4.T7 | Counting/Stats | "Into how many pieces is the potato cut?" | **Central Executive** | **Task Set Rule**: Accumulating a count. | 10/10 | |
| B4.T10 | Content Analysis | "What is Gray's mother's name?" | **Phonological Loop** | **Automatic Access Rule**: Processing verbal content. | 9/10 | |
| B4.T14 | Imagination | "What would he have seen if he had arrived earlier?" | **Episodic Buffer** | **Binding Maintenance**: "Counterfactual" reasoning requires holding a hypothetical model. | 8/10 | |
| B4.T16 | Prof. Knowledge | "What is the relationship between the composers of the three musical pieces?" | **Episodic Buffer** | **Closure Rule**: Accessing deep LTM expertise. | 9/10 | |