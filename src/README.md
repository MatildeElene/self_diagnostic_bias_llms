# Source Code Overview

This directory contains the data-processing, experimental, analysis, and visualization code used in the study. The scripts operate on data in [`/data`](../data/) and outputs in [`/results`](../results/).

| Folder/File | Description |
|---|---|
| `main.py` | Main script for running the LLM-based experimental pipeline. |
| `mapping_pipe.py` | Implements the LLM-assisted mapping procedure used to map Reddit-derived symptom descriptions to DIVA-5 examples. |
| `figures_study1.py` | Generates figures for Study 1 from the experimental results. |
| `figures_study2.py` | Generates figures for Study 2 from the experimental results. |
| `plots_LLM_rstudio.Rmd` | R Markdown script used to generate tables and additional visualizations from the analysis outputs. |
| `simple_stats.py` | Computes descriptive statistics and summary measures from the experimental results. |
| `utils/` | Contains shared configuration, API-client setup, and plotting utilities. |

## Utilities

The [`utils/`](utils/) directory contains:

| File | Description |
|---|---|
| `config.py` | Stores model and experimental configuration settings. |
| `openai_client.py` | Initializes the OpenAI API client used by the experimental scripts. |
| `plot_theme.R` | Defines shared plotting and table styles used by the R analysis scripts. |

API credentials are not included in the repository. To run scripts that query the OpenAI API, provide an `OPENAI_API_KEY` through a local environment file or environment variable.

📌 For installation instructions, data structure, and a general overview of the study, see the [main README](../README.md).
