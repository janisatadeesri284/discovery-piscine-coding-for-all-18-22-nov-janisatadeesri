number = input("Enter a number: ")

try:
    number = float(number)
    if number < 0:
        print("This number is negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
