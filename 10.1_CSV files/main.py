
with open("people.csv", "r") as data:
    rows = data.read().splitlines()[1:]

for row in rows:
    row_data = row.split(",")
    print("{0} is {1} years old {2}.".format(row_data[0], row_data[1], row_data[2]))
