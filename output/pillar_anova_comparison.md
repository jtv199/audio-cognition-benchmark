# Comparative Analysis of Cognitive Taxonomies for AI

**Generated**: January 4, 2026
**Purpose**: Determine which cognitive framework best predicts the performance of Large Audio Models (LAMs) on the MMAU-Pro benchmark.

## Methodology
We analyzed performance scores from **26 SOTA Audio Models** (Gemini, GPT-4o, etc.) across 12 task categories (312 total data points). We grouped these tasks according to different cognitive taxonomies and ran **One-Way ANOVA** to calculate:
1.  **F-Statistic**: The predictive power of the grouping (Signal-to-Noise Ratio).
2.  **Deviance (RSS)**: The unexplained error (lower is better).
3.  **AIC (Akaike Information Criterion)**: A measure that balances accuracy (Deviance) with complexity (number of parameters, $k$).

---

## The Leaderboard (Sorted by AIC)

| Rank | Taxonomy | $k$ (Params) | F-Stat | Deviance | AIC | Interpretation |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **1** | **MMAU_Original** | 12 | 9.75 | **66,389** | **1698.4** | **Most Accurate.** The 12 granular categories (Music, Speech, Spatial...) describe the data best, justifying their complexity. |
| **2** | **Baddeley (P6)** | 6 | 14.02 | 73,337 | 1717.5 | **Best Cognitive Theory.** The 6-component Working Memory model is the best scientific framework for explaining AI variance. See `output/decision_rule.md` for definitions of components like "Executive-Inhibition". |
| **3** | **Neuroscience (P3)** | **2** | **52.03** | 77,179 | 1725.4 | **Most Efficient.** A simple binary rule ("Ventral vs. Dorsal") explains nearly as much as complex models. Highest F-Stat. |
| **4** | **Katz (P4)** | 4 | 18.64 | 76,281 | 1725.7 | Clinical model performs similarly to Neuro but with more parameters. |
| **5** | **Atkinson (P5)** | 2 | 23.65 | 83,744 | 1750.9 | Strong predictor, but less precise than Neuro. |
| **6** | **CASA (P2)** | 2 | 5.94 | 88,438 | 1767.9 | Weak predictor. AI struggles with "Schema" but the split isn't clean. |
| **7** | **Ecological (P1)** | 2 | 2.16 | 89,511 | 1771.6 | **No Predictive Power.** Physics vs. Semantics is irrelevant to AI performance. |

---

## Key Insights

### 1. Complexity is Justified
The **MMAU_Original** classification (12 categories) wins on AIC. This means the specific differences between "Speech-Music" and "Speech-Sound" are real and meaningful. We cannot fully "compress" AI behavior into just 2-3 cognitive buckets without losing information.

### 2. Baddeley is the Best "Theory"
Among the scientific theories, **Baddeley's Working Memory** (AIC 1717.5) beats the others. Its breakdown of "Executive-Logic" vs. "Executive-Inhibition" captures nuances that the binary "Ventral/Dorsal" split misses.
*   **Reference:** See `output/decision_rule.md` -> **"The Inhibition Rule"** vs **"The Task Set Rule"**.

### 3. Neuroscience is the "80/20" Rule
**P3_Neuro** has the highest F-Statistic (**52.03**). If you can only ask *one* question about a task to predict if an AI will fail, ask: **"Is it a Dorsal Stream (Where/How) task?"**
*   **Ventral (What):** 46.7% Mean Score
*   **Dorsal (Where):** 33.8% Mean Score

### 4. The "Passive vs. Active" Gap
**P5_Atkinson** (Sensory vs. Control) shows a clear split. AI models act like **Passive Sensory Registers** (high performance) that lack **Active Control Processes** (low performance).

---

## Statistical Details
*   **N**: 312 data points (26 models x 12 categories).
*   **AIC Formula**: $AIC = N \ln(RSS/N) + 2k$.
*   **Significance**: All top 5 models have $p < 0.0001$.

## References
For detailed definitions of the cognitive rules governing these categories (e.g., "Inhibition Rule," "No-Chaining Rule"), see **`output/decision_rule.md`**.