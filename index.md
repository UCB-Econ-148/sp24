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

{: .mb-2 }
**Instructor:** Eric Van Dusen (<a>ericvd@berkeley.edu</a>)
{: .mb-0 .fs-5 .text-grey-dk-000 }

{: .mb-3 }
**Lecture:** TuTh 2:00 - 3:29 PM, **Office Hours:** See [Calendar](./calendar) and [Ed](https://edstem.org/us/courses/34369/discussion/)
{: .mb-0 .fs-5 .text-grey-dk-000 }

<div>
{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
  <div class="role">
    {% for staffer in instructors %}
    {{ staffer }}
    {% endfor %}
  </div>
</div>

<!-- [Zoom links](https://edstem.org/us/courses/25130/discussion/2076738){: .btn .btn-purple }  -->
[Textbook](https://www.econ148.org/textbook){: .btn .btn-blue } [Lecture PollEV](https://pollev.com/ericvandusen){: .btn .btn-purple }

+ The schedule and dates listed below are tentative and may be subject to change. 
+ All announcements are on Ed. Make sure you are enrolled and active there.
+ The [Syllabus](./syllabus) contains a detailed explanation of how each course component will work this semester
+ If you plan to add late, make sure you contact the staff first to see if you can make up the missed assignments before officially adding the class. 

<a name="schedule"></a>
## Schedule
<b>🚀 [Jump to current week](#week-{{page.currWeekNumber}}){:target="_self"} </b>
{% for module in site.modules %}
<a name="week-{{module.weekNumber}}"></a>
{{ module }}
{% endfor %}
