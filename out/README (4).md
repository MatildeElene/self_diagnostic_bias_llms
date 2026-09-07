# Supplementary Materials
The supplementary materials contain () and a pdf (prompt cues)


## Files 
### 1. summary_metrics.xlsx
Contains aggregate CAT-based evaluation metrics computed at the study-condition level.

For Study 1, ADHD-I and ADHD-HI contexts are pooled when calculating LMS, BS, and MPS metrics. For Study 2, metrics are computed using ADHD-C contexts only.

Each row corresponds to a single study-condition combination and includes:

* Model identifier
* Test version
* Temperature setting

Language Modeling Scores (LMS)

* LMS (Total)
* LMS (Men)
* LMS (Women)

Bias Scores (BS)

* BS (Total)
* BS (Men)
* BS (Women)

Model Performance Scores (MPS)

* MPS (Total)
* MPS (Men)
* MPS (Women)

Response Counts

* Total Responses
* Valid Responses
* Meaningful Responses
* Proxy-Aligned Responses

#### Definitions:

* __Valid Responses:__ Model outputs that could be assigned to one of the expected categories (MEN, WOMEN, BASKETBALL, or NONE).

* __Meaningful Responses__: Valid responses assigned to a gendered target category (MEN or WOMEN), excluding control (BASKETBALL) and noncompliant (NONE) responses.

* __Proxy-Aligned Responses__: Meaningful responses where the model selected the gender category that is empirically overrepresented for the relevant ADHD subtype in the clinical proxy distribution.


### 2. subtype_analyses.xlsx
Contains chi-square analyses comparing observed gender distributions against clinically informed proxy distributions.

Each row represents either an overall study-level analysis or a subtype-specific analysis and includes:

* Model identifier
* Test version
* ADHD subtype (or Overall)
* Number of gendered responses (N)
* Observed male and female response counts
* Expected male and female response counts
* Chi-square test statistic (χ²)
* Corresponding p-value

For Study 1 (ADHD-I and ADHD-HI), both overall and subtype-specific chi-square analyses are reported.

For Study 2 (ADHD-C), only subtype-specific analyses are reported, as the overall and subtype-level distributions are identical for the single ADHD-C category.

### 3. trial_level_outputs.xlsx

Contains trial-level model outputs for all four association tests. Each worksheet corresponds to one experimental condition:

* Study 1 – Explicit
* Study 1 – Implicit
* Study 2 – Explicit
* Study 2 – Implicit

Each row represents a single model inference and includes:

* Model identifier
* Trial ID
* Symptom ID
* Test version
* ADHD subtype
* Symptom clause
* Symptom clause ID
* Raw model response
* Cleaned response category
* Temperature setting

For implicit tests, the workbook additionally includes:

* Male Name
* Female Name

#### Definitions:

* __Male Name / Female Name__: The gender-indicative name pair presented to the model during implicit cueing tests. Names function as demographic cues and are subsequently mapped to the categories MEN and WOMEN during analysis.

* __Replication__: Identifier distinguishing repeated evaluations of the same symptom context under a given experimental condition. This variable is only used in explicit-condition tests.