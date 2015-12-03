# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:44:59 2015

@author: Matt
"""

# code to pull schedule a info 

#https://api.open.fec.gov/v1/schedules/schedule_a/?sort_nulls_large=true&api_key=DEMO_KEY&min_date=1%2F1%2F2000&per_page=20

#small scale
import pandas as pd
import requests
from time import sleep


df_scheda = {}
df_temp = {}
url1= 'https://api.open.fec.gov/v1/schedules/schedule_a/?sort_nulls_large=true'
url2= '&api_key=I5jb0yjnhFSfWu8TKedfYySWSuHQnsnabBT63qar&min_date=1%2F1%2F2005&per_page=20'
lastindex = 0
recordcount = 0

for count in range (1, 50):
    if count == 1:
        r = requests.get(url1 + url2)
        d = r.json()['results']
        df_scheda = pd.DataFrame.from_dict(d, orient = 'columns')
        lastindex = r.json()['pagination']['last_indexes']['last_index']
        recordcount += len(d)
        print(recordcount)
        print(lastindex)
        print(df_scheda)
    else:
        print(lastindex)
        print(url1 + url2 + 'last_index=' + str(lastindex))
        r = requests.get(url1 + url2 + '&last_index=' + str(lastindex))     
        r.text
        r.status_code
        d_temp = r.json()['results']
        df_temp = pd.DataFrame.from_dict(d_temp, orient = 'columns')
        df_scheda = df_scheda.append(df_temp)
        lastindex = r.json()['pagination']['last_indexes']['last_index']
        print(lastindex)
        print(df_temp)
        print(df_scheda)
    sleep(4)
 
df_scheda.set_index('committee_id', inplace=True) 
print df_scheda    
df_scheda.shape
df_scheda.dtypes

df_scheda.to_csv('sample_scheda.csv')    





# view the raw response text
r.text
r.json()
# decode the JSON response body into a dictionary
jstring = r.json()
type(jstring)
type(jstring['results'])
len(jstring['results'])
d = jstring['results']
df = pd.DataFrame.from_dict(d, orient = 'columns')
df.to_csv('test_schedule_a.csv') 
jstring['last_indexes']['last_index']  
jstring['api_version'] 

# this code helps find the last index.  last index will need to be passed iteratively to the query script, in order to pull hte next set of records
#To fetch the next page of results, append "last_index=230880619&last_contribution_receipt_date=2014-01-01" to the URL.
jstring['pagination']['last_indexes']['last_index']
jstring['pagination']['last_indexes']['last_contribution_receipt_date']
jstring['pagination']['last_indexes']








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
