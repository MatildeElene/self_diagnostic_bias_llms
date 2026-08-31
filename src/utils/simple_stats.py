# CHECK MEAN SENTENCES FROM EACH STUDY SPECIFIC SYMPTOM CLAUSE CSV, PRIOR TO LINGUISTIC EXTENSION:

import pandas as pd

# Study 1: 18 curated ADHD-I/HI base symptom clauses
s1_base = pd.read_csv(
    "data/clean_symptom_clauses/s1_base_symptom_clauses.csv"
)
s1_base_wc = s1_base["example_rewritten"].str.split().str.len()



# Study 2: 25 curated ADHD-C base symptom clauses
s2_base = pd.read_csv(
    "data/clean_symptom_clauses/s2_base_symptom_clauses.csv"
)

s2_base_wc = s2_base["adhd_c_clause_clean"].str.split().str.len()

#Study 1: final context list after (linguistic extension)
s1_contexts = pd.read_csv(
    "data/context_lists/s1_contexts.csv"
)

s1_context_wc = s1_contexts["symptom_clause"].str.split().str.len()

# Study 2: final context list after (linguistic extension)
s2_contexts = pd.read_csv(
    "data/context_lists/s2_contexts.csv"
)

s2_context_wc = s2_contexts["symptom_clause"].str.split().str.len()

# Creating a summary df: 
summary_df = pd.DataFrame({
    "Study": ["Study 1", "Study 2"],
    "Base clauses": [
        len(s1_base_wc),
        len(s2_base_wc)
    ],
    "Base mean": [
        round(s1_base_wc.mean(), 2),
        round(s2_base_wc.mean(), 2)
    ],
    "Final contexts": [
        len(s1_context_wc),
        len(s2_context_wc)
    ],

    "Final mean": [
        round(s1_context_wc.mean(), 2),
        round(s2_context_wc.mean(), 2)
    ]

})

print(summary_df.to_string(index=False))

#saving summary stats:
summary_df.to_csv("out/descriptive_stats.csv", index=False)