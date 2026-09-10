# Source Code Overview

This directory contains the data-processing, experimental, analysis, and visualization code used in the study. The scripts operate on data in [`/data`](../data/) and produce results and derived outputs in [`/results`](../results/) and [`/out`](../out/).

| Folder/File | Description |
|---|---|
| `main.py` | Main script for running the LLM-based experimental pipeline. |
| `mapping_pipe.py` | Implements the LLM-assisted mapping of Reddit-derived symptom descriptions to DIVA-5 examples. |
| `figures_study1.py` | Generates figures for Study 1 from the experimental results. |
| `figures_study2.py` | Generates figures for Study 2 from the experimental results. |
| `plots_LLM_rstudio.Rmd` | Generates tables and additional visualizations from the analysis outputs. |
| `simple_stats.py` | Computes descriptive statistics and summary measures from the experimental results. |
| `prompts/` | Contains prompt templates used for symptom mapping, paraphrasing, and the explicit and implicit CAT experiments. |
| `utils/` | Contains shared configuration, API-client setup, and plotting utilities. |

## Prompts

The [`prompts/`](prompts/) directory contains the prompt materials used in the LLM-based components of the study.

| File | Description |
|---|---|
| `explicit_cat_prompt.txt` | Prompt template used for the explicit gender-cueing CAT condition. |
| `implicit_cat_prompt.txt` | Prompt template used for the implicit gender-cueing CAT condition. |
| `paraphrasing_prompt.txt` | Prompt used to generate semantically equivalent symptom-clause variants. |
| `mapping_system_prompt.txt` | System prompt used for the Reddit-to-DIVA-5 mapping procedure. |
| `mapping_user_prompt.txt` | User-prompt template used for the Reddit-to-DIVA-5 mapping procedure. |

The mapping user prompt is stored as a template; the DIVA-5 examples and Reddit-derived sentences supplied during individual calls are provided separately under [`/data`](../data/).

## Utilities

The [`utils/`](utils/) directory contains:

| File | Description |
|---|---|
| `config.py` | Stores model and experimental configuration settings. |
| `openai_client.py` | Initializes the OpenAI API client used by the experimental scripts. |
| `plot_theme.R` | Defines shared plotting and table styles used by the R analysis scripts. |
| `.env.example` | Provides the expected format for supplying an OpenAI API key locally. |

API credentials are not included in the repository. To run scripts that query the OpenAI API, provide an `OPENAI_API_KEY` through a local environment file or environment variable. The included `.env.example` can be used as a template.

📌 For installation instructions, data structure, and a general overview of the study, see the [main README](../README.md).
