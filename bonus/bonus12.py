feet_inches = input("Enter feet and inches: ")


def convert(feet_and_inches):
    # parts = feet_inches
    parts = feet_and_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254

    # return feet, inches
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"
    return meters


# print(convert(feet_inches))
result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slides.")
