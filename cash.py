import cs50
import math
while True:
    num = cs50.get_float("Change Owed: ")
    if num > 0:
        break
    else:
        continue

num = num * 100
# number of quarters
numQ = math.floor(num/25) 
# print(f"Quarter:{numQ}")

# number of dimes
numD = math.floor((num % 25)/10) 
# print(f"Dime:{numD}")

# number of nickels
numN = math.floor(((num % 25) % 10)/5) 
# print(f"Nickel:{numN}")

# number of pennies
numP = math.floor(((num % 25) % 10) % 5) 
# print(f"Penny:{numP}")

total = numQ + numD + numN + numP

print(f"total:{total}")