import csv

# --- 1. Define Mappings (Hardcoded from the Mapping Matrix) ---
PILLAR_MAP = {
    # Category: (Baddeley, P1_Eco, P2_CASA, P3_Neuro, P4_Katz, P5_Atkinson)
    "Sound":                ("Sensory", "Physics", "Primitive", "Ventral", "Decoding", "Sensory/STS"),
    "Music":                ("Phonological Loop", "Physics", "Primitive", "Ventral", "Decoding", "Sensory/STS"),
    "Speech":               ("Phonological Loop", "Semantics", "Primitive", "Ventral", "Decoding", "Sensory/STS"),
    "Sound-Music":          ("Executive-Inhibition", "Physics", "Schema", "Dorsal", "TFM", "Control"),
    "Speech-Music":         ("Executive-Inhibition", "Semantics", "Schema", "Dorsal", "TFM", "Control"),
    "Speech-Sound":         ("Executive-Inhibition", "Semantics", "Schema", "Dorsal", "TFM", "Control"),
    "Sound-Music-Speech":   ("Executive-Inhibition", "Semantics", "Schema", "Dorsal", "TFM", "Control"),
    "Spatial":              ("Sketchpad", "Physics", "Primitive", "Dorsal", "Integration", "Control"),
    "Voice":                ("Episodic Buffer", "Semantics", "Primitive", "Ventral", "Decoding", "Sensory/STS"),
    "Multi-Audio":          ("Executive-Inhibition", "Semantics", "Schema", "Dorsal", "TFM", "Control"),
    "Open-ended":           ("Episodic Buffer", "Semantics", "Schema", "Ventral", "Organization", "Control"),
    "IF":                   ("Executive-Logic", "Semantics", "Schema", "Ventral", "Organization", "Control")
}

input_csv = "output/mmau_pro_full_performance.csv"
output_csv = "output/data/mmau_pro_pillars_scores.csv"

# --- 2. Process Data ---
rows_out = []
header = ["Model", "Category", "Score", "Baddeley", "P1_Eco", "P2_CASA", "P3_Neuro", "P4_Katz", "P5_Atkinson"]

with open(input_csv, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        model_name = row['Models']
        if model_name == "Random Choice": continue
        
        for cat, mapping in PILLAR_MAP.items():
            if cat not in row: continue
            
            score_str = row[cat].strip()
            if score_str == "-" or score_str == "": continue
            
            try:
                score = float(score_str)
                rows_out.append([
                    model_name,
                    cat,
                    score,
                    mapping[0], # Baddeley
                    mapping[1], # P1
                    mapping[2], # P2
                    mapping[3], # P3
                    mapping[4], # P4
                    mapping[5]  # P5
                ])
            except ValueError:
                continue

# --- 3. Write Output ---
import os
import os.path

if not os.path.exists("output/data"):
    os.makedirs("output/data")

with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows_out)

print(f"Successfully generated {output_csv} with {len(rows_out)} rows.")