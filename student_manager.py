# Student Marks Program

# Ask for student name and marks
name = input("Enter student name: ")
marks = input("Enter marks: ")

# Save the data into a file
with open("student_data.txt", "a") as file:
    file.write(name + " - " + marks + "\n")

print("✅ Student data saved successfully!")

# Show all saved data from the file
print("\n Saved Student Marks:")
with open("student_data.txt", "r") as file:
    for line in file:
        print(line.strip())
