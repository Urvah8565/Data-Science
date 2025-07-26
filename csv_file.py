# import csv  # 1️⃣ Import the CSV module

# # 2️⃣ Get user input
# name = input("Enter student name: ")
# marks = input("Enter marks: ")

# # 3️⃣ Open CSV file in append mode
# with open("student_data.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, marks])  # 4️⃣ Write data as a row

# print("✅ Student data saved into student_data.csv")

# # 5️⃣ Read and show the data
# print("\n📄 Saved Student Data:")
# with open("student_data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[0], "-", row[1])

import pandas as pd  # 1️⃣ Import Pandas

# 2️⃣ Read the CSV file
df = pd.read_csv("student_data.csv", header=None, names=["Name", "Marks"])

# 3️⃣ Show the full data
print("\n📄 Full Data:")
print(df)

# 4️⃣ Find total students
print("\n👥 Total students:", len(df))

# 5️⃣ Show top scorer
topper = df[df["Marks"] == df["Marks"].max()]
print("\n🏆 Topper:")
print(topper)

# 6️⃣ Show average marks
print("\n📊 Average Marks:", df["Marks"].mean())

# 7️⃣ Show sorted by marks
print("\n🔢 Sorted by Marks:")
print(df.sort_values("Marks", ascending=False))
