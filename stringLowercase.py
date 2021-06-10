string = "Today Is A BeautiFul DAY"

print(string)
print(string.lower())



#CONVERT homework

print("Hello. This program converts kilometers into miles.")

repeat = None

while True:

    km = int(input("Enter number of kilometers: "))

    mi = km * 0.621371
    print("The value is " + str(mi) + "mi.")
    #print("The value is {0}mi." .format(mi))

    repeat = str(input('Do you want to do another conversion? Type "yes" or "no": '))

    if repeat.lower() != "yes":
        print("Thank you, goodbye.")
        break