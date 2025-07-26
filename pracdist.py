
marks = {
    "Harry" : 90 ,
    "Carry" : 80 ,
    "Marry" : 50 
}
print(marks)
marks.update({"Marry":85,"Darry":65})

marks.pop("Carry")
 
print(marks.items())

for i in marks  :
    print(i , "->", marks[i])
