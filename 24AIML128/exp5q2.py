#WRUTE A PROGTRAM THAT LOOPS OVER A SEQUENCE OF ELEMENTS OF A LIST TOUPLE , DISCIMORAY AND SET

my_list = [10, 20, 30, 40]
print("Looping over a List:")
for item in my_list:
    print(item)

my_tuple = ("apple", "banana", "cherry")
print("\nLooping over a Tuple:")
for fruit in my_tuple:
    print(fruit)

my_dict = {"name": "Alice", "age": 25, "city": "Odisha"}
print("\nLooping over a Dictionary (keys and values):")
for key, value in my_dict.items():
    print(key, ":", value)

my_set = {1, 2, 3, 4, 5}
print("\nLooping over a Set:")
for num in my_set:
    print(num)