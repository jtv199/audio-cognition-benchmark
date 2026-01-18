# Glossary of Cognitive & AI Terms

**Project:** Audio Cognition Benchmark (MMAU-Pro Analysis)

## Cognitive Models (Human)

### Baddeley's Model of Working Memory (2012)
A multi-component system for temporary storage and manipulation of information.
*   **Phonological Loop:** The "Inner Voice." Stores auditory info (speech, music) for ~2 seconds. Sensitive to "Articulatory Suppression" (repeating words).
*   **Visuo-Spatial Sketchpad:** The "Inner Eye." Stores spatial location and visual imagery.
*   **Central Executive:** The "CEO." Allocates attention, switches tasks, and inhibits distractions.
*   **Episodic Buffer:** The "Binder." Combines sights, sounds, and memories into a coherent story (chunking).

### Atkinson-Shiffrin Model (Multi-Store)
The "Sequential Pipeline" theory of memory.
*   **Sensory Memory:** High-capacity, fleeting snapshot (Echoic Memory lasts ~3-4s).
*   **Short-Term Memory (STM):** Limited capacity (7 +/- 2 items). Requires attention.
*   **Long-Term Memory (LTM):** Unlimited capacity, permanent storage.

### Auditory Scene Analysis (ASA) - Bregman
How the brain separates a chaotic mix of sounds into distinct "Streams" (objects).
*   **Primitive Segregation:** Bottom-up separation based on physics (pitch, location, timing).
*   **Schema-Driven Segregation:** Top-down separation based on knowledge (identifying a specific voice).
*   **Continuity Illusion:** The brain "fills in" gaps in a sound if the gap is masked by noise.

### Processing Depth (Cutler / Massaro)
*   **Bottom-Up:** Processing data from raw sensory input $\to$ meaning (Data-driven).
*   **Top-Down:** Using expectations/context to interpret sensory input (Concept-driven).
*   **Phonemic Restoration:** A Top-Down effect where the brain "hallucinates" a missing sound to make a sentence makes sense.

---

## AI Architecture Terms

### Audio Encoder
The "Sensory Organ" of an MM-LLM. Converts raw audio waveforms into vector embeddings.
*   **Frame/Window:** The time slice the encoder processes (e.g., 20ms).
*   **Resolution Bottleneck:** If a sound event is shorter than the frame (e.g., a 5ms gap), the encoder may average it out, making the AI "physically" deaf to it.

### Tokenization
The process of breaking input (text or audio) into discrete units (tokens) the model can process.
*   **Lossy Compression:** The encoder discards "useless" acoustic details (noise, subtle timing) to focus on "meaningful" features (speech, phonemes).

### Functional Isomorphism
The hypothesis that an AI system can be benchmarked using human criteria if it exhibits similar **functional error patterns** (e.g., failing at the same noise levels), regardless of its different underlying hardware.

### Dorsal vs. Ventral Streams
*   **Ventral Stream ("What"):** Object identification (e.g., "That is a dog"). AI excels here.
*   **Dorsal Stream ("Where/How"):** Spatial tracking and motor action (e.g., "The dog is moving left"). AI often fails here ("Dorsal Blindness").
