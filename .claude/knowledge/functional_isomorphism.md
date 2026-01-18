# Functional Isomorphism: The Core Benchmark Hypothesis

**Date Saved:** January 8, 2026
**Context:** Defining the scientific justification for applying Human Cognitive Models (Baddeley, ASA) to Artificial Intelligence (MM-LLMs).

## The Core Concept
**Functional Isomorphism** posits that it does not matter if the underlying hardware differs (Biological Neurons vs. Silicon Transistors). What matters for benchmarking is if the **functional boundaries** and **error patterns** are equivalent.

We are not testing *if* the AI is "human." We are testing if the AI's processing pipeline (Encoder $\to$ Transformer) exhibits the same **"Lossy Compression Artifacts"** as the human pipeline (Cochlea $\to$ Cortex).

## The Falsification Criteria
The validity of using human cognitive models to benchmark AI is falsifiable based on the **convergence of error patterns**.

### Scenario A: Valid Application (Convergence)
*   **Observation:** The AI fails at tasks in the same conditions humans do.
    *   *Example:* AI fails to detect gaps <5ms (Temporal Resolution).
    *   *Example:* AI "hallucinates" missing sounds when masked by loud noise (Phonemic Restoration).
*   **Conclusion:** The AI and Human systems share a similar "Sensory Horizon" and "Top-Down Repair" strategy. Human models (Baddeley, ASA) are **VALID** tools for categorization.

### Scenario B: Invalid Application (Divergence)
*   **Observation:** The AI fails randomly or exhibits "Alien" capabilities.
    *   *Example:* AI has "Super-Hearing" (detects 0.1ms gaps) but fails simple logic.
    *   *Example:* AI fails to "repair" masked speech even when context makes it obvious.
*   **Conclusion:** The AI processes information fundamentally differently (e.g., purely bottom-up). Human models are an **INVALID** category error.

## The "Resolution Bottleneck" (AI Specifics)
*   **Human Bottleneck:** Biological decay (Sensory Memory) and Neural firing rates (~5ms GIN threshold).
*   **AI Bottleneck:**
    *   **The Audio Encoder (The "Ear"):** Converts continuous waves into discrete tokens (often 20-40ms frames).
    *   **The Loss:** Information smaller than the frame size is "smeared" (averaged).
    *   **The Consequence:** An AI may be "Dorsal Blind" not because it lacks logic, but because its "Ears" (Encoder) physically cannot see the temporal fine structure.

## Key Research Question
"Does the AI use **Schema (Context)** to overwrite **Sensory Loss** in the same way a human uses **Top-Down Processing** to fill in gaps?"
