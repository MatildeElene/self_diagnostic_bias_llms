![header_self_diagnostic_bias_llms](https://github.com/user-attachments/assets/70669ddf-6c5a-4be6-a7a3-93829434fee6)

# Overview
This repository contains the dataset and analysis from [Elene Hansen & Kristensten-McLachlan (2026)](insert hyperlink):

## Repo structure
```
self_diagnostic_bias_llms/
├── data/                        # inputs for later analyses
│
├── src/                         # scripts that either transform or analyse data inputs
│   ├── mapping/                 # semi-automated mapping procedure used for the Reddit-DIVA ()
│   │    ├──
│   │    └──
│   ├── experiments/
│   │    ├──
│   │    └──        
│   └── analysis/                # 
│
├── results/
│   ├── responses/
│   │   ├── s1_ex_responses.csv
│   │   ├── s1_im_responses.csv
│   │   ├── s2_ex_responses.csv
│   │   └── s2_im_responses.csv
│   │
│   └── metrics/                          # CAT derived metrics 
│       ├── s1_ex_metrics.csv
│       ├── s1_im_metrics.csv
│       ├── s2_ex_metrics.csv
│       └── s2_im_metrics.csv
│   
│
├── out/
│   ├── plots/                   # Saved plots and visualizations (.png)
│   └── reports/                 # Classification reports and evaluation outputs (.txt & .csv)
│
├── requirements.txt             # Python package dependencies
├── LICENSE
├── setup.sh                     # Environment setup script
└── README.md                    # Project documentation
```
*NOTE: s1/s2 = Study 1/2; ex = explicit cueing; im = implicit cueing.

<div style="margin-top: 1.2em;"></div> <!-- 1.2em before notes, 2em before new headings -->

# Technical Requirements
The code was run on (python v) on a macOS ('14.3'). The project requires: 

| Tool     | Installation                                                                 |
|----------|--------------------------------------------------------------------------------------|

| [R 4.4.3](https://cran.r-project.org/bin/macosx/big-sur-arm64/base/) + R Markdown           | Installed separately via [CRAN](https://cran.r-project.org/bin/macosx/big-sur-arm64/base) for R and [Posit's RStudio](https://docs.posit.co/previous-versions/rstudio.html#section-1) for running R-Markdown (or an IDE of your liking).                                |

<div style="margin-top: 2.2em;"></div>
<a name="usage"></a>

# Usage

```bash
bash run.sh
```

The command runs ().

> Note: This does not execute `stats.rmd`. It must be run seperately (requires R and R Markdown, see [Technical Requirements](#️-technical-requirements)).

<div style="margin-top: 1.2m;"></div>

# Citation 
If you use our work, please cite: 

```
```
<div style="margin-top: 1.2em;"></div>

> Note: This paper has been accepted to the KONVENS 2026 workshop [EVAL4SD](https://eval4sd.github.io/) (*First Workshop on Evaluating LLMs for Specialized Domains (Eval4SD)*). (The final version, appearing in the ACL Anthology, is forthcoming.)

<div style="margin-top: 2.2em;"></div>

# Acknowledgements
This work was made possible thanks to the following open-source resources:

See also [`metrics/README.md`](metrics/README.md).

# GITHUB TO DO
__To do: ZUSAMMEN__
- update structure?
- check up on license 
- check up on citation
- "should code be updated? Right now it is nooooooot very nice looking"

__To do: MATILDE__
- add to readme.md files in all directories
- check up on code + check python version + check up on rstudio version

__To do: ROSS__
