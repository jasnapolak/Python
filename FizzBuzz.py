number = int(input("Enter a number between 1 and 100: "))

for x in range(1, number +1):
    if (x % 3) == 0 and (x % 5) == 0:
        x = "fizzbuzz"

    elif (x % 5) == 0:
        x = "buzz"

    elif (x % 3) == 0:
        x = "fizz"

    print(x)