# Source Code Overview

This directory contains the analysis and visualization scripts provided with the study. The scripts operate on the released data in [`/data`](../data/) and [`/results`](../results/) and can be used to reproduce the corresponding summary statistics and figures.

Code used to generate the experimental data, including context construction and model querying, is not included in the public repository but is available from the authors upon request.

| Folder/File | Description |
|---|---|
| `figures_study1.py` | Generates the Study 1 figures from the released experimental results. |
| `figures_study2.py` | Generates the Study 2 figures from the released experimental results. |
| `plots_LLM_rstudio.Rmd` | R Markdown script used to generate additional visualizations from the released results. |
| `simple_stats.py` | Computes descriptive statistics and summary measures from the released experimental results. |
| `utils/` | Contains reusable helper functions used by the analysis and visualization scripts. |

📌 For a general project overview, see the [main README](../README.md).
