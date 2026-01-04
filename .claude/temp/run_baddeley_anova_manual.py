import statistics

# 1. Data Ingestion: Parse the Markdown Table manually
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
                    "Score": score,
                    "Component": group
                })
            except ValueError:
                continue

# Group scores by component
groups = {}
for item in data:
    comp = item["Component"]
    if comp not in groups:
        groups[comp] = []
    groups[comp].append(item["Score"])

# 2. Descriptive Statistics & Visualization
print("\n--- Descriptive Statistics by Component ---")
print(f"{ 'Component':<25} | { 'Mean':<6} | { 'Min':<5} | { 'Max':<5} | { 'n':<3}")
print("-" * 60)

for comp, scores in groups.items():
    mean = statistics.mean(scores)
    min_val = min(scores)
    max_val = max(scores)
    n = len(scores)
    print(f"{comp:<25} | {mean:6.1f} | {min_val:5.1f} | {max_val:5.1f} | {n:3}")

# 3. Simple ANOVA Calculation (Manual F-Statistic)
# F = (Between-Group Variance) / (Within-Group Variance)

all_scores = [s for sublist in groups.values() for s in sublist]
grand_mean = statistics.mean(all_scores)

# Calculate SS_between (Sum of Squares Between)
ss_between = 0
for comp, scores in groups.items():
    n = len(scores)
    mean = statistics.mean(scores)
    ss_between += n * (mean - grand_mean)**2

# Calculate SS_within (Sum of Squares Within)
ss_within = 0
for comp, scores in groups.items():
    mean = statistics.mean(scores)
    for score in scores:
        ss_within += (score - mean)**2

# Degrees of freedom
k = len(groups) # Number of groups
N = len(all_scores) # Total number of samples
df_between = k - 1
df_within = N - k

# Mean Squares
ms_between = ss_between / df_between
ms_within = ss_within / df_within

# F-Statistic
f_stat = ms_between / ms_within

print("\n--- One-Way ANOVA Results (Manual Calculation) ---")
print(f"Grand Mean: {grand_mean:.2f}")
print(f"SS Between: {ss_between:.2f} (df={df_between})")
print(f"SS Within:  {ss_within:.2f} (df={df_within})")
print(f"F-Statistic: {f_stat:.4f}")

# Critical Value approximation for alpha=0.05 (roughly > 2.5 for these dfs)
print("Note: An F-value > 2.6 is typically significant at p<0.05 for these sample sizes.")
if f_stat > 2.6:
    print("Result: SIGNIFICANT. The Baddeley Component likely predicts the AI's score.")
else:
    print("Result: NOT SIGNIFICANT.")

# 4. Sorted Means
print("\n--- Ranked Components (Best to Worst) ---")
sorted_groups = sorted(groups.items(), key=lambda x: statistics.mean(x[1]), reverse=True)
for comp, scores in sorted_groups:
    print(f"{comp}: {statistics.mean(scores):.1f}%")
