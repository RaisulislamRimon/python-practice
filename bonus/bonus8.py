date = input("enter today's date: ")
mood = input('how is your mood(1 to 10): ')
thoughts = input('let your thoughts flow: \n')

# with open(f"folders/{date}.txt", "r") as file:
#     file = file.readlines()

with open(f"folders/{date}.txt", "w") as file:
    # file.write(mood + ' ')
    file.write(mood + 2 * "\n")
    file.write(thoughts)




# with open(f'files/{date}.txt', 'w') as file:
#     file.write(mood + 2 + '\n')
#     file.write(thoughts)






















