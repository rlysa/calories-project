# before using you need install bs4 and lxml

from bs4 import BeautifulSoup
import requests

import json

src1 = requests.get('https://calorizator.ru/product').text


soup1 = BeautifulSoup(src1, 'lxml').find_all('li')
category = []
for i in soup1:
    i = str(i)
    if f'<a href="product/' in i:
        i = i[i.find('href="') + 14:]
        category.append(i[:i.find('">')])

dictionary = {}
category = category
for i in category:
    src2 = requests.get(f'https://calorizator.ru/product/{i}').text
    soup2 = BeautifulSoup(src2, 'lxml').find_all('tbody')
    name, kkal, protein, carbohydrates, fats = [], [], [], [], []
    for j in soup2:
        for l in j:
            l = str(l)
            l = l[l.find('<a href="/product/'):]
            l = l[l.find('>') + 1:]
            l1 = l[:l.find('<')]
            if l1 != '':
                name.append(l1)
            l = l[l.find('protein-value'):]
            l = l[l.find('>') + 2:]
            l2 = l[:l.find(' <')]
            if l2 != '' and l2.isdigit():
                protein.append(float(l2))
            else:
                protein.append(float(0))
            l = l[l.find('fat-value'):]
            l = l[l.find('>') + 2:]
            l3 = l[:l.find(' <')]
            if l3 != '' and l3.isdigit():
                fats.append(float(l3))
            else:
                fats.append(float(0))
            l = l[l.find('carbohydrate-value'):]
            l = l[l.find('>') + 2:]
            l4 = l[:l.find(' <')]
            if l4 != '' and l4.isdigit():
                carbohydrates.append(float(l4))
            else:
                carbohydrates.append(float(0))
            l = l[l.find('kcal-value'):]
            l = l[l.find('>') + 2:]
            l5 = l[:l.find(' <')]
            if l5 != '' and l5.isdigit():
                kkal.append(float(l5))
            else:
                kkal.append(float(0))
    dictionary[i] = []
    for j in range(len(name)):
        n = name[j]
        dictionary[i].append({
            'name': str(name[j]),
            'kkal': kkal[j],
            'protein': protein[j],
             'carbohydrates': carbohydrates[j],
            'fats': fats[j]
        })

js = json.dumps(dictionary, indent=4)
with open('kkal.json', 'w') as file:
    file.write(js)
