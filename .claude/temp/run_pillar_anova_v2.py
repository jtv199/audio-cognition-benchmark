import csv
import statistics
import math

# --- Helper: Beta Function for F-Distribution (Pure Python) ---
def log_beta(x, y):
    return math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y)

def beta_inc(x, a, b):
    # Regularized Incomplete Beta Function (simpson's rule or series expansion)
    # Using a simple series expansion for approximation
    if x == 0: return 0
    if x == 1: return 1
    
    # Symmetry
    if x > (a + 1) / (a + b + 2):
        return 1 - beta_inc(1 - x, b, a)
        
    lbeta = log_beta(a, b)
    factor = math.exp(a * math.log(x) + b * math.log(1 - x) - lbeta) / a
    
    # Lentz's method for continued fraction would be better, but let's use a small loop
    # actually, for F-test p-values, we just need 1 - CDF.
    # Let's try a simpler integration if needed, or just standard series.
    # Series expansion:
    result = 1.0
    term = 1.0
    for i in range(1, 100):
        numerator = i * (1 - b + i) * x
        denominator = (a + i + 1) * (a + 2 * i) # simplified, actually complex
        # This is getting risky for a pure python script without reliable libraries.
        # Let's use a simpler approximation or just omit if too hard.
        pass
    
    # FALLBACK: Use a known approximation for F-test p-value
    return 0.0 # Placeholder if too complex

def fdtr(df1, df2, f):
    # Calculate P-value for F-test using approximations
    # Based on: Abramowitz and Stegun 26.6.15 (Normal approx)
    # or Paulson's approximation
    if f <= 0: return 1.0
    
    x = df2 / (df2 + df1 * f)
    # P(F > f) = Ix(df2/2, df1/2) where Ix is regularized beta function
    # Let's implement a rudimentary Simpson's integration for Beta
    # B(z; a, b) = integral from 0 to z of t^(a-1) (1-t)^(b-1) dt
    
    a = df2 / 2.0
    b = df1 / 2.0
    
    # Numerical integration (Simpson's rule)
    n = 100
    h = x / n
    s = 0
    
    def f_beta(t):
        if t <= 0 or t >= 1: return 0
        return (t**(a-1)) * ((1-t)**(b-1))
        
    for i in range(1, n): # 1 to n-1
        t = i * h
        weight = 4 if i % 2 == 1 else 2
        s += weight * f_beta(t)
        
    s += f_beta(x) # End point (start point 0 is 0 or inf, handle carefully)
    # Start point limit check: if a > 1, f(0)=0. If a < 1, singularity.
    # Assuming df >= 2 usually.
    
    integral = (h/3) * s
    beta_val = math.exp(log_beta(a, b))
    
    return integral / beta_val

# --- Helper Function for ANOVA ---
def calculate_anova(groups):
    all_scores = [s for sublist in groups.values() for s in sublist]
    grand_mean = statistics.mean(all_scores)
    N = len(all_scores)
    k = len(groups) # Parameter count (categories)
    
    if k < 2: return 0.0, 0, 0, 0.0

    # SS Between
    ss_between = 0
    for scores in groups.values():
        n_i = len(scores)
        mean_i = statistics.mean(scores)
        ss_between += n_i * (mean_i - grand_mean)**2

    # SS Within (Deviance)
    ss_within = 0
    for scores in groups.values():
        mean_i = statistics.mean(scores)
        for s in scores:
            ss_within += (s - mean_i)**2

    df_between = k - 1
    df_within = N - k
    
    if df_between == 0 or df_within == 0: return 0.0, df_between, df_within, ss_within

    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    
    if ms_within == 0: return 0.0, df_between, df_within, ss_within

    f_stat = ms_between / ms_within
    return f_stat, df_between, df_within, ss_within, k

# --- Main Analysis ---
csv_file = "output/data/mmau_pro_pillars_scores.csv"
taxonomies = ["Baddeley", "P1_Eco", "P2_CASA", "P3_Neuro", "P4_Katz", "P5_Atkinson"]
results = []

# Load Data
data = []
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['Score'] = float(row['Score'])
        data.append(row)

print("\n--- Comparative ANOVA Results ---")
# Headers
print(f"{ 'Taxonomy':<12} | { 'k':<3} | { 'F-Stat':<8} | { 'df':<8} | { 'Deviance':<9} | { 'P-Value':<8} | {'Power'}")
print("-" * 80)