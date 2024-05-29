import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re

page = requests.get("https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787", verify=False)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', id="table_id")
headers = []

for i in table.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns=headers)

for j in table.find_all('tr')[1:]:
    print('--')
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(df)
    df.loc[length] = row

# with open('test.html', 'w') as f:
#     f.write(str(page.content))
# print(table)

# scripts = BeautifulSoup(page.content, 'lxml').find_all('script', {'type': 'text/javascript'})
# print(scripts)

# table_data = json.loads(
#     re.search(r"var datasource = ({.*})", scripts[-5].string).group(1),
# )

# # with open('test.html', 'w') as f:
# #     f.write(str(scripts))
# print(scripts[-5])

