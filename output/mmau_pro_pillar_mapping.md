# Mapping MMAU-Pro Categories to Cognitive Pillars

**Generated**: January 4, 2026
**Purpose**: Map the 12 high-level MMAU-Pro categories to the component structures of the 4-Pillar Framework to enable comparative ANOVA testing.

**Reference:** For detailed definitions of the underlying cognitive rules (e.g., "Inhibition Rule," "Task Set Rule"), see **`output/decision_rule.md`**.

---

## 1. Mapping Strategy

We align the MMAU-Pro categories (from Table 3) to the specific sub-components of each theoretical framework.

### Pillar 1: Ecological Psychology (Gaver)
*   **Physics (Event Source):** Focus on the mechanical origin of sound (Impact, Scraping, Solids, Liquids).
*   **Semantics (Meaning):** Focus on the learned association (Speech, Music, Context).

### Pillar 2: CASA (Bregman)
*   **Primitive (Automatic):** Grouping by pitch, timbre, harmony.
*   **Schema (Attention):** Selection, Inhibition, Meaning-driven segregation.

### Pillar 3: Neuroscience (Rauschecker)
*   **Ventral (What):** Object ID, Speech Recog, Melody.
*   **Dorsal (Where/How):** Localization, Motion, Motor Planning (Rhythm), Multi-stream tracking.

### Pillar 4: Clinical Audiology (Katz/Buffalo)
*   **Decoding:** Basic phonemic/acoustic analysis (Clear Speech, Simple Music).
*   **Tolerance-Fading Memory (TFM):** Performance in Noise, Short-term memory load.
*   **Integration:** Binaural/Spatial tasks, Cross-modal binding.
*   **Organization:** Sequencing, Planning, Complex Reasoning.

### Pillar 5: Atkinson-Shiffrin (Memory)
*   **Sensory/STS:** Passive registration and short-term holding (Single modality).
*   **Control:** Active manipulation, Rehearsal, Coding (Multi-modality, Reasoning).

### Pillar 5-Ext: Extended A-S Model (3-Store)
*   **Sensory:** Raw pattern matching (Sound, Music).
*   **LTM-Explicit:** Semantic knowledge retrieval (Speech, Open-Ended).
*   **STM-Control:** Active manipulation and inhibition (Multi-Audio, Spatial, IF).

---

## 2. The Mapping Matrix

| MMAU-Pro Category | Baddeley (Reference) | Pillar 1: Ecological | Pillar 2: CASA | Pillar 3: Neuro | Pillar 4: Katz | Pillar 5: Atkinson | Pillar 5-Ext: A-S Extended |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Sound** | Sensory | Physics | Primitive | Ventral | Decoding | Sensory/STS | Sensory |
| **Music** | Phonological Loop | Physics (Abstract) | Primitive | Ventral | Decoding | Sensory/STS | Sensory |
| **Speech** | Phonological Loop | Semantics | Primitive | Ventral | Decoding | Sensory/STS | LTM-Explicit |
| **Sound-Music** | Ex-Inhibition | Physics | Schema | Dorsal | TFM | Control | STM-Control |
| **Speech-Music** | Ex-Inhibition | Semantics | Schema | Dorsal | TFM | Control | STM-Control |
| **Speech-Sound** | Ex-Inhibition | Semantics | Schema | Dorsal | TFM | Control | STM-Control |
| **Sound-Music-Speech** | Ex-Inhibition | Semantics | Schema | Dorsal | TFM | Control | STM-Control |
| **Spatial** | Sketchpad | Physics | Primitive | Dorsal | Integration | Control | STM-Control |
| **Voice** | Episodic Buffer | Semantics | Primitive | Ventral | Decoding | Sensory/STS | Sensory |
| **Multi-Audio** | Ex-Inhibition | Semantics | Schema | Dorsal | TFM | Control | STM-Control |
| **Open-ended** | Episodic Buffer | Semantics | Schema | Ventral | Organization | Control | LTM-Explicit |
| **IF (Instruction)** | Ex-Logic | Semantics | Schema | Ventral | Organization | Control | STM-Control |

---

## 3. Rationale for Critical Mappings

### Why "Multi-Audio" is Dorsal (Neuro)?
*   **Reasoning:** Tracking multiple streams requires spatial separation (even if virtual) and rapid attentional switching, which engages the Parietal (Dorsal) network.
*   **Baddeley Equivalent:** Central Executive (**Inhibition Rule** - see `decision_rule.md`).

### Why "Spatial" is Integration (Katz)?
*   **Reasoning:** Katz defines "Integration" as the ability to synthesize information from both ears (Binaural) or across modalities. Spatial hearing is the primary binaural integration task.
*   **Baddeley Equivalent:** Visuo-Spatial Sketchpad (**Spatial Rule** - see `decision_rule.md`).

### Why "Mixed Modalities" are TFM (Katz)?
*   **Reasoning:** "Tolerance-Fading Memory" specifically covers "Speech-in-Noise" and performance under competing signal conditions. Any mix (Speech+Music) is a TFM stress test.
*   **Baddeley Equivalent:** Central Executive (**Inhibition Rule** - see `decision_rule.md`).

### Why "Music" is Physics (Ecological)?
*   **Reasoning:** While music has meaning, in Gaver's taxonomy, it is often treated as "Abstract" or "Symbolic" rather than strictly "Event-based," but it aligns closer to Physics (harmonic structure) than pure Linguistic Semantics. However, for this binary classification, we treat it as structured Physics unless lyrics are involved.