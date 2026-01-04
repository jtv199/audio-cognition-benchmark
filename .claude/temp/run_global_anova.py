import csv
import math
import statistics

# --- 1. Define Mapping ---
# Maps Table 3 Categories (CSV Columns) to Refined Baddeley Components
# We separate "Executive" into "Logic" (Task Set) and "Inhibition" (Conflict)
CATEGORY_MAP = {
    "Sound": "Sensory",
    "Music": "Phonological Loop",
    "Speech": "Phonological Loop",
    "Sound-Music": "Executive-Inhibition",
    "Speech-Music": "Executive-Inhibition",
    "Speech-Sound": "Executive-Inhibition",
    "Sound-Music-Speech": "Executive-Inhibition",
    "Spatial": "Sketchpad",
    "Voice": "Episodic Buffer", # Paralinguistics usually Buffer
    "Multi-Audio": "Executive-Inhibition", # The critical failure point
    "Open-ended": "Episodic Buffer",
    "IF": "Executive-Logic" # Instruction Following
}

csv_file = "output/mmau_pro_full_performance.csv"

# --- 2. Load Data ---
data_points = [] # List of {'Model': str, 'Component': str, 'Score': float}

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        model_name = row['Models']
        if model_name == "Random Choice": continue # Skip random baseline
        
        for category, component in CATEGORY_MAP.items():
            try:
                score_str = row[category].strip()
                if score_str == "-" or score_str == "": continue
                score = float(score_str)
                
                data_points.append({
                    "Model": model_name,
                    "Component": component,
                    "Score": score
                })
            except ValueError:
                continue

# --- 3. Group Data by Component ---
groups = {}
for dp in data_points:
    comp = dp['Component']
    if comp not in groups:
        groups[comp] = []
    groups[comp].append(dp['Score'])

# --- 4. Descriptive Stats ---
print(f"{ 'Component':<25} | { 'Mean':<6} | { 'StdDev':<6} | { 'n':<4}")
print("-" * 60)

component_means = {}

for comp, scores in groups.items():
    mean = statistics.mean(scores)
    stdev = statistics.stdev(scores) if len(scores) > 1 else 0.0
    component_means[comp] = mean
    print(f"{comp:<25} | {mean:6.2f} | {stdev:6.2f} | {len(scores):<4}")

# --- 5. One-Way ANOVA (Component Effect across All Models) ---
# F = MS_between / MS_within

all_scores = [s for sublist in groups.values() for s in sublist]
grand_mean = statistics.mean(all_scores)
N = len(all_scores)
k = len(groups)

# SS Between
ss_between = 0
for comp, scores in groups.items():
    n_i = len(scores)
    mean_i = statistics.mean(scores)
    ss_between += n_i * (mean_i - grand_mean)**2

# SS Within
ss_within = 0
for comp, scores in groups.items():
    mean_i = statistics.mean(scores)
    for s in scores:
        ss_within += (s - mean_i)**2

df_between = k - 1
df_within = N - k

ms_between = ss_between / df_between
ms_within = ss_within / df_within

f_stat = ms_between / ms_within

# Calculate P-value? (Approximate/Critical Value)
# For df_between=5, df_within=~300, Critical F (alpha=0.01) is approx 3.0
is_significant = f_stat > 3.0

print("\n--- Global ANOVA Results (All Models) ---")
print(f"Number of Models: {len(set(dp['Model'] for dp in data_points))}")
print(f"Total Data Points: {N}")
print(f"F-Statistic: {f_stat:.4f}")
print("Critical F (alpha=0.01) ~ 3.0")
if is_significant:
    print("Result: SIGNIFICANT. The Cognitive Component strongly predicts model failure/success.")
else:
    print("Result: NOT SIGNIFICANT.")

# --- 6. Ranking ---
print("\n--- Cognitive Hierarchy (Easiest to Hardest) ---")
sorted_comps = sorted(component_means.items(), key=lambda x: x[1], reverse=True)
for i, (comp, mean) in enumerate(sorted_comps, 1):
    print(f"{i}. {comp:<25}: {mean:.2f}%")
