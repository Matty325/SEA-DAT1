# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 15:34:53 2015

@author: Matt
"""

'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

#[your code here]
import csv
with open('chipotle.tsv', mode ='rU') as tsvin:
    file_nested_list = [row for row in csv.reader(tsvin, delimiter= '\t')]
  
    
'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

#[your code here]
header = file_nested_list[0]
data = file_nested_list[1:]

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!  Break the problem into steps and then code each step
'''

#[your code here]
from re import sub
from decimal import Decimal
group_item_count = 0
group_sum_item_price = 0

for item in data:
    item_count = int(item[1])
    item_price = Decimal(sub(r'[^\d.]', '', item[4]))
    group_item_count += item_count
    group_sum_item_price += item_price

avg_price = round((group_sum_item_price / group_item_count),2)
print(group_item_count)
print(group_sum_item_price)
print(avg_price)

##avg price per order = $6.94.
    

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
#[your code here]
sodas = []
for item in data:
    if "Canned" in item[2] and item[3] not in sodas:
        sodas.append(item[3])
print sodas

## sodas = ['[Sprite]', '[Dr. Pepper]', '[Mountain Dew]', '[Diet Dr. Pepper]', '[Coca Cola]', '[Diet Coke]', '[Coke]', '[Lemonade]', '[Nestea]']

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

#[your code here]
totaltoppingcount=0
recordcount=0
for item in data:
    if "Burrito" in item[2]:
        recordcount +=1
        totaltoppingcount += item[3].count(',')+1
print totaltoppingcount 
print type(totaltoppingcount)          
print recordcount
print type(recordcount)
avgtoppings = float(totaltoppingcount)/float(recordcount)
print avgtoppings
print type(avgtoppings)

## avvg count of toppings for burritos is 5.395. I got this counting the number of commas for each buritto item and adding one to that total, since the number of commas in the list is one less than the count of items

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

#[your code here]
chips = []
for item in data:
    if "Chips" in item[2] and item[2] not in chips:
        chips.append(item[2])

chip_sums = {}
for item in data:
    key = item[2]
    itemtotal = int(item[1])
    if key in chips:
        chip_sums[key] = chip_sums.get(key, 0)+itemtotal
print(chips, chip_sums)

## Chip_sums (dictionary of unique chip types and total count of that order type):
##{'Chips and Roasted Chili-Corn Salsa': 18, 'Chips and Tomatillo-Red Chili Salsa': 25, 'Chips and Mild Fresh Tomato Salsa': 1, 'Chips and Guacamole': 506, 'Chips and Fresh Tomato Salsa': 130, 'Chips and Tomatillo Red Chili Salsa': 50, 'Chips and Tomatillo-Green Chili Salsa': 33, 'Side of Chips': 110, 'Chips and Roasted Chili Corn Salsa': 23, 'Chips': 230, 'Chips and Tomatillo Green Chili Salsa': 45}
        

'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''

#[your code here]
