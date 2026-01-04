import csv
import statistics

# --- Helper Function for ANOVA ---
def calculate_anova(groups):
    # groups is a dict: { "Component_Name": [score1, score2...] }
    all_scores = [s for sublist in groups.values() for s in sublist]
    grand_mean = statistics.mean(all_scores)
    N = len(all_scores)
    k = len(groups)
    
    if k < 2: return 0.0, 0, 0 # Cannot run ANOVA with 1 group

    # SS Between
    ss_between = 0
    for scores in groups.values():
        n_i = len(scores)
        mean_i = statistics.mean(scores)
        ss_between += n_i * (mean_i - grand_mean)**2

    # SS Within
    ss_within = 0
    for scores in groups.values():
        mean_i = statistics.mean(scores)
        for s in scores:
            ss_within += (s - mean_i)**2

    df_between = k - 1
    df_within = N - k
    
    if df_between == 0 or df_within == 0: return 0.0, df_between, df_within

    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    
    if ms_within == 0: return 0.0, df_between, df_within

    f_stat = ms_between / ms_within
    return f_stat, df_between, df_within

# --- Main Analysis ---
csv_file = "output/data/mmau_pro_pillars_scores.csv"
taxonomies = ["Baddeley", "P1_Eco", "P2_CASA", "P3_Neuro", "P4_Katz", "P5_Atkinson"]
results = []

# Load Data
data = []
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert Score to float
        row['Score'] = float(row['Score'])
        data.append(row)

print("\n--- Comparative ANOVA Results ---")
print(f"{ 'Taxonomy':<15} | { 'F-Stat':<8} | { 'df':<8} | {'Predictive Power'}")
print("-" * 60)

for tax in taxonomies:
    # Group scores by the current taxonomy's labels
    groups = {}
    for row in data:
        label = row[tax]
        if label not in groups:
            groups[label] = []
        groups[label].append(row['Score'])
    
    f_stat, df_b, df_w = calculate_anova(groups)
    results.append((tax, f_stat, df_b, df_w, groups))

# Sort by F-stat desc
results.sort(key=lambda x: x[1], reverse=True)

for tax, f_stat, df_b, df_w, _ in results:
    power = "High" if f_stat > 10 else "Medium" if f_stat > 5 else "Low"
    df_str = f"{df_b},{df_w}"
    print(f"{tax:<15} | {f_stat:<8.4f} | {df_str:<8} | {power}")

print("\n--- Detailed Breakdown of Top Model ---")
best_tax, best_f, best_df_b, best_df_w, best_groups = results[0]
print(f"Winner: {best_tax} (F={best_f:.4f}, df={best_df_b},{best_df_w})")
print(f"{ 'Component':<25} | { 'Mean':<6} | {'n':<4}")
print("-" * 40)

# Sort components by mean score
comp_stats = []
for comp, scores in best_groups.items():
    comp_stats.append((comp, statistics.mean(scores), len(scores)))
comp_stats.sort(key=lambda x: x[1], reverse=True)

for comp, mean, n in comp_stats:
    print(f"{comp:<25} | {mean:6.2f} | {n:<4}")