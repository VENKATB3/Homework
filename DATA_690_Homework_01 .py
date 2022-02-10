# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:55:20 2022

@author: SUMANTH TEJA
"""

import requests
import re

url = 'https://www.gutenberg.org/files/2600/2600-0.txt'
r = requests.get(url, allow_redirects=True)
filename = "warpeace.txt"
open(filename, 'wb').write(r.content)
 
text_file = open(filename, 'r')
text = text_file.read()
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

unique = []
for word in words:
    if word not in unique:
        unique.append(word)
print(len(unique))