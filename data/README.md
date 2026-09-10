# Data Overview

This directory contains the data used to construct the experimental materials and clinically informed reference distributions used in the study. It includes source and intermediate data used for symptom mapping and name selection, the base symptom clauses and final context lists used as experimental inputs, and the proxy data used for comparative evaluation.

| Folder | Description |
|---|---|
| `base_symptom_clauses/` | Contains the base ADHD symptom clauses used to construct the experimental contexts for Studies 1 and 2. |
| `context_lists/` | Contains the final paraphrased context lists used as experimental inputs for Studies 1 and 2. |
| `mapping/` | Contains the data used in the Reddit-to-DIVA-5 symptom mapping procedure underlying construction of the symptom clauses. |
| `names/` | Contains U.S. Social Security Administration baby-name data used to select gender-indicative names for the implicit cueing condition. |
| `proxy_data/` | Contains the clinical data used to derive the gender- and ADHD-subtype-specific proxy distributions used for comparative evaluation. |

📌 For a general project overview, see the [main README](../README.md).

## Proxy Data

The original supplementary material provided by [Platania et al. (2025)](https://www.frontiersin.org/journals/global-womens-health/articles/10.3389/fgwh.2025.1549028/full) is included alongside an extracted CSV containing the data used to derive the clinically informed reference distributions in the present study. The original file is retained unchanged to preserve the provenance of the derived proxy data.

## Name Data

Gender-indicative names used in the implicit cueing condition were selected using baby-name data from the U.S. Social Security Administration (SSA). The original SSA data are retained in [`names/`](names/) to preserve the source data used in the study.

The SSA source data are U.S. government data and are not original materials produced by the authors. The repository license therefore does not assert ownership over these source data.

## Symptom Mapping Data

The [`mapping/`](mapping/) directory contains materials used in the LLM-assisted mapping of Reddit-derived self-reported sentences to adult ADHD examples from the DIVA-5 framework. These mappings were used in constructing the symptom materials for the subsequent experiments.

Prompt templates associated with the mapping procedure are provided separately under [`../src/prompts/`](../src/prompts/).

## DSM-5 Symptom Overview

The experimental contexts were constructed to represent the 18 adult ADHD symptoms defined by the DSM-5, comprising nine predominantly inattentive (ADHD-I) and nine hyperactive–impulsive (ADHD-HI) symptoms. Study 1 evaluates these symptom groups separately, while Study 2 combines inattentive and hyperactive–impulsive symptom clauses to construct ADHD-C contexts.

<img width="849" height="531" alt="Overview of DSM-5 ADHD symptoms used to construct the experimental contexts" src="https://github.com/user-attachments/assets/9ff93345-d68e-41c9-b620-1974e4e53548" />
