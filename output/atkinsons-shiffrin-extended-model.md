# Atkinson-Shiffrin Extended Model (1968 + Modern Extensions)

**Generated**: January 4, 2026
**Purpose**: Define the components of the extended Modal Model of Memory, clarifying the distinction between Structural Features (Passive) and Control Processes (Active) as used in the AI Benchmark ANOVA.

---

## 1. Overview of the Model

The Atkinson-Shiffrin model (1968) proposes that memory consists of three structural stores: **Sensory Memory**, **Short-Term Memory (STM)**, and **Long-Term Memory (LTM)**. Information flows from the environment through these stores, governed by **Control Processes**.

Modern extensions (e.g., Camina & Güell, 2017) elaborate on the sub-types within Sensory and Long-Term memory.

---

## 2. Structural Components (Passive Stores)

### A. Sensory Memory (The Registers)
**Function:** High-capacity, rapid-decay buffer that holds raw sensory input in its veridical form before attention selects it.
*   **Echoic Memory (Auditory):**
    *   **Duration:** 2–4 seconds.
    *   **Relevance:** Critical for integrating speech across time. If an AI has a short "context window" for raw audio tokens, it fails here.
*   **Iconic Memory (Visual):**
    *   **Duration:** ~200–500 ms.
    *   **Note:** The diagram labeled this "Ionic," which is a typo.
*   **Haptic Memory (Touch):**
    *   **Duration:** ~2 seconds.

### B. Short-Term Memory (STM)
**Function:** Limited-capacity store for holding information currently in conscious awareness.
*   **Duration:** 15–30 seconds (without rehearsal).
*   **Modern View:** Replaced or expanded by Baddeley's **Working Memory** (which adds the Central Executive).
*   **AI Equivalent:** The Context Window (post-tokenization) or the immediate "scratchpad" of activations.

### C. Long-Term Memory (LTM)
**Function:** Permanent, effectively infinite storage.
*   **Explicit (Declarative) Memory:** Conscious recall.
    *   **Episodic:** Events, personal experiences ("I heard a dog bark at 2:00").
    *   **Semantic:** Facts, concepts ("A dog is an animal").
*   **Implicit (Non-Declarative) Memory:** Unconscious influence.
    *   **Procedural:** Skills, habits ("How to ride a bike," or for AI, "How to parse syntax").
    *   **Priming:** Recent exposure facilitating processing.

---

## 3. Control Processes (Active Manipulation)

The key innovation of the 1968 model was the **Control Process**. These are transient, voluntary strategies used to maintain information in STM or transfer it to LTM.

*   **Rehearsal:** Repetition to prevent decay (e.g., "Maintenace Rehearsal").
*   **Coding:** Transforming information (e.g., converting "Visual Text" to "Phonological Sound").
*   **Retrieval Strategies:** Active search of LTM.

---

## 4. Relevance to AI Benchmarking (ANOVA Results)

Our statistical analysis (ANOVA F=23.6) found a massive performance gap between:

1.  **Sensory/STS Tasks (Passive):**
    *   *Examples:* Identifying a sound, recognizing a melody.
    *   *Mechanism:* Input -> Sensory -> Pattern Match.
    *   *AI Performance:* **High (~48%)**.

2.  **Control Tasks (Active):**
    *   *Examples:* Multi-audio tracking, Spatial manipulation, "Count the speakers."
    *   *Mechanism:* Requires **Rehearsal** (keeping a count) or **Coding** (transforming spatial cues).
    *   *AI Performance:* **Low (~34%)**.

**Conclusion:** Current Large Audio Models function like a **Passive Sensory Register** attached to a **Semantic LTM**. They lack the **Active Control Processes** (Rehearsal loop) required for complex tasks.
