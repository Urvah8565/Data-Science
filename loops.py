# # 1 -----Bill Splitter-----

# bill = int(input("whats your total bill : "))
# people = int(input("How many peoples are there "))

# split = (input(f"Did you want to split bill with {people} peoples (yes/no ): ")).lower()  

# if split == "yes" :
#     divide = bill / people 
#     print (f"Each person should pay Rs {divide}")

# else :
#     print(f"You need pay the full bill of Rs {bill}")
# # ----End----

# 2 Simple Shopping Cart

totalprice = 0 

items = int(input("How many items did you bought "))
for i in range (items) :
 price = int (input(f"Enter the price of item {i+1} "))

 totalprice+=price

print(f"Total price of your items {totalprice}")
# -----END-----

# 3 Even or Odd Counter
# even_count = 0
# odd_count = 0


# for i in range (5) :
 
#  num = int(input(f"Enter the number {i+1}  : "))

#  if num % 2 == 0 :
#         print(f"{num} is Even number")
#         even_count+=1
#  else :
#         print(f"{num} is Odd number")
#         odd_count+=1


# print(f"{even_count} : Even numbers")   
# print(f"{odd_count} : Odd numbers")     
# =====END=====

import random 


attempts = 3 
secret = random.randint (1,10)
while attempts > 0 :
 guess = int(input("Enter the number between 1 to 10 "))


 if guess > secret :
    print("Too high")
 elif  guess < secret :
    print("Too low")

 else :
    print("Correct number")
    break
 attempts -=1 

 if attempts > 0 :
   print (f"{attempts} attempts left")
 else :
   print("Invalid numbers ")    

print(f"The correct number was {secret}")