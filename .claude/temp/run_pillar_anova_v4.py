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
    n = 20 
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

def calculate_stats(groups):
    all_scores = [s for sublist in groups.values() for s in sublist]
    N = len(all_scores)
    k = len(groups) # Parameters (Groups)
    
    if N == 0: return 0, 0, 0, 0, 0, 0

    grand_mean = statistics.mean(all_scores)

    # SS Between & Within
    ss_between = 0
    ss_within = 0 # This is RSS (Residual Sum of Squares)
    
    for scores in groups.values():
        n_i = len(scores)
        if n_i > 0:
            mean_i = statistics.mean(scores)
            ss_between += n_i * (mean_i - grand_mean)**2
            for s in scores:
                ss_within += (s - mean_i)**2

    df_between = k - 1
    df_within = N - k
    
    f_stat = 0.0
    if df_between > 0 and df_within > 0 and ss_within > 0:
        ms_between = ss_between / df_between
        ms_within = ss_within / df_within
        f_stat = ms_between / ms_within

    # AIC Calculation
    # AIC = N * ln(RSS/N) + 2*k
    # k is actually num_groups + 1 (for variance estimate), but typically just num_groups is used for comparison
    # We will use k_model = num_groups + 1
    k_model = k + 1 
    if ss_within > 0:
        aic = N * math.log(ss_within / N) + 2 * k_model
    else:
        aic = float('inf')

    return f_stat, df_between, df_within, ss_within, k, aic

# --- Main Analysis ---
csv_file = "output/data/mmau_pro_pillars_scores.csv"
taxonomies = ["Baddeley", "P1_Eco", "P2_CASA", "P3_Neuro", "P4_Katz", "P5_Atkinson", "P5_Ext", "MMAU_Original"]
results = []

data = []
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            row['Score'] = float(row['Score'])
            data.append(row)
        except: pass

print("\n--- Comparative ANOVA Results (with AIC) ---")
print(f"{ 'Taxonomy':<15} | { 'k':<3} | { 'F-Stat':<8} | { 'Deviance':<9} | { 'AIC':<8} | { 'P-Value':<8} |{'Power'}")
print("-" * 90)

for tax in taxonomies:
    groups = {}
    for row in data:
        label = row.get(tax)
        if label:
            if label not in groups:
                groups[label] = []
            groups[label].append(row['Score'])
    
    if not groups: continue
        
    f_stat, df_b, df_w, deviance, k, aic = calculate_stats(groups)
    
    # P-Value Calc
    try:
        if f_stat > 100: p_val = 0.0
        else: p_val = fdtr(df_b, df_w, f_stat)
    except: p_val = 1.0
        
    results.append((tax, k, f_stat, df_b, df_w, deviance, aic, p_val))

# Sort by AIC (Lower is Better)
results.sort(key=lambda x: x[6]) # Sort by AIC

for res in results:
    tax, k, f_stat, df_b, df_w, deviance, aic, p_val = res
    power = "High" if f_stat > 10 else "Medium" if f_stat > 5 else "Low"
    if p_val < 1e-4: p_str = "<1e-4"
    else: p_str = f"{p_val:.4f}"
    
    print(f"{tax:<15} | {k:<3} | {f_stat:<8.4f} | {deviance:<9.1f} | {aic:<8.1f} | {p_str:<8} | {power}")

print("\n--- Notes ---")
print("1. Deviance: Residual Sum of Squares (RSS). Lower implies better fit.")
print("2. AIC: Akaike Information Criterion. Lower is better. Penalizes complexity (k).")
print("3. Sorted by AIC (Best balance of simplicity and accuracy).")
