# password = input("Enter new password: ")
# result = []
#
# if len(password) >= 8:
#     result.append(True)
# else:
#     result.append(False)
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
# result.append(digit)
#
# # print( 'digit check', password.isdigit())
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True
#
# result.append(uppercase)
#
# print(result)
# # print(all(result))
#
# # both are same
# # if all(result) == True:
# if all(result):
#     print("Strong password")
# else:
#     print("Weak password")
#


password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    # result.append(True)
    result["length"] = True
else:
    # result.append(False)
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
# result.append(digit)
result["digits"] = digit

# print( 'digit check', password.isdigit())

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

# result.append(uppercase)
result["upper-case"] = uppercase

print(result)
# print(all(result))

# both are same
# if all(result) == True:
if all(result.values()):
    print("Strong password")
else:
    print("Weak password")

print(result)
print(result.values())
print(all(result))
print(all(result.values()))
