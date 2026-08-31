![header_self_diagnostic_bias_llms](https://github.com/user-attachments/assets/70669ddf-6c5a-4be6-a7a3-93829434fee6)

# Overview

This repository contains the data, model outputs, and analysis materials accompanying *Gender Associations in LLM-Mediated ADHD Self-Diagnosis*.

## Code and Data Availability

The repository contains the data and analysis code required to reproduce the reported summary statistics and figures. Experimental inputs and model outputs are provided under [`data/`](data/) and [`results/`](results/), while the corresponding analysis and visualization scripts are available under [`src/`](src/).

Code used to generate the experimental data, including context construction and model querying, is not included in the public repository but is available from the authors upon request.

## Repo structure
```
self_diagnostic_bias_llms/
├── data/                        # Experimental inputs and reference data
│   ├── context_lists/           # Final context sentences used in experiments
│   ├── base_symptom_clauses/    # Base clauses used to construct context lists
│   ├── platania_proxy_data.csv  # Extracted clinical reference data
│   ├── platania_supplementary.xlsx
│   └── README.md
├── src/                         # Analysis and visualization scripts
│
├── results/                     # Model outputs and derived evaluation results
│   ├── responses/               # Raw model responses from the four experiments
│   │   ├── s1_ex_responses.csv
│   │   ├── s1_im_responses.csv
│   │   ├── s2_ex_responses.csv
│   │   └── s2_im_responses.csv
│   │
│   └── metrics/                   # CAT-derived evaluation metrics
│       ├── s1_ex_metrics.csv
│       ├── s1_im_metrics.csv
│       ├── s2_ex_metrics.csv
│       └── s2_im_metrics.csv
│   
│
├── out/                         # Generated analysis outputs
│   ├── plots/                   # Figures and visualizations (.png)
│   └── reports/                 # Statistical and evaluation reports (.txt, .csv)
│
├── requirements.txt             # Python package dependencies
├── LICENSE                      # Repository license
└── README.md                    # Project documentation
```
*NOTE: s1/s2 = Study 1/2; ex = explicit cueing; im = implicit cueing.


# Technical Requirements
The analyses were conducted using Python and R. Required Python dependencies are listed in [`requirements.txt`](requirements.txt).

| Tool | Installation |
|------|--------------|
| Python 3.12.2 | Install Python and the dependencies listed in [`requirements.txt`](requirements.txt). |
| R 4.4.2 + R Markdown | Install R via [CRAN](https://cran.r-project.org/). R Markdown files can be run using [RStudio](https://posit.co/download/rstudio-desktop/) or another compatible environment. |


# License

Gender Associations in LLM-Mediated ADHD Self-Diagnosis © 2026 by Matilde Elene Hansen and Ross Deans Kristensen-McLachlan is licensed under CC BY 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/

# Citation
If you use this work, please cite:

> Citation forthcoming.

The paper has been accepted to the KONVENS 2026 workshop [EVAL4SD](https://eval4sd.github.io/) (*First Workshop on Evaluating LLMs for Specialized Domains*). The final published version in the ACL Anthology is forthcoming.


# Acknowledgements
This work was partially supported by the Danish National Research Foundation (Grant No.:
DNRF193) through TEXT: Center for Contemporary Cultures of Text, Aarhus University.

