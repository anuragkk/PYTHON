print("Welcome to calculator")


def calculator():
    calculation_is_on = True

    while calculation_is_on:
        # Convert inputs to numbers
        num_1 = float(input("Please enter a number:\n"))
        operation = input("Please select from +, -, *, %:\n")
        num_2 = float(input("Please enter another number:\n"))

        if operation == "+":
            result = num_1 + num_2
        elif operation == "-":
            result = num_1 - num_2
        elif operation == "*":
            result = num_1 * num_2
        elif operation == "%":
            result = num_1 % num_2
        else:
            print("Invalid operation selected.")
            continue

        print(f"The result is: {result}")

        choice = input(
            f"Type 'y' to continue calculating with this {result}, or 'n' to start over, or 'exit' to quit:\n").lower()
        if choice == "y":
            num_1 = result  # Start next round with previous result
        elif choice == "n":
            continue  # Restart the loop
        else:
            calculation_is_on = False
            print("Goodbye!")


calculator()
