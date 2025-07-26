marks = {
    "Darkyy" : 90 ,
    "Harry" : 23 ,
    "Master" : 56

}
print(marks, type(marks))
print(marks["Darkyy"])

print(marks.keys())
print(marks.values())
marks.update({"Master": 55, "Peter": 65}) 
print(marks)
print(marks["Master"])

print(marks.get("Darkyy1"))

print(marks.clear())