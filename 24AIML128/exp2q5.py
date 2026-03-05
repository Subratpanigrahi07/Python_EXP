student = {
    "name": "Subrat Panigrahi",
    "Age": 20,
    "Course": "CSE",
    "City": "Gunupur"
}

print("Dictionary data:")
print(student)

print("\nKeys in dictionary:")
print(student.keys())

print("\nValues in dictionary:")
print(student.values())

print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)