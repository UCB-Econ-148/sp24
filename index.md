---
layout: page
title: Home
nav_order: 1
description: >-
    Data Science for Economists, UC Berkeley, Spring 2024
currWeekNumber: 1
---

# Data Science for Economists
{: .mb-2 }
UC Berkeley, Spring 2024
{: .mb-2 .fs-6 .text-grey-dk-000 }

[PollEV](https://pollev.com/ericvandusen){: .btn .btn-purple }
[Ed](https://edstem.org/us/courses/53352/discussion/){:target="_blank" .btn .btn-ed .mr-1 }
[Gradescope](https://www.gradescope.com/courses/707898){:target="_blank" .btn .btn-gradescope .mr-1 }
<!-- [Lectures Recordings](https://youtube.com/playlist?list=PLQCcNQgUcDfr24xMKf9uY3Nclj2gX0CQD&si=OopnvW3jasaYWx6W){:target="_blank" .btn .btn-recordings .mr-1} -->
[Extenuating Circumstances](https://forms.gle/P5zYy4gXzvhzZeA96){:target="_blank" .btn .btn-blue .mr-1 } 
[Anonymous Feedback](https://forms.gle/sTw8gxu9ryGbcn4R7){:target="_blank" .btn .btn-feedback .mr-1 } 

{: .mb-2 }
**Instructor:** 
{: .mb-0 .fs-5 .text-grey-dk-000 }

<div>
{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
  <div class="role">
    {% for staffer in instructors %}
    {{ staffer }}
    {% endfor %}
  </div>
</div>

{: .mb-3 }
**Lecture:** Tuesday's and Thursday's, 2:00 - 3:29 PM, [Lewis 100](https://dac.berkeley.edu/lewis-hall)       
{: .mb-0 .fs-5 .text-grey-dk-000 }

{: .mb-4 }        
**Office Hours:** see [Calendar](./calendar) and [Ed](https://edstem.org/us/courses/53352/discussion/4119934)
{: .mb-0 .fs-5 .text-grey-dk-000 }

{: .highlight }
> Welcome to [Week {{page.currWeekNumber}}](#week-{{page.currWeekNumber}}) of Econ 148!

+ The schedule and dates listed below are tentative and may be subject to change. 
+ All announcements will be made via Ed once it's set up.
+ The [Syllabus](./syllabus) contains a detailed explanation of how each course component will work this semester
+ If you plan to add late, make sure you contact the staff first to see if you can make up the missed assignments before officially adding the class. 

<a name="schedule"></a>
## Schedule
{% for module in site.modules %}
<a name="week-{{module.weekNumber}}"></a>
{{ module }}
{% endfor %}
