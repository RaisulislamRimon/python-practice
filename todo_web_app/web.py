import streamlit as st
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

x = st.slider("Select a value")
st.write(x, "squared is", x * x)

print(x)

# import streamlit as st
import functions

st.title('My Todo Web App')
st.subheader('This is my todo web app')
st.write('This app is to increase your productivity')
st.checkbox('Buy grocery')
st.checkbox('Throw the trash')

# function call for get_todos
todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

# st.text_input()
# st.text_input(label='')
# st.text_input(label='Enter a todo: ')
# st.text_input(label='Enter a todo: ', placeholder='Add new todo...')

print('hello')
