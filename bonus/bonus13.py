feet_inches = input("Enter feet and inches: ")

print('feet_inches', feet_inches)


# print(type(feet_inches))


# def parse(feet, inches):
def parse(feet_inches):
    # parts = feet_inches
    # parts = feet_and_inches.split(" ")
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    # return feet, inches
    return {"feet": feet, "inches": inches}  # python dictionary


# def convert(feet_and_inches):
def convert(feet, inches):
    # # parts = feet_inches
    # parts = feet_and_inches.split(" ")
    # feet = float(parts[0])
    # inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254

    # return feet, inches
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"
    return meters


# parse(feet_inches)['feet']
# parsed = parse(feet_inches)['feet']
parsed = parse(feet_inches)
# print('parsed', parsed)  # parsed {'feet': 3.0, 'inches': 10.0}

# print(convert(feet_inches))
# result = convert(feet_inches)
# result = convert(parsed['feet'], parsed['inches'])
result = convert(parsed['feet'], parsed['inches'])

# print(f"{feet} feet and {inches} is equal to {result}")
# print(f"{parse(feet_inches)['feet']} feet and {parse(feet_inches)['inches']} is equal to {result}")
print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slides.")
