#!/usr/bin/env python

"""
This script will set up the repo for a new semester by generating markdown files in _modules.
You will need to edit the links in other places (such as index.md and syllabus.md) manually. 
"""

import os
import sys
from datetime import datetime, timedelta
import numpy as np


weekdays = {key: value for key, value in zip(np.arange(7)+1, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_input(prompt):
    input_str = input(prompt)
    if input_str == 'q':
        sys.exit(0)
    return input_str


if __name__ == '__main__':

    # print("Note: Enter \"q\" anytime to quit. ")

    if os.path.exists("_modules") and len(os.listdir("_modules")) > 0:
        print(bcolors.WARNING + "Warning: the _modules folder already contains files. This script may overwrite the existing files. " + bcolors.ENDC)
        confirm = get_input(bcolors.WARNING + "Overwrite? [yes/no] " + bcolors.ENDC)
        if confirm != "yes":
            sys.exit(0)
        print()

    semester_start_date = ""
    lecture_days = []

    while True: 
        try: 
            semester_start_date_str = get_input("* Enter the date of the first class (in the format MM/DD/YYYY): ")
            semester_start_date = datetime.strptime(semester_start_date_str, "%m/%d/%Y")
            # print(weekdays[semester_start_date.weekday()+1])
            break
        except Exception: 
            print(bcolors.WARNING + f"Invalid format: \"{semester_start_date_str}\"" + bcolors.ENDC)

    first_monday = semester_start_date - timedelta(days=semester_start_date.weekday())
    print()
    
    while True: 
        try: 
            print("* Enter the days of the week for the lectures. Separate the days of week by comma. (Use 1 for Monday, 2 for Tuesday, etc) For example, if the lectures are on Mondays, Wednesdays, and Fridays, enter \"1, 3, 5\". ")
            lecture_days_str = get_input("Days of the week for the lectures: ")
            lecture_days = [int(day.strip()) for day in lecture_days_str.split(",")]
            break
        except Exception: 
            print(bcolors.WARNING + f"Invalid format: \"{lecture_days_str}\"" + bcolors.ENDC)

    print()
    
    if semester_start_date.weekday()+1 not in lecture_days:
        raise ValueError(f"{semester_start_date.strftime('%m/%d/%Y')} is a {weekdays[semester_start_date.weekday()+1]}, which is not in {', '.join([weekdays[day] for day in lecture_days])}{bcolors.ENDC}. ")

    print(f"Confirm: the first lecture is on {bcolors.OKCYAN}{semester_start_date.strftime('%m/%d/%Y')} ({weekdays[semester_start_date.weekday()+1]}){bcolors.ENDC} and lectures are on {bcolors.OKCYAN}{', '.join([weekdays[day] for day in lecture_days])}{bcolors.ENDC}. ")
    confirm = get_input("Correct? [yes/no] ")
    if confirm != "yes":
        sys.exit(0)
    print()

    while True: 
        try: 
            num_weeks_str = get_input("* Enter the number of weeks in the semester: ")
            num_weeks = int(num_weeks_str)
            break
        except Exception: 
            print(bcolors.WARNING + f"Invalid format: \"{num_weeks_str}\"" + bcolors.ENDC)

    last_date = first_monday + timedelta(days=7*(num_weeks-1)+lecture_days[-1]-1)
    print(f"The last lecture of the semester will be {bcolors.OKCYAN}{last_date.strftime('%m/%d/%Y')} ({weekdays[last_date.weekday()+1]}){bcolors.ENDC}. ")
    print()

    print("* Enter dates to skip (holidays, days without a lecture, etc) (in the format MM/DD/YYYY). Enter \"done\" to finish. ")
    dates_to_skip = []
    while True: 
        try: 
            date_to_skip_str = get_input("Date to skip: ")
            if date_to_skip_str == "done":
                break
            date_to_skip = datetime.strptime(date_to_skip_str, "%m/%d/%Y")
            # print(weekdays[semester_start_date.weekday()+1])
            dates_to_skip.append(date_to_skip)
        except Exception: 
            print(bcolors.WARNING + f"Invalid format: \"{date_to_skip_str}\"" + bcolors.ENDC)
    print(f"Skipping {len(dates_to_skip)} dates: {', '.join([date.strftime('%m/%d/%Y') for date in dates_to_skip])}")
    print()

    

    count = 1
    os.makedirs("_modules", exist_ok=True)

    # week 1
    md_texts = []
    md_texts.append("---")
    md_texts.append(f"    title: {1}. ")
    md_texts.append(f"    weekNumber: {1}")
    md_texts.append(f"    days:")
    for dow in lecture_days:
        if dow >= semester_start_date.weekday()+1:
            if (first_monday + timedelta(days=7*0+dow-1)) not in dates_to_skip:
                md_texts.append(f'      - date: {(first_monday + timedelta(days=7*0+dow-1)).strftime("%Y-%m-%d")}')
                md_texts.append(f'        events:')
                md_texts.append(f'          "**{count}**{{: .label .label-gray }} Lecture {count}":')
                md_texts.append(f'            "**{count}**{{: .label .label-ghost }} slides • video"')
                count += 1
    md_texts.append("---")
    # print("\n".join(md_texts))
    with open(os.path.join("_modules", f'week-{str(1).zfill(2)}.md'), 'w', encoding="utf-8") as f:
        f.write("\n".join(md_texts))

    # week 2+
    for week in range(1, num_weeks):
        md_texts = []
        md_texts.append("---")
        md_texts.append(f"    title: {week+1}. ")
        md_texts.append(f"    weekNumber: {week+1}")
        md_texts.append(f"    days:")
        for dow in lecture_days:
            if (first_monday + timedelta(days=7*week+dow-1)) not in dates_to_skip:
                md_texts.append(f'      - date: {(first_monday + timedelta(days=7*week+dow-1)).strftime("%Y-%m-%d")}')
                md_texts.append(f'        events:')
                md_texts.append(f'          "**{count}**{{: .label .label-gray }} Lecture {count}":')
                md_texts.append(f'            "**{count}**{{: .label .label-ghost }} slides • video"')
                count += 1
        md_texts.append("---")
        # print("\n".join(md_texts))
        with open(os.path.join("_modules", f'week-{str(week+1).zfill(2)}.md'), 'w', encoding="utf-8") as f:
            f.write("\n".join(md_texts))

    print(bcolors.OKGREEN + f"Success! Generated markdowns for {num_weeks} weeks ({count-1} lectures). " + bcolors.ENDC)
    print("Remember to edit the title for each week and each lecture!")



