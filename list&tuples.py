# list 
frnds = ["Bob","Darkyy","Starc",5,3.50,False]
frnds[2] = "Mitchell"
print(frnds)

frnds.append("Anderson")
print(frnds)

frnds.remove("Mitchell")
print(frnds)

l1 = [5 ,4,6,3,1,2]
l1.sort()
print(l1)

frnds.insert(1, "NewFriend")
print(frnds) 

frnds.pop(2)
print(frnds)
 
frnds.reverse()
print(frnds)

count_str = 0 
count_int = 0
for i in frnds:
    if type(i) == str :
        count_str +=1 
    elif type(i) == int :
        count_int+=1
print(f"The number of string in a frnd list are  : {count_str}")
print(f"The number of int in a frnd list are  : {count_int}")

# tuples
a = (2,3,4,5,6,7,7,7)
print(a.count(7))

print(a.index(3))
