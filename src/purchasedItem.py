import math
purchasedItem = {}
x = 0
y = 0
itemSum = 0

print("Please enter the number of items that you have purchased: ")
totalItemNumber = int(input())

while x < totalItemNumber:
    x = x + 1
    print("Please enter the price of item %i:" % x)
    purchasedItem[x] = float(input())

for y in purchasedItem:
   itemSum = itemSum + purchasedItem[y]
   y = y + 1

print(float(itemSum))