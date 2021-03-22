# Filling Area on Line Plots

import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data2.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

Overall_Median = 57287

# plt.fill_between(ages, py_salaries)  # Fills the area under the python salary plot, y2= 0 By default

# plt.fill_between(ages, py_salaries, alpha=0.25)  # Lightens the area under the python plot for better visualization

# plt.fill_between(ages, py_salaries, Overall_Median, alpha=0.25)   # Changes the direction of shading at median

plt.fill_between(ages, py_salaries, dev_salaries, alpha=0.25, where=(py_salaries > dev_salaries), interpolate=True,
                 label='Above Avg')
# Added a conditional for conditional shading

plt.fill_between(ages, py_salaries, dev_salaries, alpha=0.25, where=(py_salaries <= dev_salaries), interpolate=True,
                 color='red', label='Below Avg.')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()
