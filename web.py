import streamlit as st
import functionMain

todos = functionMain.get_todos()


def add_todo():
    selected_todo = st.session_state["new_todo"] + "\n"
    todos.append(selected_todo)
    functionMain.write_todos(todos)


st.title("My to-do App")
st.subheader("Created by @Gerard Do")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")