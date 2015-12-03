# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 20:22:13 2015

@author: Matt
"""

http://soprweb.senate.gov/downloads/2015_1.zip
http://soprweb.senate.gov/downloads/2015_2.zip

lowest: http://soprweb.senate.gov/downloads/1999_1.zip

latest: http://soprweb.senate.gov/downloads/2015_4.zip


years = ('1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015')
counters = ('1','2','3','4')
print years
print counters


import requests, zipfile, StringIOd
from time import sleep

for year in years:
    for item in counters:
        string = 'http://soprweb.senate.gov/downloads/' + str(year) +'_' + str(item) + '.zip'
        print string
        r = requests.get(string)
        r.status_code
        z = zipfile.ZipFile(StringIO.StringIO(r.content))
        z.extractall()








for year in years:

for counter in range (1:5):
    print counter

print(range(1:5))


r = requests.get('http://soprweb.senate.gov/downloads/2015_1.zip')
r.status_code
r.open()
r.text


#this works to download and extract teh zip files....
import requests, zipfile, StringIO
r = requests.get('http://soprweb.senate.gov/downloads/2015_1.zip')
z = zipfile.ZipFile(StringIO.StringIO(r.content))
z.extractall()
# need to be able to read the xml files and write to a dataframe