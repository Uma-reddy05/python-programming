"""
Day 18 - matplotlib in python
Author - Uma
Date - 22-10-2026
"""

import matplotlib.pyplot as plt


#------LINE GRAPH-------
days = [1, 2, 3, 4, 5]

marks = [50, 60, 75, 65, 90]

plt.plot(days, marks)

plt.title("my marks progress")
plt.xlabel("days")
plt.ylabel("marks")

plt.show()


#-------BAR CHART----------
subject = ["maths", "python", "chemistry", "physics"]
subject_marks = [98, 99, 95, 98]

plt.bar(subject, subject_marks)
plt.title("subject marks")
plt.xlabel("subject")
plt.ylabel("marks")

plt.show()


#------PIE CHART-------
study_sub = ["maths", "python", "chemistry"]
hours = [3, 2, 4]

plt.pie(hours, labels=study_sub, autopct="%1.1f%%")
plt.title("study time distribution")
plt.show()


"""
------WHAT I LEARNED-------

1. plt.plot() — creates a line graph.
2. plt.bar() — creates a bar chart.
3. plt.pie() — creates a pie chart.
4. plt.title() — adds a title.
5. plt.xlabel() and plt.ylabel() — label the axes.
6. plt.show() — displays the graph.
7. marker="o" — adds circular markers to the line graph.
8. autopct="%1.1f%%" — displays percentages on the pie chart.

"""