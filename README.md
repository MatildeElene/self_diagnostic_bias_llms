![header_self_diagnostic_bias_llms](https://github.com/user-attachments/assets/70669ddf-6c5a-4be6-a7a3-93829434fee6)

# Overview

This repository contains the data, experimental code, model outputs, and analysis materials accompanying *Gender Associations in LLM-Mediated ADHD Self-Diagnosis*.

The study evaluates gender associations in LLM-mediated ADHD self-diagnosis using an adapted Context Association Test (CAT) under explicit and implicit gender cueing.

## Code and Data Availability

The repository contains the experimental inputs, model outputs, analysis code, and visualization materials used in the study.

Experimental inputs and reference data are provided under [`data/`](data/), model responses and derived evaluation results under [`results/`](results/), and the corresponding experimental, analysis, and visualization code under [`src/`](src/). Generated figures and tables are available under [`out/`](out/).

API credentials are not included. Scripts requiring access to the OpenAI API expect an `OPENAI_API_KEY` to be supplied through a local environment file or environment variable.

## Repository Structure
```
self_diagnostic_bias_llms/
├── data/                         # Experimental inputs and reference data
│   ├── base_symptom_clauses/     # Base symptom clauses used to construct stimuli
│   ├── context_lists/            # Final context sentences used in experiments
│   ├── mapping/                  # Data used in the Reddit-to-DIVA mapping procedure
│   ├── names/                    # SSA name data used for implicit gender cueing
│   ├── proxy_data/               # Clinical reference data
│   └── README.md                 # Data documentation
│
├── src/                          # Experimental, analysis, and visualization code
│   ├── utils/                    # Shared configuration and helper functions
│   ├── prompts/                  # Prompt templates used in the LLM pipeline
│   ├── main.py                   # LLM-based experimental pipeline
│   ├── mapping_pipe.py           # Reddit-to-DIVA mapping procedure
│   ├── figures_study1.py         # Study 1 figures
│   ├── figures_study2.py         # Study 2 figures
│   ├── plots_LLM_rstudio.Rmd     # R Markdown tables and visualizations
│   ├── simple_stats.py           # Descriptive statistics and summaries
│   └── README.md
│
├── results/                      # Model outputs and derived evaluation results
│   ├── responses/                # Raw model responses
│   │   ├── s1_ex_responses.csv
│   │   ├── s1_im_responses.csv
│   │   ├── s2_ex_responses.csv
│   │   └── s2_im_responses.csv
│   │
│   ├── metrics/                  # CAT-derived evaluation metrics
│   │   ├── s1_ex_metrics.csv
│   │   ├── s1_im_metrics.csv
│   │   ├── s2_ex_metrics.csv
│   │   └── s2_im_metrics.csv
│   │
│   ├── summaries/                # Analysis summaries used for tables and figures
│   └── README.md
│
├── out/                          # Generated outputs
│   ├── figures/                  # Figures and visualizations
│   ├── tables/                   # Generated tables
│   └── README.md
│
├── requirements.txt              # Python package dependencies
├── LICENSE                       # Repository license
└── README.md                     # Project documentation
```
**Abbreviations:** `s1`/`s2` = Study 1/Study 2; `ex` = explicit cueing; `im` = implicit cueing.

## Technical Requirements

The analyses were conducted using Python and R. Required Python dependencies are listed in [`requirements.txt`](requirements.txt).

| Tool | Installation |
|---|---|
| Python 3.12.2 | Install Python and the dependencies listed in [`requirements.txt`](requirements.txt). |
| R 4.4.2 + R Markdown | Install R via [CRAN](https://cran.r-project.org/). R Markdown files can be run using [RStudio](https://posit.co/download/rstudio-desktop/) or another compatible environment. |

For scripts that query the OpenAI API, set the `OPENAI_API_KEY` environment variable before running the experimental pipeline.

## License

*Gender Associations in LLM-Mediated ADHD Self-Diagnosis* © 2026 Matilde Elene Hansen and Ross Deans Kristensen-McLachlan.

This work is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Citation

If you use this work, please cite:

> Citation forthcoming.

The paper has been accepted to [EVAL4SD](https://eval4sd.github.io/) (*First Workshop on Evaluating LLMs for Specialized Domains*), co-located with KONVENS 2026. The final published version in the ACL Anthology is forthcoming.

## Acknowledgements

This work was partially supported by the Danish National Research Foundation (Grant No. DNRF193) through TEXT: Center for Contemporary Cultures of Text, Aarhus University.

