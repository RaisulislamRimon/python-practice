password = input("Enter new password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

# print( 'digit check', password.isdigit())

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

print(result)