import streamlit as st
import functionMain

todos = functionMain.get_todos()


def add_todo():
    selected_todo = st.session_state["new_todo"] + "\n"
    todos.append(selected_todo)
    functionMain.write_todos(todos)


st.title("My to-do App")
st.subheader("Created by @Gerard Do")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functionMain.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

