import csv
import statistics
import math

def log_beta(x, y):
    return math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y)

def fdtr(df1, df2, f):
    if f <= 0: return 1.0
    x = df2 / (df2 + df1 * f)
    if x <= 0 or x >= 1: return 0.0 # Boundary check
    
    a = df2 / 2.0
    b = df1 / 2.0
    
    # Simple Simpson's rule for Beta(x; a, b)
    n = 20 # Low precision for speed/stability
    h = x / n
    s = 0
    
    def f_beta(t):
        if t <= 0 or t >= 1: return 0
        try:
            return (t**(a-1)) * ((1-t)**(b-1))
        except:
            return 0
        
    for i in range(1, n):
        t = i * h
        weight = 4 if i % 2 == 1 else 2
        s += weight * f_beta(t)
        
    s += f_beta(x)
    
    integral = (h/3) * s
    try:
        beta_val = math.exp(log_beta(a, b))
    except:
        return 0.0
        
    return integral / beta_val

def calculate_anova(groups):
    all_scores = [s for sublist in groups.values() for s in sublist]
    if not all_scores: return 0.0, 0, 0, 0.0, 0
    
    grand_mean = statistics.mean(all_scores)
    N = len(all_scores)
    k = len(groups)
    
    if k < 2: return 0.0, 0, 0, 0.0, k

    ss_between = 0
    for scores in groups.values():
        n_i = len(scores)
        mean_i = statistics.mean(scores)
        ss_between += n_i * (mean_i - grand_mean)**2

    ss_within = 0
    for scores in groups.values():
        mean_i = statistics.mean(scores)
        for s in scores:
            ss_within += (s - mean_i)**2

    df_between = k - 1
    df_within = N - k
    
    if df_between == 0 or df_within == 0: return 0.0, df_between, df_within, ss_within, k

    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    
    if ms_within == 0: return 0.0, df_between, df_within, ss_within, k

    f_stat = ms_between / ms_within
    return f_stat, df_between, df_within, ss_within, k

# --- Main Analysis ---
csv_file = "output/data/mmau_pro_pillars_scores.csv"
taxonomies = ["Baddeley", "P1_Eco", "P2_CASA", "P3_Neuro", "P4_Katz", "P5_Atkinson"]
results = []

data = []
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            row['Score'] = float(row['Score'])
            data.append(row)
        except: pass

print("\n--- Comparative ANOVA Results ---")
print(f"{'Taxonomy':<12} | {'k':<3} | {'F-Stat':<8} | {'df':<8} | {'Deviance':<9} | {'P-Value':<8} | {'Power'}")
print("-" * 80)

for tax in taxonomies:
    groups = {}
    for row in data:
        label = row.get(tax)
        if label:
            if label not in groups:
                groups[label] = []
            groups[label].append(row['Score'])
    
    if not groups:
        continue
        
    f_stat, df_b, df_w, deviance, k = calculate_anova(groups)
    
    # P-Value Calc
    try:
        if f_stat > 100: p_val = 0.0 # Extreme F
        else: p_val = fdtr(df_b, df_w, f_stat)
    except:
        p_val = 1.0 # Fail safe
        
    results.append((tax, k, f_stat, df_b, df_w, deviance, p_val))

results.sort(key=lambda x: x[2], reverse=True)

for res in results:
    tax, k, f_stat, df_b, df_w, deviance, p_val = res
    power = "High" if f_stat > 10 else "Medium" if f_stat > 5 else "Low"
    df_str = f"{df_b},{df_w}"
    
    # Handle p-value display
    if p_val < 1e-4: p_str = "<1e-4"
    else: p_str = f"{p_val:.4f}"
    
    print(f"{tax:<12} | {k:<3} | {f_stat:<8.4f} | {df_str:<8} | {deviance:<9.1f} | {p_str:<8} | {power}")

print("\n--- Notes ---")
print("1. Deviance: Residual Sum of Squares (RSS). Lower implies better fit.")
print("2. P-Value: Calculated via manual Regularized Beta Function integration.")
