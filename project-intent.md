# Audio Cognition Benchmark - Project Overview

## Executive Summary

This project develops a **"Cognitive Stress Test" benchmark** for Audio Large Language Models (AudioLLMs). Moving beyond simple accuracy metrics, we utilize **Functional Isomorphism** and **Cognitive Subtraction** to rigorously measure specific processing deficits. By replicating classic human cognitive experiments (Baddeley, Sperling, ELU), we aim to mathematically distinguish between **Sensory Blindness** (Encoder failure) and **Executive Failure** (Reasoning collapse).

**Current Status**: Phase 2 - Experimental Design

**Repository**: https://github.com/jtv199/audio-cognition-benchmark

---

## Project Goals

### Primary Objective
Validate the existence of specific cognitive bottlenecks in Audio AI by implementing **Paired Stress Tests** (Cognitive Subtraction):

1.  **Replicate Human Experimental Protocols**: Adapt classic psychological paradigms (e.g., Sperling's Partial Report, Baddeley's Dual-Task) into computational benchmarks.
2.  **Isolate Component Failures**: Use "Baseline vs. Stress" comparisons to mathematically prove if a failure is due to:
    *   **Sensory Limits** (e.g., Echoic Memory capacity)
    *   **Executive Load** (e.g., Inhibition failure under noise)
    *   **Top-Down Repair** (e.g., Lack of Schema-driven restoration)
3.  **Establish "Functional Isomorphism"**: Demonstrate that valid AI benchmarking requires testing the *process* (error patterns), not just the *output* (transcription accuracy).

### Key Research Question
*"Can we mathematically isolate specific cognitive deficits (Sensory vs. Executive) in Audio AI by replicating the 'performance deltas' found in human experimental psychology?"*

## Methodology: Cognitive Subtraction

We reject static "Taxonomies" in favor of dynamic **Paired Testing**. Every benchmark consists of a **Baseline Task (A)** and a **Stress Task (B)**. The **Delta (B - A)** reveals the specific cognitive cost.

| Target Component | Human Analogue | AI Experiment (The Pair) | The Metric (Delta) |
| :--- | :--- | :--- | :--- |
| **Sensory Trace** | **Sperling (1960)**<br>Partial Report | **A:** "Recall all 10 digits."<br>**B:** "Recall the 3 digits at this specific timestamp." | If $Acc_B \gg Acc_A$, the model has a high-capacity "Sensory Buffer." |
| **Executive Capacity** | **Baddeley (1974)**<br>Dual-Task | **A:** "Transcribe this noisy audio."<br>**B:** "Transcribe AND count the adjectives." | If $Acc_{Trans}$ is stable but $Acc_{Count}$ drops, the model has low "Spare Capacity." |
| **Schema Repair** | **Miller & Licklider (1950)**<br>Continuity Illusion | **A:** "Did the tone stop?" (Gap = Silence)<br>**B:** "Did the tone stop?" (Gap = Noise) | If the model reports "It continued" only in B, it uses Top-Down Repair. |

---