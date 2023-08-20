# search on Google anything

import webbrowser

# user_term = input("Enter a search Term: ")
user_term = input("Enter a search Term: ").replace(' ', '+')

# webbrowser.open("https://www.google.com")
# webbrowser.open('https://www.google.com/search?q=hello')
# webbrowser.open(f"https://www.google.com/search?q={user_term}")
webbrowser.open('https://www.google.com/search?q=' + user_term)
