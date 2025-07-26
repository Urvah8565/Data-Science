friends = {
    "Darkyy" : {"age":25, "Phone":1235,"City":"Berlin" },
    "Thomas" : {"age":22, "Phone":1982,"City":"Munich" },
    "Warner" : {"age":28, "Phone":1653,"City":"Heidelberg " },
    "JACK" : {"age":28, "Phone":1655,"City":"Heidelberg " }
}

# Count the number of friends in each city
city_count = {}
for info in friends.values():
    city = info["City"]
    city_count[city] = city_count.get(city, 0) + 1

print(city_count)
# find = input("Enter the name of your friend : ")
# if find in friends :
#   print(friends[find])
# else :
#  print("No data found")

for name , info in friends.items() :
 print(f"Name-{name} - age-{info['age']}-Phone-{info['Phone']}-City - {info['City']} ")
#  for (info["City"]) in friends.items () :






# # for updating city
# friends["Thomas"]["City"] = "Tokyo" 

# # Add new frnd
# friends.update({"Steyn": {"age":30, "Phone":6325,"City":"New york"}})

# # dlt frnd
# friends.pop('Warner')

# for name , info in friends.items() :
#   if (info["City"]=="New york") :
#     print(f"{name} is from USA Rest are from Germany")
#   print(f"Name-{name} - age-{info['age']}-Phone-{info['Phone']}-City - {info['City']} ")
