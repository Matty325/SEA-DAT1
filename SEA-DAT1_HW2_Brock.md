Q1) Code:
mbrock@NA01495L MINGW64 /c/users/mbrock/desktop/githubclones/GA-SEA-DAT1 (master)
$ ls
02_git_github.pdf  code/  data/  homework/  new_file.md  notebooks/  other/  parked/  project/  README.md  slides/  syllabus.md

mbrock@NA01495L MINGW64 /c/users/mbrock/desktop/githubclones/GA-SEA-DAT1 (master)
$ cd data/

mbrock@NA01495L MINGW64 /c/users/mbrock/desktop/githubclones/GA-SEA-DAT1/data (master)
mbrock@NA01495L MINGW64 /c/users/mbrock/desktop/githubclones/GA-SEA-DAT1/data (master)
$ head chipotle.tsv
order_id        quantity        item_name       choice_description      item_price
1       1       Chips and Fresh Tomato Salsa    NULL    $2.39
1       1       Izze    [Clementine]    $3.39
1       1       Nantucket Nectar        [Apple] $3.39
1       1       Chips and Tomatillo-Green Chili Salsa   NULL    $2.39
2       2       Chicken Bowl    [Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]]      $16.98
3       1       Chicken Bowl    [Fresh Tomato Salsa (Mild), [Rice, Cheese, Sour Cream, Guacamole, Lettuce]]     $10.98
3       1       Side of Chips   NULL    $1.69
4       1       Steak Burrito   [Tomatillo Red Chili Salsa, [Fajita Vegetables, Black Beans, Pinto Beans, Cheese, Sour Cream, Guacamole, Lettuce]]  $11.75
4       1       Steak Soft Tacos        [Tomatillo Green Chili Salsa, [Pinto Beans, Cheese, Sour Cream, Lettuce]]       $9.25

mbrock@NA01495L MINGW64 /c/users/mbrock/desktop/githubclones/GA-SEA-DAT1/data (master)
$ tail chipotle.tsv







1831    1       Carnitas Bowl   [Fresh Tomato Salsa, [Fajita Vegetables, Rice, Black Beans, Cheese, Sour Cream, Lettuce]]       $9.25
1831    1       Chips   NULL    $2.15
1831    1       Bottled Water   NULL    $1.50
1832    1       Chicken Soft Tacos      [Fresh Tomato Salsa, [Rice, Cheese, Sour Cream]]        $8.75
1832    1       Chips and Guacamole     NULL    $4.45
1833    1       Steak Burrito   [Fresh Tomato Salsa, [Rice, Black Beans, Sour Cream, Cheese, Lettuce, Guacamole]]       $11.75
1833    1       Steak Burrito   [Fresh Tomato Salsa, [Rice, Sour Cream, Cheese, Lettuce, Guacamole]]    $11.75
1834    1       Chicken Salad Bowl      [Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Guacamole, Lettuce]]      $11.25
1834    1       Chicken Salad Bowl      [Fresh Tomato Salsa, [Fajita Vegetables, Lettuce]]      $8.75
1834    1       Chicken Salad Bowl      [Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Lettuce]] $8.75


Q1 Discussion:
This looks like a one-to-many table that represents orders by item. Each row represents an item, and a number of items in an order, a description of the item and its custom toppings (if applicable), as well as a subtotal price for the number of items on that line.  
The order number aggregates the order. E.g., the first four rows of data represent one order that had 4 items in order #1. Data row five represents order #2 which had two chicken bowls wiht same toppings, and the total price for two bowls of $16.98
the last thre rows represent the items that were in order 1834).

Q2: Discussion: Based on the last unique order ID of 1834, that suggests that there are 1834 order records in this file. 

Q3 Code:
mbrock@NA01495L MINGW64 /c/users/mbrock/desktop/githubclones/GA-SEA-DAT1/data (master)
$ wc -l chipotle.tsv
4623 chipotle.tsv

Q3 answer: There are a total of 4623 lines (including column headers)



Q4 code and answer:
USing grep piped to wc -l
Matt@Corvinius MINGW64 /c/users/Matt/githubclones/GA-SEA-DAT1/data (master)
$ grep "Steak Burrito" chipotle.tsv | wc -l
368

Matt@Corvinius MINGW64 /c/users/Matt/githubclones/GA-SEA-DAT1/data (master)
$ grep "Chicken Burrito" chipotle.tsv | wc -l
553

Based on count of orders with at least one order of steak burrito or chicken burrito, it seems that chicken burritos are more popular. 
(Technically if there were many orders of steak burritos with multiple quantities, counting number of lines may not be a valid approach. But an eyeball of the data suggests there are only a handful of orders that include more than one steak burrito.)


Q5 code and answer:
Matt@Corvinius MINGW64 /c/users/Matt/githubclones/GA-SEA-DAT1/data (master)
$ grep "Chicken Burrito" chipotle.tsv | grep "Black Beans" |  wc -l
282

Matt@Corvinius MINGW64 /c/users/Matt/githubclones/GA-SEA-DAT1/data (master)
$ grep "Chicken Burrito" chipotle.tsv | grep "Pinto Beans" | wc -l
105

Based on a line count of the occurrence of "Chicken Burrito" with "Black Beans" v. with "Pinto Beans", it seems that black beans are more popular.
Same limitation/caveat in the discussion of steak burritos applies here - though again there don't seem to be many orders with a multiple quantity of the same item for this menu item.
