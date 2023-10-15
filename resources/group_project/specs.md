---
layout: default
title: Group Project
nav_order: 6
description: Group project instructions, specifications, and rubrics. 
---

# Group Project
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


**Access the template ipynb here:**  

[Download](https://www.econ148.org/sp23/resources/group_project/project_template.ipynb){: .btn .btn-blue }  [View in Datahub](https://datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FUCB-Econ-148%2Fsp23-student&branch=main&urlpath=lab%2Ftree%2Fsp23-student%2Fproj%2Fproj03%2Fproject_template.ipynb){: .btn }  [View in Colab](https://drive.google.com/file/d/1meqwXGTfs0iQt7NYxpapZrOd6Wbfaub-/view?usp=sharing){: .btn }  

**Group assignments are released [here](https://docs.google.com/spreadsheets/d/1yt70gxBrpmd4xM0fyGx71kwTrr-S6-1sST6xedNyV-k/edit?usp=sharing).**   

{: .note }
See clarifications and submission instructions on [Ed](https://edstem.org/us/courses/34369/discussion/3018671). 

---
## Introduction

In this project, you will have the opportunity to apply the data science techniques that you have learned throughout the semester to explore and replicate papers from the [Equality of Opportunity Project](http://www.equality-of-opportunity.org/data/), led by Harvard Professor Raj Chetty.

The Equality of Opportunity Project aims to provide insights into the sources of economic mobility and to identify effective policy interventions to promote equality of opportunity in the United States. The project has collected an extensive dataset that includes anonymized tax records for millions of individuals, which has been used in numerous research papers to study topics such as intergenerational mobility, the effects of education on earnings, and the impacts of neighborhoods on children's outcomes.

Through this project, you will have the chance to work with this rich dataset and replicate some of the papers published by Professor Chetty and his colleagues. You will use Python and Pandas to explore the data, clean it, and analyze it, applying the techniques you have learned in class to answer research questions and test hypotheses. You will also have the chance explore ideas of your interests using the datasets. 

---
## Timeline
The project is due on **May. 1st**. 

---
## Deliverables and Rubrics
The template notebook is the template for the group project. Read the project template carefully as it contains all the instructions for this project--each markdown cell provides instructions on what to do in order to complete a successful project. 

Here is the list of deliverables and the grading rubrics. See the project template for more details. 

### Deliverables

| Deliverable | Points |
| ----------- | ----------- |
| Abstract | 5%  | 
| Project Background | 5% |
| Project Objective | 5% |
| Data Description | 5% |
| Data Cleaning | 5% |
| EDA | 20% |
| Modeling | 20% |
| Interpretation and Conclusions | 20% |
| Post-Analysis Reproducibility | 10% |
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

In order to make the project consistent across teams, we are limiting the project to a specific set of datasets that are linked to economics journal articles.  

Browse and choose one of the datasets from Harvard Professor Raj Chetty's [Equality of Opportunity Project](http://www.equality-of-opportunity.org/data/). You will find them neatly presented (and mostly cleaned) together with the title of the corresponding research paper. 

| Paper | Link |
| ----------- | ----------- |
| Race and Economic Opportunity in the United States: An Intergenerational Perspective | [summary](https://opportunityinsights.org/paper/race/), [PDF](https://opportunityinsights.org/wp-content/uploads/2018/04/race_paper.pdf) | 
| Who Becomes an Inventor in America? The Importance of Exposure to Innovation | [summary](https://opportunityinsights.org/paper/losteinsteins/), [PDF](https://opportunityinsights.org/wp-content/uploads/2019/01/patents_paper.pdf) |
| Mobility Report Cards: The Role of Colleges in Intergenerational Mobility | [summary](https://opportunityinsights.org/paper/mobilityreportcards/), [PDF](https://opportunityinsights.org/wp-content/uploads/2018/03/coll_mrc_paper.pdf) |
| The Fading American Dream: Trends in Absolute Income Mobility Since 1940 | [summary](https://opportunityinsights.org/paper/the-fading-american-dream/), [PDF](https://opportunityinsights.org/wp-content/uploads/2018/03/abs_mobility_paper.pdf) | 
| The Effects of Neighborhoods on Intergenerational Mobility | [summary](https://opportunityinsights.org/paper/neighborhoodsi/), [PDF](https://opportunityinsights.org/wp-content/uploads/2018/03/movers_paper1.pdf) | 
| Childhood Environment and Gender Gaps in Adulthood | [summary](https://opportunityinsights.org/paper/gendergaps/), [PDF](https://opportunityinsights.org/wp-content/uploads/2018/03/gender_paper.pdf) |
| The Association Between Income and Life Expectancy in the United States, 2001-2014 | [summary](https://opportunityinsights.org/paper/lifeexpectancy/), [PDF](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4866586/pdf/nihms783419.pdf) |
| Measuring the Impacts of Teachers I and II: Evaluating Bias in Teacher Value-Added Estimates and Teacher Value-Added and Student Outcomes in Adulthood | I: [summary](https://opportunityinsights.org/paper/teachersi/), [PDF](https://opportunityinsights.org/wp-content/uploads/2018/03/teachers1.pdf); II: [summary](https://opportunityinsights.org/paper/teachersii/), [PDF](https://opportunityinsights.org/wp-content/uploads/2018/03/teachers2.pdf) |
| Is the United States Still a Land of Opportunity? Recent Trends in Intergenerational Mobility | [summary](https://opportunityinsights.org/paper/recentintergenerationalmobility/), [PDF](https://opportunityinsights.org/wp-content/uploads/2018/04/mobility_trends.pdf) | 
| Where is the Land of Opportunity? The Geography of Intergenerational Mobility in the United States | [summary](https://opportunityinsights.org/paper/land-of-opportunity/), [PDF](https://opportunityinsights.org/wp-content/uploads/2018/03/mobility_geo.pdf) | 

---
## Submission Checklists

### Project
* A Jupyter Notebook
* A PDF file of the Jupyter Notebook
* Include a link to all datasets that you downloaded and used in the notebook
* Figures and Plots (if not already included in the notebook)

### Peer Review and Assessment
* Peer review (for reproducibility) on another group's project
* Peer review for groupmates' contributions

---
## Additional Resources
How to Import Files in Colab: [External data: Local Files, Drive, Sheets, and Cloud Storage](https://colab.research.google.com/notebooks/io.ipynb)

