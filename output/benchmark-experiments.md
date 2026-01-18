# Benchmark Experimental Protocols: The "Cognitive Stress Test" Suite

**Date**: January 8, 2026
**Purpose**: Define the exact operational protocols for the Pilot Study. These experiments are adapted from classic human cognitive psychology to mathematically isolate specific AI processing deficits.

---

## Experiment 1: The "Executive Load" Test
**Target:** Central Executive Capacity (Baddeley) & Cognitive Spare Capacity (Mishra).
**Human Analogue:** Baddeley & Hitch (1974) Dual-Task; Robbins et al. (1996) Chess Interference.

### The Logic
We test if the model's "reasoning" resources are shared with its "listening" resources. If they are shared, increasing the reasoning load should degrade listening performance (or vice versa).

### Protocol
*   **Stimulus:** 30-second audio clips of dense speech (e.g., news report, technical lecture) with varying levels of background "Babble Noise" (SNR +10dB to -5dB).
*   **Task A (Baseline - Perception Only):**
    *   *Prompt:* "Transcribe this audio verbatim."
    *   *Metric:* Word Error Rate (WER).
*   **Task B (Stress - Perception + Executive Load):**
    *   *Prompt:* "Transcribe this audio verbatim **AND** maintain a running count of how many times the speaker uses an adjective. Output the transcription first, then the count."
    *   *Metric:* WER + Count Accuracy ($Acc_{Count}$).

### The Hypothesis (The Delta)
*   **Human-Like Failure:** As Noise increases, $Acc_{Count}$ collapses while $Acc_{Trans}$ is preserved (prioritizing the primary stream).
*   **AI Failure (Executive Collapse):** Both $Acc_{Trans}$ and $Acc_{Count}$ collapse significantly more in Task B than Task A, proving that "Reasoning" steals resources from "Hearing."

---

## Experiment 2: The "Sensory Buffer" Test
**Target:** Echoic Memory Capacity (Atkinson-Shiffrin).
**Human Analogue:** Sperling (1960) / Moray et al. (1965) Partial Report.

### The Logic
Human "Echoic Memory" is a high-capacity, rapidly decaying buffer (2-4s). We test if the AI has access to a similar "raw audio" buffer or if it is bottlenecked by the Tokenizer immediately.

### Protocol
*   **Stimulus:** A rapid sequence of 10 random spoken digits (e.g., "5-9-2-1-8-3-7-4-6-0") presented at 2 digits/sec.
*   **Condition A (Whole Report):**
    *   *Prompt (Pre-Audio):* "Listen to these numbers. I will ask you to recall all of them."
    *   *Prompt (Post-Audio):* "Recall all the numbers."
*   **Condition B (Partial Report):**
    *   *Prompt (Pre-Audio):* "Listen to these numbers."
    *   *Prompt (Post-Audio - Immediate):* "Recall only the 3 numbers that appeared in the **middle** of the sequence."

### The Hypothesis (The Delta)
*   **If AI has a Sensory Buffer:** Accuracy in **Partial Report** (extrapolated) should be significantly higher than **Whole Report**. (e.g., getting 3/3 in partial implies it "saw" all 10, whereas it might only recall 5/10 in whole).
*   **If AI is Bottlenecked:** Accuracy will be identical or worse in Partial Report, proving no "pre-attentive" high-capacity trace exists.

---

## Experiment 3: The "Schema Repair" Test
**Target:** Top-Down Restoration (Auditory Scene Analysis).
**Human Analogue:** Miller & Licklider (1950) Continuity Illusion; Warren (1970) Phonemic Restoration.

### The Logic
Humans hallucinate missing sounds if they are masked by noise (Restoration), but notice the gap if it is silence. This tests if the model uses "World Knowledge" (Schema) to override "Sensory Reality."

### Protocol
*   **Stimulus A (Gap = Silence):** A spoken sentence where one word is interrupted by 200ms of silence. "The [SILENCE]eel is on the axle."
*   **Stimulus B (Gap = Noise):** The same sentence, but the gap is filled with 200ms of white noise. "The [NOISE]eel is on the axle."
*   **Task:** "Transcribe the sentence. Do not guess; if a sound is missing, write [MISSING]."

### The Hypothesis (The Delta)
*   **Human-Like Restoration:**
    *   **Stimulus A:** Model reports "[MISSING]" or "The eel..." (Correct sensory detection).
    *   **Stimulus B:** Model reports "The **wheel**..." (Hallucination/Restoration).
*   **The Delta:** The *difference* in "hallucination rate" between Noise and Silence is the metric of Top-Down Repair. If the model hallucinates "wheel" in *both*, it is ignoring sensory input (Pure Hallucination). If it hallucinates in *neither*, it lacks Top-Down repair (Pure Sensory).

---

## Implementation Plan (Pilot)
1.  **Generate Stimuli:** Use `TTS` (Text-to-Speech) + `ffmpeg` to generate the noisy/gapped audio files programmatically.
2.  **Code the Harness:** Create a Python script `run_pilot.py` to:
    *   Load the models (e.g., Whisper, Qwen-Audio).
    *   Feed the paired stimuli.
    *   Parse the output (Regex for counts, fuzzy matching for transcription).
    *   Calculate the Deltas.
