products = int( input("How many products did u have : "))
 
total_price = 0 
wtprice = 0


if products >= 3 :
   print("Congratulation you get discount offers ")
   for i in range (products) :
    price = int(input(f"Enter the price of product {i+1} : "))
    discount = float(input(f"Enter discount for product {i+1} : "))
    sum = price * discount / 100 
    fprice = price - sum
    print(f"Final price after {discount}% discount is {fprice} : ")
    
    total_price +=fprice



  
   print(f"Total price with discount {total_price}")



else :
 print("you didnt get any discount offer.If you want discount buy atleast 3 products ")
 for i in range (products) :
    price = int(input(f"No discount Enter the price of product {i+1} : "))
    wtprice+=price
    print(f"Final price without discount {wtprice} ")
    







    





