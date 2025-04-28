def get_number(number):
    """Function to get a valid number input from the user."""
    while True:
        number1 = input(f"Enter number {number}: ")
        try:
            return float(number1)
        except ValueError:
            print("Invalid number! Please enter a valid number.")
            
def get_operator():
    """Function to get a valid operator from the user."""
    while True:
        sign = input("Enter an operator (+, -, *, /): ").strip()
        if sign in ["+", "-", "*", "/"]:
            return sign
        else:
            print("Invalid operator! Please enter one of (+, -, *, /).")
    
def calculator():
    """Main calculator function to perform operations."""
    print("Welcome to the Calculator!")
    
    # Loop to allow multiple calculations
    while True:
        number1 = get_number(1)
        number2 = get_number(2)
        number3 = get_number(3)
        
        sign = get_operator()  # Get the operator
        
        result = 0
        if sign == "+":
            result = number1 + number2 + number3
        elif sign == "-":
            result = number1 - number2 - number3
        elif sign == "/":
            if number2 != 0 and number3 != 0:
                result = (number1 / number2) / number3
            elif number2 == 0 or number3 == 0:
                print("Error: Division by zero is not allowed.")
                continue  # Skip this operation and ask again
        elif sign == "*":
            result = number1 * number2 * number3
        
        print(f"The result of {number1} {sign} {number2} {sign} {number3} is: {result}")
        
        # Ask user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != "yes":
            print("Thank you for using the calculator! Goodbye!")
            break

calculator()