# simple calculator for calculations

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error! Division by Zero."
    return a / b

def main():
    print("Simple calculator for the calculations.")
    print("a. Addition ")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")

    while True:
        operation = input("Enter your operations (a/b/c/d): ")

        if operation in ['a', 'b', 'c', 'd']:
            try:
                num1 = float(input("Enter your first number:"))
                num2 = float(input("Enter your second number:"))
            except ValueError:
                print("Invalid Input. Please enter numbers.")
                continue

            if operation == 'a':
                print(f"{num1} + {num2} = ",(addition(num1, num2)))
            elif operation == 'b':
                print(f"{num1} - {num2} = ",(subtraction(num1, num2)))
            elif operation == 'c':
                print(f"{num1} * {num2} = ",(multiplication(num1, num2)))
            elif operation == 'd':
                print(f"{num1} / {num2} = ",(division(num1, num2)))
        
        else:
            print("Invalid operation.")
        
        next_oper = input("Do you want to continue another calculation (yes/no)?: ")
        if next_oper.lower() != 'yes':
            break

if __name__ == "__main__":
    main()




