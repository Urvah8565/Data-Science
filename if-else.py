# marks 
# marks = int(input("Enter your marks "))

# if marks > 90 :
#      print("Distinction")

# elif marks > 60 :
#      print ("First Class ")
# elif marks > 40 :
#      print("Second Class") 
# else : print("Fail")  
# ------- END --------

# ✅ Grade calculator with name input?

# name = input("Enter your name : ")
# grade = int(input("Enter your grade : "))

# if grade > 90  :
#     print(f"Congratulation {name} you score very well.Now you got A+/Distinction")
# elif grade > 75 :
#     print(f"Well Score {name} you score nice.You got A/First class")
# elif grade > 60 :
#     print(f"Nice work {name}.you got B/Second class ")
# elif grade > 50 :
#     print(f"Good score {name}.You got C/Pass")
# else :
#     print(f"Opps {name} you failed.try agian champ.\nnever give up {name} 👊\nI know you can do it even better ")
# |------END------|

# ✅ Age checker with voter eligibility?

# age = int(input("Enter your age : "))

# if age > 18 :
#     print("Great! You are eligible for voting")
# elif age >= 18 :
#     print("Give vote ")
# else :
#     print("You are not eligible for voting! Come when you become 18 years old")

#  |-----END-----|

# ✅ Simple login system?
correct_username = "Darkyy"
correct_password = "Iamdarkyy"
attempts = 3 

while attempts>0 :
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    if username== correct_username and password==correct_password: 
       print(f"Correct Password.Access gained✅ {username}")  
       break 
    elif username == "" or password == "" :
       print("Username or Password is empty")
       
    else:
         print("Incorrect username or password try again")
         attempts-=1  


    if attempts > 0  :
     print(f"{attempts} attempts left")
    else :


        print(f"Too many wrong attempts.Login failed")
     