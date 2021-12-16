"""
Assignment 11 Tristan Torgersen
"""

import json, re
with open('/Users/tristan/Downloads/yelp_AZ_2018.txt', encoding='utf-8') as fin:
    for review in fin:
        matches1 = re.findall(r'!+', review, flags=re.I)
        matches2 = re.findall(r'\b[A-Z]+\b', review)
        num_matches1 = len(matches1)
        num_matches2 = len(matches2)

        print(matches1)
        print("----------")
        print(matches2)