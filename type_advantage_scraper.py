import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send an HTTP request to the website and retrieve the HTML
html = requests.get('https://www.polygon.com/pokemon-go-guide/22554033/type-chart-strengths-weaknesses-super-effective')

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html.text, 'html.parser')
rows = soup.find_all('td')

#appending information into list
list = []
for i in rows:
    if i:
        list.append(i.text.strip())

#print(list)


#Create an empty list to store the sublists
sublists = []

# Use the slice() method to create sublists of every 3 indices
for i in range(0, len(list), 3):
    sublist = list[i:i+3]
    sublists.append(sublist)

#print(sublists)

pokemon_weak_strong = pd.DataFrame(sublists)
pokemon_weak_strong.columns = ['Type', 'Strength', 'Weakness']
#pokemon_weak_strong.to_csv('Strength_weakness.csv')
#print(pokemon_weak_strong)