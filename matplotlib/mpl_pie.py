from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]  # to give an emphasis

# Using Pie Chart for this data, makes the pie chart crowded. So, either use bar chart or reduce the data. Upto 5 pie

# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'}, explode=explode, shadow=True, startangle=90,
        autopct='%1.1f%%')

# autopct gives %age to the slices

plt.title('My Awesome Pie Chart')
plt.tight_layout()   # automatically gets some padding
plt.show()
