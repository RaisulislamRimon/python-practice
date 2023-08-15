waiting_list = ['sen', 'ben', 'john']
# sorting the list in ascending order
# waiting_list.sort()
# sorting the list in descending order
waiting_list.sort(reverse=True)

# print(waiting_list) # ['sen', 'ben', 'john']
for index, data in enumerate(waiting_list):
    row = f"{index + 1}. {data.capitalize()}"
    print(row)