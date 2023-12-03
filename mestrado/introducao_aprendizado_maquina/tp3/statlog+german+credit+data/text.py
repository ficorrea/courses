# a = []
# with open('german.data-numeric') as file:
#     for i in file.readlines():
#          print(i.strip().replace(' ', ',').replace(',,,', ','))

import pandas as pd
pd.read_csv('german.csv')

