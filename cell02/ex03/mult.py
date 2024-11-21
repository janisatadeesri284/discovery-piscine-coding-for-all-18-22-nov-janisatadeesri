num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:

    num1 = float(num1)
    num2 = float(num2)
    
    result = num1 * num2

    if result > 0:
        print("The result of multiplying the two numbers is positive.")
    elif result < 0:
        print("The result of multiplying the two numbers is negative.")
    else:
        print("The result of multiplying the two numbers is zero.")

    
    print(f"The result of the multiplication is: {result}")

except ValueError:
   
    print("Invalid input. Please enter valid numbers.")
