import csv

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file))
    # print(file.read())
    # print(data)

# print(data)
# print(data[2:])
# print(data[1:])
city = input("Enter a city: ")

for row in data:
    # for row in data[1:]:
    # print(row)
    if row[0] == city:
        print(row[1])
