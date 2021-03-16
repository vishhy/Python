from matplotlib import pyplot as plt

# print(plt.style.available)
# plt.style.use('fivethirtyeight')
# xkcd comics, anti-gravity module
plt.xkcd()

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]  # x-axis

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]  # y-axis

# Median Python Developer Salaries by Age

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.', label='All Devs')
#linewidth

plt.plot(ages_x, py_dev_y, marker='o', label='Python Devs')
plt.plot(ages_x, js_dev_y, marker='^', label='JS Devs')
# We can also use hex values for colours

plt.title('Median Developer Salaries by Age')

# plt.legend(['All Devs', 'Python Devs'])
plt.legend()

plt.xlabel('Ages')
plt.ylabel('Median Salaries in USD')

# GRID
# plt.grid(True)

plt.tight_layout()

# plt.savefig('path/plot.png'), saves the plot automatically

plt.show()
