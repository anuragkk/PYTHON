def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}

print(operations["+"])


def cal():
    should_continue = True
    num_1 = float(input("what is the first number\n"))
    while should_continue:

        for symbol in operations:
            print(symbol)
        operation_symbol = input(f"pick an operation:\n")
        num_2 = float(input("what is your second number\n"))
        result = operations[operation_symbol](num_1, num_2)
        print(f"the result is {num_1} {operation_symbol} {num_2} = {result}")
        choice = input(f"do you like to continue your calculation with the {result}\n").lower()
        if choice == "y":
            num_1 = result

        elif choice == "n":
            cal()

        else:
            print("Tata")
            return


cal()
