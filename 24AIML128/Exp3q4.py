#ACCEPT A DIGIT WITHINN0 TO 6 AND DISPLAY THE WEEK BY SUCH AS : 0 FOR SUNDAY 1 FOR MONDAY ETC 

# Program to accept a digit (0–6) and display the weekday

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("0: Sunday, 1: Monday, 2: Tuesday, 3: Wednesday, 4: Thursday, 5: Friday, 6: Saturday")

try:
    num = int(input("Enter a digit (0–6): "))
    if 0 <= num <= 6:
        print("Day is:", weekdays[num])
    else:
        print("Invalid input! Please enter a number between 0 and 6.")
except ValueError:
    print("Invalid input! Please enter a digit.")