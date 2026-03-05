#WRITE A PROGRAM THAT FIND THE FARHENHIET FOR GIVEN CELSIOUS FROM THE LIST


celsius_list = [0, 20, 37, 100]

fahrenheit_list = [(c * 9/5) + 32 for c in celsius_list]

print("Celsius values:", celsius_list)
print("Fahrenheit values:", fahrenheit_list)