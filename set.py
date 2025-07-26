# # players = {"Starc", "Darkyy","Starc", "Anderson", "Bumrah","Jhonson","Smith"}




# # players.add ("Brett lee")
# # print(players)

# # players.remove("Starc")
# # print(players)

# # players.discard("jACA")
# # print(players)

# # opponents = {"Viv richard","Brain Lara","Curtly ambrose","Anderson","Smith"}

# # allplyers = players.union(opponents)
# # print(allplyers)

# # allplyers = players.intersection(opponents)
# # print(allplyers)


# # aset = {"User1","User2","User3","User4"}
# # bset = {"User2","User3","User4"}

# # difference = aset.difference(bset)
# # print(difference)



# # java_students = {"Darkyy","James","Soul","Bob","elison"}
# # python_students = {"Darkyy","Nora","Rix","Buzz","Bob"}

# # all_students = java_students.union(python_students) 
# # print(f"Unique students {all_students}")

# # inBoth = python_students.intersection(java_students)
# # print(f"Both courses {inBoth}")


# # onlypy = python_students.difference(java_students)
# # print(f"Python students {onlypy}")

# # onlyjava = java_students.difference(python_students)
# # print(f"Java students {onlyjava}")

# a = (90,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) 
# print(a.count(0))


# team_A = {"Darkyy", "Bumrah", "Starc", "Anderson"}
# team_B = {"Anderson", "Smith", "Starc", "Lee"}

# unique = team_A.union(team_B) 
# print(unique)

# inBoth = team_A.intersection(team_B)
# print(inBoth)

# onlyA = team_A.difference(team_B)
# print(onlyA)

# onlyB = team_B.difference(team_A)
# print(onlyB)

# newP = team_A.add("Shami")
# print(team_A)

# removeP = team_B.remove("Smith")
# print(team_B)



# report = {
#     "Darkyy": 91,
#     "Rix": 76,
#     "Buzz": 65
# }

# report.update({"Ali":84,"Buzz":75})

# report.pop("Rix")
# print(report)

# for i in report :
#     print(f" {i} got {report[i]} marks ")



# ==========new==========
# report = {
#     "Darkyy": {"marks": 91, "email": "darkyy@gmail.com", "course": "Python"},
#     "Ali": {"marks": 84, "email": "ali@gmail.com", "course": "Java"},
#     "Buzz": {"marks": 75, "email": "buzz@gmail.com", "course": "Python"}
# }

# report.update({"Rix":{"marks":81, "email":"rix@gmail.com","course":"JavaScript"}})
# report.update({"Buzz":{"marks":78, "email":"buzz@gmail.com","course":"Python"}})

# # for name , info in report.items() :
# #     print(f"{name} got {info['marks']} marks in {info['course']} - {info['email']}  ") 


# for  name , info   in report.items()  :
#  if info["marks"] > 80 :
#   print(f"{name} scored {info['marks']}")
# ==========end===============



report = {
    "Darkyy": {"marks": 91},
    "Ali": {"marks": 84},
    "Buzz": {"marks": 75},
    "Rix": {"marks": 61},
    "Nora": {"marks": 45}
}

for name , info in report.items() :
  if info['marks'] > 90 :
    print(f"{name} got {info['marks']} marks | Grade A+")
  elif info['marks'] > 80  :
    print(f"{name} got {info['marks']} marks | Grade A") 
  elif info['marks'] > 70 :
    print(f"{name} got {info['marks']} marks | Grade B")
  elif info['marks'] > 60 :
    print(f"{name} got {info['marks']} marks | Grade C")
  else :
    print(f"{name} got {info['marks']} marks |  fail ")    