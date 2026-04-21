"""
The Professions_dataset.xlsx file is from:
https://www.kaggle.com/datasets/zamamahmed211/professions-dataset

The code snippet below uses the pandas library to parse the file into a list called f
"""

import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

lst = []
f = pd.read_excel('Professions_dataset.xlsx')

first_column = f.iloc[:, 0]
lst_of_noun_professions = first_column.to_list()

print(lst_of_noun_professions)
