# program 1

# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for i in ids:
#     if '_' in i:
#         x = x + 1
# print(x)


# program 2

#
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for i in ids:
#     if '_' in i:
#         x = x + 1
# print(x)
#


# program 3

#
length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

# if perimeter in length < 14 and area in width < 8:
if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")

#
