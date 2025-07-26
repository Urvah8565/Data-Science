# students = {
#     "Darkyy": {"age": 19, "subject": "Math"},
#     "Thomas": {"age": 20, "subject": "Physics"},
#     "Lena": {"age": 21, "subject": "Biology"},
#     "Ella": {"age": 22, "subject": "Math"}
# }

# liked = input("Enter the subject that student like the most : ")
# totalsub = 0 
# for name,info in students.items() :
#      if liked == (info["subject"])  :
#           print(f"{name} like {liked}")
#           totalsub+=1
     
# if totalsub == 0 :
#      print("Not found")
# print(f"Total students in {liked} are {totalsub}")

# fav_fruits = {
#     "Darkyy": "Mango",
#     "Lena": "Strawberry",
#     "Thomas": "Banana"
# }
# name = input("Enter friends name : ")

# fav = fav_fruits.get(name)

# if fav :
#     print(f"{name}'s fav fruit is {fav}")
# else :
#     print("Not found")




# contacts = {
#     "Darkyy": {"phone": "1234567890", "email": "darkyy@example.com"},
#     "Lena": {"phone": "9876543210", "email": "lena@example.com"},
#     "Thomas": {"phone": "5556667777", "email": "thomas@example.com"}
# }

# def show_contact () :
#     show = input("Enter the name : ")
#     find = contacts.get(show) 
#     if find :
#         print(f"Name - {show} - Phone - {find['phone']} - Email -  {find['email']} ")
        
        
#     else :
#         print("No data found")    
#     return show 

# a = show_contact()
# print(a)


contacts = {
    "Darkyy": "1234567890",
    "Leena": "9876543210"
}

while(True) :
 ask = input("Enter what did you want to do ? add/update/delete/view/exit :  ")
# For add 
 if ask.lower() == "add" :
    a = input("Enter name : ")
    b = input("Enter Number : ")
    contacts[a] = b
    print(contacts)
# For update 
 elif ask.lower() == "update" :
    a = input("Enter name for update : ")
    b = input("Enter Number for update : ")
    contacts[a] = b
# For delete 
 elif ask.lower() == "delete" :   
    dlt = input("Enter the name to delete : ")
    if dlt in contacts :
      del contacts [dlt]
      print(f"{dlt} deleted")
      print(contacts)
    else : print(f"No {dlt} found in contacts")
       
      
# For View 
 elif ask.lower() == "view" :
    name = input("Enter the name to view : ")
    view = contacts.get(name)
    if view :
      print(f" {name} → {contacts[name]}")
    else :
     print(f"NO! {name} found in contact")


 elif ask.lower() == "exit" :
   print(contacts)
   print("Good bye!")
   break


 
    
 

 

     
            