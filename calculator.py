a = int(input("Input first number: "))
b = int(input("Input second number: "))
operation = str(input("Enter an arithmetic: ('+', '-', '*' or '/') "))

if operation == "+":
    print(a + b)

elif operation == "-":
    print(a - b)

elif operation == "*":
    print(a * b)

else:
    print(a / b)