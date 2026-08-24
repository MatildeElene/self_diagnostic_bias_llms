![header_self_diagnostic_bias_llms](https://github.com/user-attachments/assets/70669ddf-6c5a-4be6-a7a3-93829434fee6)

# Overview
This repository contains the dataset and analysis outputs from [Elene Hansen & Kristensten-McLachlan (2026)]:

## Repo structure
```
self_diagnostic_bias_llms/
├── data/                        # Input data used throughout the pipeline
│
├── src/                         # scripts that either transform or analyse data inputs
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

<div style="margin-top: 1.2em;"></div> <!-- 1.2em before notes, 2em before new headings -->

# Technical Requirements
The code was run using Python 4.4.2 on macOS 14.3. The project requires:

| Tool | Installation |
|------|--------------|
| [R 4.4.2](https://cran.r-project.org/bin/macosx/big-sur-arm64/base/) + R Markdown | Install R separately via [CRAN](https://cran.r-project.org/bin/macosx/big-sur-arm64/base/). R Markdown files can be run using [RStudio](https://docs.posit.co/previous-versions/rstudio.html#section-1) or another compatible IDE. |
<div style="margin-top: 2em;"></div>
<a name="usage"></a>

# Citation 
If you use our work, please cite: 

```
*Citation forthcoming*
```
<div style="margin-top: 1.2em;"></div>

> Note: This paper has been accepted to the KONVENS 2026 workshop [EVAL4SD](https://eval4sd.github.io/) (*First Workshop on Evaluating LLMs for Specialized Domains (Eval4SD)*). (The final version, appearing in the ACL Anthology, is forthcoming.)

<div style="margin-top: 2.2em;"></div>

# Acknowledgements
This work was partially supported by the Danish National Research Foundation (Grant No.:
DNRF193) through TEXT: Center for Contemporary Cultures of Text, Aarhus University.

