my_list = ["Darkyy", "Starc",5646,4.566]

my_list.append("Starc")
print(len(my_list))
print(my_list)

my_tuple = (1,2,3,4,5)

my_tuple += (6, 7, 8)  # Tuples are immutable, so we create a new tuple
two = my_tuple[6]
print(two)
print(len(my_tuple))

my_list.reverse()
print(my_list)


print(my_list.index("Darkyy"))
