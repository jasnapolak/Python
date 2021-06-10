print("Hello. This program converts kilometers into miles.")

repeat = None

while True:

    km = int(input("Enter number of kilometers: "))

    mi = km * 0.621371
    print(mi)

    repeat = str(input('Do you want to do another conversion? Type "yes" or "no": '))

    if repeat != "yes":
        print("Thank you, goodbye.")
        break

