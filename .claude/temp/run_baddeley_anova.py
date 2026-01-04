import re
import pandas as pd
import scipy.stats as stats

# 1. Data Ingestion: Parse the Markdown Table
file_path = "output/mmau_pro_baddeley_summary.md"

with open(file_path, "r") as f:
    lines = f.readlines()

data = []

for line in lines:
    if "B3.T" in line:
        parts = line.split("|")
        if len(parts) > 5:
            # Task ID is usually in parts[1]
            task_id = parts[1].replace("*", "").strip()
            task_name = parts[2].strip()
            # Score is in parts[4], usually like " 64.9% "
            score_str = parts[4].replace("*", "").replace("%", "").strip()
            # Component is in parts[5]
            component_str = parts[5].replace("*", "").strip()
            
            try:
                score = float(score_str)
                
                # Simplify Component Names for Grouping
                if "Central Executive" in component_str:
                    group = "Central Executive"
                elif "Phonological Loop" in component_str:
                    group = "Phonological Loop"
                elif "Episodic Buffer" in component_str:
                    group = "Episodic Buffer"
                elif "Sensory" in component_str:
                    group = "Sensory/Pre-Cog"
                elif "Sketchpad" in component_str:
                    group = "Visuo-Spatial Sketchpad"
                else:
                    group = "Other"

                data.append({
                    "Task": task_id,
                    "Name": task_name,
                    "Score": score,
                    "Component": group
                })
            except ValueError:
                continue

df = pd.DataFrame(data)

# 2. Descriptive Statistics
print("\n--- Descriptive Statistics by Component ---")
print(df.groupby("Component")["Score"].describe())

# 3. ANOVA Test
# We need to create a list of score arrays for the ANOVA function
groups = df.groupby("Component")["Score"].apply(list)
f_val, p_val = stats.f_oneway(*groups)

print("\n--- One-Way ANOVA Results ---")
print(f"F-Statistic: {f_val:.4f}")
print(f"P-Value: {p_val:.4e}")

if p_val < 0.05:
    print("Result: SIGNIFICANT. The Baddeley Component significantly predicts the AI's score.")
else:
    print("Result: NOT SIGNIFICANT. The scores are not significantly different across components.")

# 4. Means Ranking
print("\n--- Mean Scores Ranking ---")
print(df.groupby("Component")["Score"].mean().sort_values())

# 5. Visualization (Text)
print("\n--- Distribution Visualization (Text) ---")
for name, group in df.groupby("Component"):
    scores = sorted(group["Score"].tolist())
    mean = sum(scores) / len(scores)
    print(f"{name:25} | Mean: {mean:.1f}% | Min: {scores[0]:.1f} | Max: {scores[-1]:.1f} | n={len(scores)}")
