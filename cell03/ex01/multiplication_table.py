user_input = input("Enter a number to display its multiplication table: ")

try:
    
    number = int(user_input)
    
    
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
except ValueError:
    
    print("Invalid input. Please enter a valid number.")
