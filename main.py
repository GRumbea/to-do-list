import streamlit as st
import functions as func

todos = func.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + '\n'
    todos.append(todo_local)
    func.write_todos(todos)


st.title("My To-Do List")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.write("")
st.write("")
st.text_input(label="Enter a To-Do: ", placeholder="Add a new todo...", on_change=add_todo, key='new_todo')

