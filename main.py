number = int(input("Which number do you want to check? "))

even_odd_calculation = number % 2 

if even_odd_calculation == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")