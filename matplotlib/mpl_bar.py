from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

# We want to create a bar chart of the most popular languages from a csv

plt.style.use('fivethirtyeight')
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most Popular Languages')

plt.xlabel('No. of Users')
# plt.ylabel('')
plt.grid(color='g')
plt.tight_layout()
plt.show()
