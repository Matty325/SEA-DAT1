# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:02:47 2015

@author: Matt
"""





#final code to pull complete committees table from api.open.fec.gov
import pandas as pd
import requests
from time import sleep

df = {}
url_part1 = "https://api.open.fec.gov/v1/committees/?sort=name&sort_nulls_large=true&page="
url_part3 = "&per_page=100&api_key=I5jb0yjnhFSfWu8TKedfYySWSuHQnsnabBT63qar"
for count in range (1, 539):
    if count == 1:
        r = requests.get(url_part1 + str(count) + url_part3)
        d = r.json()['results']
        df = pd.DataFrame.from_dict(d, orient = 'columns')
        print(df)
    else:
        print(df)       
        r = requests.get(url_part1 + str(count) + url_part3)
        d_temp = r.json()['results']
        df_temp = pd.DataFrame.from_dict(d_temp, orient = 'columns')
        df = df.append(df_temp)
        print(df_temp)
        print(df)
    sleep(4)
 
df.set_index('committee_id', inplace=True) 
print df    
df.shape
df.to_csv('committee_table.csv')    





''' test code/working code to build up to final 
url_part1 = "http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:"
url_part3 = "&LAN=625"
for count in range(1, 52):
    if count == 1:
        r = requests.get(url_part1 + str(count) + url_part3)      
        header = r.json()[0]
        body = r.json()[1:]
        data = pd.DataFrame(body, columns=header)
    else:
        if count not in [3, 7, 14, 43, 52 ]:
            r = requests.get(url_part1 + str(count) + url_part3)      
            header = r.json()[0]
            body = r.json()[1:]
            data_temp = pd.DataFrame(body, columns=header)
            data_temp.tail(10)
            data = data.append(data_temp)
            data.tail(47)
            data.shape
print (data)
 

import pandas as pd
import requests
from time import sleep

r = requests.get('https://api.open.fec.gov/v1/committees/?sort=name&sort_nulls_large=true&page=1&per_page=1&api_key=I5jb0yjnhFSfWu8TKedfYySWSuHQnsnabBT63qar')
#df = pd.read_json('https://api.open.fec.gov/v1/committees/?sort=name&sort_nulls_large=true&page=1&per_page=5&api_key=I5jb0yjnhFSfWu8TKedfYySWSuHQnsnabBT63qar')

#https://api.data.gov/nrel/alt-fuel-stations/v1/nearest.json?api_key=I5jb0yjnhFSfWu8TKedfYySWSuHQnsnabBT63qar&location=Denver+CO

# check the status: 200 means success, 4xx means error
r.status_code

# view the raw response text
r.text
r.json()
# decode the JSON response body into a dictionary
jstring = r.json()
type(jstring)
type(jstring['results'])
d = r.json()['results']
d2 = jstring['results']
df2 = pd.DataFrame.from_dict(d, orient='columns')
df.shape
df.dtypes
df.index
df.describe(include='all')

jstring['results']['candidate_ids']
data = pd.read_json(jstring['results'])
'''
