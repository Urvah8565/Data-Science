task = int(input("How many tasks? "))

challenge = []
for i in range(task):
	taskname = str(input(f"Enter task {i+1} : "))
	challenge.append(taskname)
print(f"Your task list {challenge}")


# for sort list
sort = (input("Do you want to sort the list ? (yes/no) : ")).lower()
if sort == "yes" :
   challenge.sort()
   print(f"Sorted list is {challenge} ")

# for add any item 
add = (input("Do you want to add anything ? (yes/no) : " )).lower()
if add == "yes" :
 addit = input("Enter the task you want to add : " )
 challenge.append(addit)
 print(f"You add {addit} in {challenge}")
else :
 print("Ok")
# for remove any task
remove = (input("Do you want to remove anything ? (yes/no) : " )) .lower()
if remove == "yes" :
 removeit = input("Which task want to remove ")

 if removeit in challenge :
  challenge.remove(removeit)
  print(f"remian task  {challenge}")
 else : print(f"{removeit} is not found in list")
 print(f"Your task {challenge}")
else : 
     print(f"Current task  {challenge}")

