# Taxonomy Discrepancy Report: Neuro vs. Cognitive Models

**Generated**: January 4, 2026
**Purpose**: Highlighting discrepancies between the 4-Pillar Framework (Neuro/Ecological/CASA) and the Baddeley Working Memory Model classification of auditory tasks.

---

## 1. The "Foundational" Misclassification (Layer 1)

**Discrepancy:**
*   **Old View (4-Pillar):** Tasks like *Speaker Gender Recognition*, *Age Prediction*, and *Instrument Classification* were classified as **Layer 1 (Foundational)** because they map to the **Ventral "What" Stream** in neuroscience (Pillar 3).
*   **New View (Baddeley):** These tasks are classified as **Sensory / Pre-Cognitive**. They rely on threshold detection and pattern matching (LTM) but place minimal load on Working Memory components (Loop/Executive).

**Implication for Benchmarking:**
*   Current "Foundation" benchmarks (AIR-Bench) heavily weigh these tasks.
*   A model could achieve high scores on "Foundation" tiers purely via statistical pattern matching (Sensory) without possessing any "Working Memory" or "Executive" capability.
*   **Recommendation:** Move these tasks to a separate "Sensory Baseline" category, distinct from true "Foundational Cognition" (which requires at least Phonological Loop involvement).

## 2. The "Speech-in-Noise" Reclassification

**Discrepancy:**
*   **Old View (4-Pillar):** Classified under **Pillar 4 (Clinical)** as "Tolerance-Fading Memory" or "Robustness." Often treated as a harder version of perception.
*   **New View (Baddeley):** Classified as a **Central Executive** task (Inhibition Rule). The primary mechanism is the *active suppression* of the distractor stream, not just the perception of the target.

**Implication for Benchmarking:**
*   "Robustness" tests are actually **Executive Function** tests.
*   Failing a noise task might not mean the model has bad "hearing" (acoustics); it might mean it lacks **Inhibition** (control).
*   **Recommendation:** Rename "Robustness" to "Executive Inhibition" or "Cognitive Control" to reflect the mechanism being tested.

## 3. The "Binding" vs. "Perception" Split

**Discrepancy:**
*   **Old View (4-Pillar):** "Audio Grounding" (finding a sound at a timestamp) and "Scene Classification" were often grouped with Perception (Layer 1).
*   **New View (Baddeley):** These are **Episodic Buffer** tasks (Binding Rule). They require integrating distinct feature codes (Semantic + Temporal, or Visual + Audio) into a unified "Episode."

**Implication for Benchmarking:**
*   These tasks test the "Bridge" between systems.
*   Success requires more than just identifying the sound; it requires **maintaining the link** between the sound and its context (Time/Location).
*   **Recommendation:** Group "Grounding" and "Captioning" under a specific "Multimodal Binding" category.

## 4. The "Modality Gap" in Counting

**Discrepancy:**
*   **Old View (4-Pillar):** Counting tasks (B3.T32, B4.T7) were labeled "Quantitative Reasoning" (Layer 3).
*   **New View (Baddeley):** Counting is a classic **Central Executive** task (Task Set Rule + Maintenance). It requires holding a running total (Loop/Buffer) while processing new input (Sensory).

**Implication for Benchmarking:**
*   Counting is an excellent proxy for **Working Memory Capacity** (The 4-Chunk Rule).
*   It is less about "Math" (reasoning) and more about "Maintenance" (holding state).

---

## Summary of Strategic Shifts

| Task Category | Old Label (4-Pillar) | New Label (Baddeley) | Benchmarking Shift |
| :--- | :--- | :--- | :--- |
| **Gender/Age/Instrument** | Layer 1 (Foundational) | **Sensory (Pre-Cog)** | Lower priority; "Hardware check" only. |
| **Speech-in-Noise** | Robustness / Clinical | **Central Executive** | Primary test for Inhibition/Attention. |
| **Audio Grounding** | Perception | **Episodic Buffer** | Test for Binding Capacity. |
| **Counting Sounds** | Reasoning | **Executive / Maintenance** | Test for State Maintenance (RAM). |
