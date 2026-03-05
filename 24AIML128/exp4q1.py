# WRITE A PROGRAM THAT POINTS THE DECIMAL EQUIVALENT OF1/2,1/3,1/4....1/100

for i in range(2, 101):  
    decimal_value = 1 / i
    print(f"1/{i} = {decimal_value:.6f}")