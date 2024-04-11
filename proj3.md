---
layout: default
title: Project 3
nav_order: 6
description: Project 3 instructions, specifications, and rubrics. 
#nav_exclude: true
---

# Project 3
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Timeline
The project is due on **Friday, April 26, 2024**. This is the Friday before RRR week. Once you have finished this project, you will have finished all assignments in this course - congratulations!

In addition, there will be one checkpoint due on **Friday, April 12, 2024**. 

**Note:** During the time of the project, all discussion sections will be turned into optional OH for your group to ask any clarifiying questions. We strongly encourage you to attend these!

## Groups
This is a group project. Good collaboration and leadership will be needed for a successful replication. We ask that you organize yourself in groups of 4. Groups may have members from different discussion sections. We encourage you to use Ed as a place to look for team members, as well as the following [form](https://forms.gle/Z3UUcFPcUMAaBPYY8).

If you are looking for a group to join or if you are in a group looking for additional members, please fill out this [form](https://forms.gle/Z3UUcFPcUMAaBPYY8) before **Friday April 5th, 11:59pm**. We will fill groups short of members by Monday April 8th. 

**Every group must have only 1 member fill out this [form](https://forms.gle/Z3UUcFPcUMAaBPYY8), even if you already have 4 people in your group.**


---
## Introduction

In this project, you will have the opportunity to apply the data science and economic tools and techniques that you have learned throughout the semester to explore and replicate a paper from Berkeley Professor Ted Miguel's extensive work.

Ted Miguel's main research focus is African economic development, including work on the economic causes and consequences of violence; the impact of ethnic divisions on local collective action; interactions between health, education, environment, and productivity for the poor; and methods for transparent social science research. He has conducted field work in Kenya, Sierra Leone, Tanzania, and India (sourced from [his own bio](http://emiguel.econ.berkeley.edu/research_/)). 

Many of the datasets used in his research are posted online, either on the relevant articles [page](http://emiguel.econ.berkeley.edu/research_/) or on his [Dataverse](https://dataverse.harvard.edu/dataverse/emiguel).

---
## Project Objectives

As a group, you'll choose one paper from Ted Miguel's Dataverse and attempt to replicate its findings. Replication in the context of this project refers to **computational reproducibility**, which is:

*The ability to duplicate the results of a prior study using the same data and procedures as were used by the original investigator. Computational reproducibility is done using the same computer code (possibly rebuilt from scratch), but can be achieved using a different software package.* (Dreber and Johannesson (2023))

In other words, you should pick a paper that triggers your group's interests, access its data and source code, and re-code the analysis in your own coding environment, then present your main findings as regression outputs and figures as in the original paper. 

Before doing so, you should, as a group, read and understand the paper's main objectives, policy implications, and especially its methodology section to have the necessary context to pursue a replication.

For more information on different forms of reproducibility, please see The Institute for Replication (I4R)'s [main page](https://i4replication.org/definitions.html).

---
## Deliverables and Rubrics

Your final delivarable should be a Replication Report following the I4R framework. It should be submitted as a PDF, typed up in LaTeX (Chat-GPT can be really helpful for this). Please use the [LaTeX template](https://osf.io/zt5f2) attached. Read the replicaton report template carefully as it contains all the information you need to pursue for a successful replication. Knowing LaTeX is a super-power and makes your work look really pretty!

Past replication reports have taken 10-15 pages, although we will not be checking the page count very carefully. That being said, please be concise in your work. Writing more information than necessary often comes at the cost of clarity. Your communication and presentation is very important for a replication exercise.

In addition, you should submit a [well-organized](https://towardsdatascience.com/how-to-keep-your-research-projects-organized-part-1-folder-structure-10bd56034d3a), compressed (`.zip`) folder that contains a Jupyter notebook and all the data used. We should be able to replicate your work by running the notebook locally on our computers.

Here is the list of deliverables and the grading rubrics. See the replication report for more details. 

### Deliverables

#### Replication Report (50%)

| Deliverable | Points |
| ----------- | ----------- |
| Abstract | 5%  | 
| Introduction | 5% |
| Reproducibility | 20% |
| Checkpoint 2 (More Details Later) | 10% |
| Conclusion | 5% |
| Clarity, Style and Presentation | 5% |


#### Code & Analysis (50%)

| Deliverable | Points |
| ----------- | ----------- |
| Checkpoint (see details [below](#submission-checklists)) | 15% |
| Data Cleaning & Pre-Processing | 5% |
| Modeling (regressions) | 10% |
| Visualizations (figures, tables) | 15% |
| Clarity, Style and Presentation | 5% |

### Grading Rubrics
For each deliverable, we will award points according to the following percentage scale:

| Grade | Description |
| ----------- | ----------- |
| Excellent (above 90%) | Work that is free of all but the most minor errors and demonstrates creativity and/or a very deep understanding of what you are doing. | 
| Good (80-90%) | Work that is free of fundamental errors and demonstrates a basic understanding of what you're doing. |
| Fair (60-80%) | Work with fundamental errors in analysis and/or conveys a lack of understanding of the basics of the work you are attempting to do. |
| Lacking (below 60%) | Work that is severely lacking or incomplete. | 

---
## Datasets and Papers

There are a total of 58 papers published on Ted Miguel's Dataverse. Some contain replication data for RCTs with 1000s of participants over several years with multiple Stata (`.do`/`.dta`) files. Others are far less complex in their data structures, yet seek to answer questions no less interesting. Take this into consideration when your group chooses what paper to replicate. Below are some suggestions that course staff think would be a great options given our limited time:

| Paper | Link |
| ----------- | ----------- |
| Fisman, Raymond, and Edward Miguel. 2007. "Corruption, Norms and Legal Enforcement: Evidence from Diplomatic Parking Tickets." Journal of Political Economy 115 (6): 1020-1048. | [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/28059), [PDF](http://emiguel.econ.berkeley.edu/research/corruption-norms-and-legal-enforcement-evidence-from-diplomatic-parking-tickets/) | 
|Miguel, Edward. 2005. "Poverty and Witch Killing." Review of Economic Studies 72 (4): 1153-1172.| [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/27988), [PDF](http://emiguel.econ.berkeley.edu/assets/assets/miguel_research/44/_Paper__Poverty_and_Witch_Killing.pdf) | 
|Miguel, Edward, Sebastian M. Saiegh, and Shanker Satyanath. 2011. "Civil War Exposure and Violence." Economics & Politics 23 (1): 59-73| [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/29272), [PDF](http://emiguel.econ.berkeley.edu/research/civil-war-exposure-and-violence/) |
|Hsieh, Chang-Tai, Edward Miguel, Daniel Ortega, and Francisco Rodriguez. 2011. "The Price of Political Opposition: Evidence from Venezuela's Maisanta." American Economic Journal: Applied Economics 3 (2): 196-214.| [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/29273), [PDF](https://eml.berkeley.edu/~webfac/bardhan/e271_s08/miguel.pdf) |
| Kramon, Eric, Joan Hamory, Sarah Baird, and Edward Miguel. 2022. “Deepening or Diminishing Ethnic Divides? The Impact of Urban Migration in Kenya.” American Journal of Political Science 66 (2): 365-84 | [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/B8TWK2), [PDF](http://emiguel.econ.berkeley.edu/wordpress/wp-content/uploads/2021/03/KLPS-Urbanization_190219.pdf) |
|Baysan, Ceren; Burke, Marshall; González, Felipe; Hsiang, Solomon; Miguel, Edward, 2020, "Non-economic factors in violence: Evidence from organized crime, suicides and climate in Mexico"| [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HFH5BN), [PDF](https://www.nber.org/system/files/working_papers/w24897/w24897.pdf) |
|Bauer, Michal, Julie Chytilova, and Edward Miguel. (2020). "Using survey questions to measure preferences: Lessons from an experimental validation in Kenya", forthcoming European Economic Review.| [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/M1ITQ1), [PDF](https://www.sciencedirect.com/science/article/abs/pii/S0014292120301252?via%3Dihub) |
|Burke, Marshall, Lauren Falcao Bergquist, and Edward Miguel, "Sell Low and Buy High: Arbitrage and Local Price Effects in Kenyan Markets," The Quarterly Journal of Economics, v.134 2, May 2019, 785-842.| [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/C8UMQP), [PDF](https://economics.harvard.edu/files/economics/files/ms29141.pdf) |
|Miguel, Edward; Burgess, Robin; Jedwab, Remi; Morjaria, Ameet; Padró i Miquel, Gerard, 2016, "The Value of Democracy: Evidence from Road Building in Kenya"| [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PHDDMD), [PDF](https://www.nber.org/system/files/working_papers/w19398/w19398.pdf) |
|Miguel, Edward; Friedman, Willa; Kremer, Michael; Thornton, Rebecca, 2016, "Education as Liberation"| [data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/81NOQY), [PDF](http://emiguel.econ.berkeley.edu/assets/assets/miguel_research/13/Ed-as-Lib_2013-10-14.pdf) |


---
## Submission Checklists

### Checkpoint (due Friday, April 12, 2024)

This will be a separate gradescope assignment that will be due earlier. There is no need to submit any code, a write-up of your progress so far (preferably in LaTeX) will suffice. Everything must be submitted in a single pdf. You must include:    
- Group composition (names and assigned responsibilities).
- Chosen paper.
- Screenshots of the project code organization (including any relevant data/notebook/code).
- Screenshots of LaTeX project in Overleaf following the I4R template.
- A description of what you have attempted to do so far.
- A summary of what's going well and what you are struggling with.
- A note on how course staff may help you succeed.
   
### Project (due Friday, April 26, 2024)
  
- A PDF of the Replication Report (submitted to the project 3 written assignment on Gradescope)
- A PDF file of the Jupyter Notebook containing all the analysis (submitted to the project 3 written assignment on Gradescope)
- A well-organized compressed (`.zip`) file containing: (submitted to the project 3 coding assignment on Gradescope)
    - A Jupyter Notebook that can easily be run to replicate all your results
    - All datasets that you downloaded and used in the notebook
    - Figures and Plots (if not already included in the report or notebook)

---
## Important Notes

- Please do not reach out to Professor Ted Miguel or any of his co-authors with questions about the replications. Direct all questions to course staff: Peter, Rohan, or Professor Van Dusen.
- During the time of the project, all discussion sections will be turned into optional OH for your group to ask any clarifiying questions. We strongly encourage you (and your group) to attend these!
- Course staff may share, with the consent of the group, the best replications with the authors of the paper.
- A lot of the code for the original papers is written in Stata (using `.do`/`.dta` files). Rohan will hold a lecture on translating Stata to Python using a Python package he built ([`Stata2Python`](https://www.econ148.org/textbook/content/01-python_v_stata/syntax.html#stata2python){:target="_blank"}). You may also find Google and ChatGPT helpful for this, but please ensure your code is free of errors and you understand what's going on. Do not simply just copy-and-paste!

<!-- 
### Sources

For Ted Miguel's bio, we used his own found on http://emiguel.econ.berkeley.edu/research_/. -->
