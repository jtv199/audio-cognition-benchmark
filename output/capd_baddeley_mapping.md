# Mapping CAPD Tasks to Baddeley's Working Memory Model

This document classifies standard Central Auditory Processing Disorder (CAPD) tasks according to the primary Baddeley Working Memory component they stress, using the specific "Decision Rules" defined in `decision_rule.md`.

---

## 1. Central Executive Tasks ("The Boss")

**Primary Rule Stress:** The **Inhibition Rule** (blocking distractors) and the **Task Set Rule** (maintaining a procedural program).

| CAPD Task | Description | Why it fits (Rule Application) |
| :--- | :--- | :--- |
| **Speech-in-Noise (SIN)** | Identify words in background noise. | **Inhibition Rule:** The "decision" is what to *ignore*. The CE must actively suppress the noise (distractor) to focus on the signal. Failure looks like "hallucinating" words from the noise. |
| **Auditory Figure-Ground** | Similar to SIN; picking a voice out of a crowd. | **Selective Attention:** Requires the "CEO" to direct the resources of the Phonological Loop to one specific stream. |
| **Competing Sentences** | Listen to both ears, repeat only one. | **Inhibition Rule:** Extreme stress test. You hear "The dog ran" (Left) and "The cat slept" (Right). You must *inhibit* the Right ear entirely. |
| **Pitch Pattern Sequence** | "High-High-Low" labeling. | **Task Set Rule:** You aren't just hearing; you are running a program: "If High, say High. If Low, say Low." This translation requires Executive control. |

---

## 2. Phonological Loop Tasks ("The Recorder")

**Primary Rule Stress:** The **2-Second Decay Rule** (time limit) and the **No-Chaining Rule** (order via gradient).

| CAPD Task | Description | Why it fits (Rule Application) |
| :--- | :--- | :--- |
| **Dichotic Digits** | Hear "5, 9" (Left) and "1, 4" (Right). Repeat all 4. | **Capacity Rule:** No inhibition needed; you repeat everything. The bottleneck is holding 4 distinct acoustic items before they decay (2-second limit). |
| **TAPS Number Memory** | Repeat digit strings (e.g., "7-2-9-5"). | **No-Chaining Rule:** Tests the "Primacy Gradient." If a patient swaps digits ("7-9-2-5"), it's a normal Loop error. If they forget one and the rest vanish, it's a Chaining failure. |
| **Random Gap Detection** | Detecting tiny silence gaps in noise. | **Sensory Resolution:** Technically pre-Loop, but relies on the high-resolution "tape recording" aspect of the Phonological Store to detect discontinuities. |

---

## 3. Episodic Buffer Tasks ("The Integrator")

**Primary Rule Stress:** The **Binding Maintenance Rule** (holding connections against load) and **Chunking**.

| CAPD Task | Description | Why it fits (Rule Application) |
| :--- | :--- | :--- |
| **Filtered Words** | Recognize muffled/distorted words. | **Chunking/Closure:** The input is incomplete ("_at"). The Buffer must access Long-Term Memory to "fill in the gap" ("Cat") based on context. |
| **Time-Compressed Speech** | Speech sped up (e.g., 2x speed). | **Processing Speed + Closure:** The acoustic signal is too fast for the Loop's normal rehearsal; the Buffer must synthesize the meaning directly from the rapid fragments. |
| **TAPS Sentence Memory** | Repeat full sentences. | **Chunking Rule:** "The dog ran fast" is 4 words but 1 Chunk. Success depends on using Grammar (LTM) to compress the size, not just raw Loop capacity. |

---

## 4. Sensory / Pre-Cognitive ("The Input")

**Primary Rule Stress:** **Threshold Detection** (no memory load).

| CAPD Task | Description | Why it fits (Rule Application) |
| :--- | :--- | :--- |
| **Gaps In Noise (GIN)** | Detect silence gap (e.g., 5ms) in white noise. | **Temporal Resolution:** A hardware test of the ear/cortex connection. No "decision" other than "Did it happen?" |
| **Masking Level Difference** | Detect tone in noise with phase inversion. | **Binaural Interaction:** Brainstem physics. Occurs before the signal reaches the "Workspace" of working memory. |

---

## Summary for AI Benchmarking

*   **To Test the Loop:** Use **Dichotic Digits** or **Non-word Repetition**. Look for *transposition errors* (human-like) vs. *hallucination* (model failure).
*   **To Test the Executive:** Use **Competing Sentences**. Can the model *ignore* a clear, semantic signal?
*   **To Test the Buffer:** Use **Filtered Speech**. Can the model use "World Knowledge" to repair a broken audio signal?