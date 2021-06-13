with open("data.csv", "r") as data_file:
    data = data_file.read().splitlines()


for line in data:
    line_data = line.split(",")
    print("{0} is {1} years old and {2}.".format(line_data[0], line_data[1], line_data[2]))


# za split() napišeš V NOVO spremenljivko
