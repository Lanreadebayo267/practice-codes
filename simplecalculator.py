def calculator():
    print("Welcome to the Simple Calculator!")

    while True:
        operation = input("Choose operation (+, -, *, /): ")

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2

        print(f"Result: {num1} {operation} {num2} = {result}")

        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print(("Thanks for using the calculator. Goodbye!"))
            break

calculator()
    