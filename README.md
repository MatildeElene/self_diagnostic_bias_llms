![bias_llm_update](https://github.com/user-attachments/assets/e91d3b3a-ea36-408f-b0c6-56dc8d371372)



# Overview
This repository contains the dataset and analysis from [Elene Hansen & Kristensten-McLachlan (2026)](insert hyperlink):

Repo structure

assignment_2/
├── data/                        # Possible data storage for project
│
├── out/
│   ├── plots/                   # Saved plots and visualizations (.png)
│   └── reports/                 # Classification reports and evaluation outputs (.txt & .csv)
│
├── src/
│   ├── logistic_regression.py   # Logistic regression baseline classifier
│   ├── neural_network.py        # MLP neural network classifier with GridSearchCV
│   └── utils.py                 # Shared utility and preprocessing functions
│
├── requirements.txt             # Python package dependencies
├── setup.sh                     # Environment setup script
├── run.sh                       # Runs the full analysis pipeline
└── README.md                    # Project documentation


| Item                    | Location                                      | Documentation                   |
|-------------------------|--------------------------------------------------------|--------------------------------|
| | | |
| | | |
| | | |
| | | |

<br>

(perhaps more here)

<div style="margin-top: 1.2em;"></div> <!-- 1.2em before notes, 2em before new headings -->

# Technical Requirements
The code was run on (python v) on a macOS ('14.3'). The project requires: 

| Tool     | Installation                                                                 |
|----------|--------------------------------------------------------------------------------------|
| [make](https://www.gnu.org/software/make/manual/make.html) | Installed via [Homebrew](https://formulae.brew.sh/formula/make)                  |
| [uv](https://docs.astral.sh/uv/)                         | Installed through this project's `makefile` (see [Usage](#usage))                 |
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
