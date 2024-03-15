---
layout: default
title: Syllabus
nav_order: 2
description: Course structure and policies.
---

# Syllabus 📖
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

**Note:** See [here](../enrollment) for information about enrollment.

---

## Communication 💬

This semester, we'll be using [Ed](https://edstem.org/us/courses/53352/discussion/) to communicate. Ed is where you will see all announcements and get help from staff and other students on assignments and concepts. You will be added to Ed automatically; email the course staff if you're not sure how to access it.

**Important Note:** Staff will not be answering content questions on Ed. Ed is supposed to be a student-run platform in this class; students are encouraged to answer content-related questions instead. Your activity on Ed will be taken into account for your participation grade.

We will not be using bCourses at all in this class; this website and Ed serve as replacements.

---

<!-- ## Logistics 📆

**Lecture:** Lewis 100, TuTh 2:00 - 3:29 PM

**Discussion Section:** See ["Associated Sections"](https://classes.berkeley.edu/content/2024-spring-econ-148-001-lec-001) for more detail. There is no section in the first week of class (Jan 17-20). For the first 3 weeks we need you to go to your assigned section time, and after that we can see if we can be more flexible with section times.

**Office Hours:** Throughout the week, see [Ed](https://edstem.org/us/courses/34369/discussion/) for more detail.

Lectures, discussion sections, and office hours will be hosted in-person by default. We'll post updates in [this post on Ed](https://edstem.org/us/courses/34369/discussion/) and send out announcements if there's any changes.  

---

-->

## About 🧐

**From the course catalog**: This course will give the undergraduate student the basic computational building blocks needed to be a good consumer and producer of applied economics work. Students will work to acquire data through APIs, access census data, or download from replication repositories. The course will cover wrangling data, working with incomplete or unstructured data, joining and merging data, exploratory data analysis and data visualization. The course will cover many aspects of preparing data for econometric analysis.  Practices around literate code, open science tools, reproducibility, and data management will also be covered.  

Econ 148 uses the Python language to teach computation. It also uses the Jupyter Notebook environment, which makes it easy to get started with programming without needing to use a text editor and terminal and is very popular in data science applications. The main Python package we will use for data manipulation is Pandas, and several related packages such as Seaborn, GeoPandas, etc.  **Note that Data 8 (or Stat 20 and familiarity with Python) is a prerequisite to this class, but Data 100 or Econ 140/141 is not.**  

This class serves a different purpose than several other classes that may sound similar. Specifically:
- **Data 8**: Starting from a Data 8 background, this course dives deeper into Python and its applications in economics. After taking this class, you will be able to obtain, clean, and analyze economics data independently, and be well-equipped (in terms of data science skills) to write a paper/thesis and do economics research.
- **Data 100**: Econ 148 is potentially an alternative to Data 100, for students who do not have the prereqs of CS61A and Math 54, and with more focus on data science techniques relevant to economics. Students who have taken Data 100 are suggested NOT to take this class. And, if you can take Data 100 you should take Data 100.
- **Data 88E**: Econ 148 is a "followup" to Data 88E. You will learn more data science skills with real-life datasets. We will also use "industry-standard" packages (e.g. Pandas), the ones that are actually being used in research and workplaces.  
- **CS 61A and CS 88**: While these courses also teach Python, they serve a slightly different purpose - namely, they are designed to introduce students to computer science, not to computing in data science. They cover the Python language in far greater detail than we will, but they do not cover how to work with real-world data. 
- **Econ 140/141**: Econ 140/141 focuses more on how to arrive at the right conclusion using statistical techniques (like various forms of regressions) given a cleaned dataset. Econ 148 focuses more on how to get this dataset, make it a cleaned dataset, and produce exploratory data analysis before diving into main regression. (This is not a trivial portion! Economists spend around 1/3 of their time on getting and cleaning data when doing empirical research!)

If you have already taken the prerequisite Data 8, and are interested in learning more about how to apply data science skills in economics -- welcome! You're in the right place 😎. 

The rough topic breakdown is as follows:
- Pandas 
- Sourcing Data - API and elements of SQL
- Exploratory Data Analysis
- Cleaning and Wrangling Data 
- Visualization - Matplotlib / Seaborn / Plotly / Geopandas
- Preparing Datasets for Econometric Analysis
- Survival Analysis
- Time Series 
- Introduction to ML

Lecture and Discussion slides and code will be posted after each section, and they will cover everything you are required to know for the course.

<!-- There is a work-in-progress textbook -->

Also, note that the course will emphasize the use of real-world data. Some possible datasets include:  
- IPUMS microdata on outcomes of college education
- FRED data on macro indicators 
- Zillow data on cost of housing 
- Who owns real estate in Dubai 
- Telco Churn / Credit Risk

You will leave the course being able to independently apply the skills you've learned to datasets of your own choosing.

---

## Course Structure 🍎

### Lecture

There will be two lectures a week. In lectures, we'll introduce you to new ideas and concepts in data science oriented for economists. Lecture attendance and participation is a part of your participation grade; the specifics are explained in the Policies section below. However, lectures will be recorded and posted after class for you to review in the future. All lecture resources (slides, code, supplemental readings) will be linked on the course website. **Note:** Lecture recordings will only be accessible to students in the course.

During each lecture, there will be a point (or more) at which we stop and ask you to answer a short question via [Poll Everywhere](https://pollev.com/). We call these questions **Quick Checks**. They serve three purposes:
1. For us to get a gauge of how well the class understands the material we're currently covering
2. For you to get a gauge of how well you understand the material we're currently covering
3. For us to record lecture participation

**Quick Checks are graded on completion, not correctness.** It's not important to get these questions right on your first try – but it's important to try them. You will be given time in lecture to answer them.

<br>

### Discussion Section

There is one discussion section a week that is held by Peter and Rohan, our UGSIs. Discussion attendance and activity is a part of your participation grade, and **the midterm will be heavily based on the section material**. Sections are 1 hour long, starting Berkeley-time. The first 15 minutes will be a recap of last week's material, resulting in a summary slide well worth reviewing ahead of your midterm and projects. The remaining time will be spent on the lab of the week, a Jupyter Notebook exercise you're expected to finish on your own time. The hope is that by participating in the discussion section, you will be able to get a good start on the labs and projects. 

<!-- Several sections will continue into office hours, where you're welcome to ask individual questions or comments on the course so far. -->

Expectations towards the students:  
- Participation in class activity. This is incredibly important; the entire class will benefit from a highly collaborative environment while learning data science.
- Academic Integrity and Honesty per the Berkeley Honor Code. 
- Accommodations are done through the office of DSP in due time prior to the start of the event where accommodations are needed. 
- Should technical support be needed, please contact Student Technological Services ahead of time. You'll need either a laptop/mac or a large tablet in this class.

<br>

### Lab and Project

You learn data science by **doing** data science, not by listening or reading about it. As such, labs and projects will be your primary source of learning in this class.

Labs and projects primarily consist of tasks to clean, manipulate, and understand real-life datasets. You will apply the skills you learned in recent lectures to accomplish these tasks. Autograder tests in your notebook will tell you if you're on the right track or not. However, for the projects, the local autograders are not comprehensive – we will have additional hidden tests. Most labs and projects will also include a few "written" problems, where you have to type your answer in text. These problems will be manually graded.

There will be 9 labs and 3 projects in total. In general, lab and project assignments will be released after lectures on Thursday. Labs will be due the following Friday at midnight (11:59PM), and projects will be due several weeks later at Friday at midnight. See the Policies section for our extensions and late submissions policy, as well as our drop policy.

All lab and project assignments should be completed individually except Project 3 (which is a group project; details will be announced later in the semester). But we encourage you to discuss approaches with others; see our Academic Honesty policy below. 

<br>

### Office Hours and Ed

In addition to lectures and labs, we will host several office hours a week. In office hours, you'll get a chance to ask questions about and work with your peers on assignments. You are also very welcome to ask about course logistics and lecture materials. We highly recommend attending office hours if you feel like you need help and/or clarification on any assignments or materials. In the past, OHs have felt very much like co-working spaces that you'll encounter in your future professional lives!

Furthermore, you're encouraged to ask and answer questions about assignments and concepts on Ed. As a reminder, Ed will be a student-run forum this semester and you are expected to answer questions on Ed.

<br>

### Exams

We will have an in-class midterm that covers the first half of the course materials. <!-- The midterm is worth 15% of your total grade. -->

More relevant logistics for exams will be announced on Ed.

---

## Technology 🖥

We will be using several websites this semester. Here's what they're all used for:

- [Course Website](http://www.econ148.org): where all content will be posted.
- [Textbook](http://www.econ148.org/textbook): textbook that accompanies the course.
- [Ed](https://edstem.org/us/courses/53352/discussion/): discussion forum where all announcements will be sent, and where all student-staff and student-student communication will occur. 
- [DataHub](http://data100.datahub.berkeley.edu): where all assignments will be hosted. (You will not usually have to navigate here manually; assignment links on the course homepage bring you to the right place automatically.) <!-- make PR with new packages-->
- [Gradescope](https://www.gradescope.com/courses/707898): where all labs and projects are submitted and all grades live. (Not bCourses! 🙅)
- [Poll Everywhere](https://pollev.com/ericvandusen) : this is where we will do class checks and attendance checks! 

---

## Policies ✏️

### Grading

Here's how we will compute your grade.

| Component | Weight | Notes |
| --- | --- | --- |
| Participation | 15% | Including lectures, discussion sections, and Ed |
| Labs | 25% | 1 lab drop |
| Projects 1 + 2| 20% | no drops |
| Project 3| 15% | |
| Midterm | 25% | |

#### Participation

Attendance will be taken for all lectures and discussions, and Ed activity will be tracked. In addition, we will take into account lecture and discussion *activity* beyond just attendance; people who actively participate will be given a higher score. 

#### Surveys

Since this is a new-ish (2nd offering) class, we're very interested in receiving your feedback as to how it's going and how we can improve. 

As such, we will have feedback survey for you to fill out at the end of very lab. These are a part of your lab grade, and you get a score for completing them (although they're completely anonymous). There is also a general [feedback form](https://forms.gle/sTw8gxu9ryGbcn4R7) where you can share your feedback anonymously at any point throughout the semester.

#### Labs

There will be 9 labs in total and all labs are weighted equally. Labs will consists of autograded coding questions and text-based free response questions. The autograded questions will be graded by correctness, but all test cases used in the autograder will be available to you (i.e. all tests are public, and there is no hidden tests). One free response question will be randomly selected for manual grading in each lab. This free response question will count for 10 to 20% of your grade for that respective lab.

You will have 1 lab drop to be used at any time throughout the semester.

#### Projects

There will be 3 projects in total. Projects 1 and 2 have a weight of 10% each, while project 3 has a weight of 15%. Projects are graded by correctness (both the autograded and the free-response questions). There will be hidden tests for projects. 

<br>

### Late Policy and Extensions

Assignments are due to Gradescope at 11:59PM on the day that they are due. We will have a small grace period of 3 minutes (until 12:02 am) to account for any technical difficulties. It is your responsibility to be proactive about your submissions; staff are not expected to be active on midnight to help you with submission issues.

Students are allowed to submit labs and projects late for a 50% penalty within 48 hours after they are due, after which they will receive no credit. We will factor in late submissions when we're calculating grades at the end of the semester.

**Extensions:** We know this is a stressful time, and we don't want to penalize you because of circumstances that are out of your control. To request an extension, please submit [this google form](https://forms.gle/P5zYy4gXzvhzZeA96) as soon as possible (definitely before the deadline). As long as your request is within reason, there's a good chance of it being granted. Students with DSP accommodations that allow for late assignment submissions will still need to fill out the google form, but no explanation will be required.

<br>

### Regrade Requests

When scores for assignments are released, regrade windows will be open for two days. Regrade requests that are made via email/Ed or are made outside of the designated regrade window will not be considered.

<br>

### Academic Honesty

You must write your answers in your own words, and you must not plagiarize your completed work. Every semester we have to deal with people who share answers, attendance passwords, and code. We can see it and we can test for it with a detection script. 

Make a serious attempt at every assignment yourself. If you get stuck, read the supporting code, refer to examples in the lectures and discussion sections. After that, go ahead and discuss any remaining doubts with others, especially the course staff during office hours. That way you will get the most out of the course content.

You are also not permitted to turn in answers or code that you have obtained from others. Not only is such copying dishonest, it misses the point of the assignments, which is not for you to find the answers somewhere and send them along to the staff. It is for you to figure out how to solve the problems, with the support available in the course.

The landscape of using AI for help with coding is rapidly changing. To succeed in the class, you will need to learn fundamental concepts without assistance from AI. For one example, you will not be allowed to use AI for the in-class, handwritten midterm. Use common sense and cite any AI you do use. Flagrant and obvious use of AI will not demonstrate your understanding of the concept and will lead to grading penalties. We have all used AI for help with coding, and we have seen that using AI without a solid understanding of the fundamentals can lead to incorrect, buggy and inefficient code.

Please read [Berkeley's Code of Conduct](https://conduct.berkeley.edu/code-of-conduct/) carefully. Penalties for cheating at UC Berkeley are severe and include reporting to the [Center for Student Conduct](https://conduct.berkeley.edu/). They might also include a F in the course or even dismissal from the university. It's just not worth it.

Data science is a collaborative activity. As such, we encourage you to discuss assignments with others. Go on Ed and discuss with other students. We expect that you will work with integrity and with respect for other members of the class, just as the course staff will work with integrity and with respect for you.

You are not alone in this course! We're here to help you succeed. If you invest the time to learn the material and complete the assignments, you won’t need to copy any answers. If you use code you found online, please cite it in a comment.

<br>

### Inclusion

The instructor and course staff are committed to creating an inclusive learning environment, one that welcomes all students and supports a diversity of beliefs, thoughts, perspectives, values, and experiences, and one that respects all identities and backgrounds (including race/ethnicity, nationality, gender, class, religion, ability, sexual orientation, etc.) 

To help accomplish this:  
- If you feel like your performance in the class is being impacted by your experiences outside of class, please do not hesitate to come and talk with the instructor or course staff. We are here to be a resource for you.
- We are here to learn, and sometimes along the way we make mistakes. If something is said in class that makes you feel uncomfortable, please come and talk to the instructor or course staff about it.
- As a participant in this class, you should strive to respect the diversity and experiences of your classmates.

<br>

### Accommodations

If you have any special needs or require ability-related accommodations, please notify the instructor as soon as possible. If an unexpected personal or medical challenge is interfering with your ability to complete assignments and/or attend class, it is important that you contact the instructor or course staff as early as possible. Further resources are available through the [Disabled Students Program](https://dsp.berkeley.edu).


---

## Acknowledgements 🙏

This class is loosely based on Data C100 and Data 88E. When creating Econ 148, we've referred to the materials of several other courses:

- [Data 8](http://data8.org)
- [Data 100](https://ds100.org)
- [ERE 131](https://erg.berkeley.edu/new-erg-course-data-environment-and-society/)
- [DS Modules](https://www.github.com/ds-modules)



The website uses [Just the Class](https://kevinl.info/just-the-class/).
