import streamlit as st
import fonctions

# Commentaire de Test
todos = fonctions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fonctions.write_todos(todos)


st.title("My Todo App")
st.subheader("C'est ma Todo Liste")
st.write("Une belle application")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fonctions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a Todo here ...",
              on_change=add_todo, key='new_todo')

