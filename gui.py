import PySimpleGUI as sg
import functionMain
from supportFont import addCharacter, removeCharacter
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")


todos_list = functionMain.get_todos()
refined_list = removeCharacter(todos_list)

list_box = sg.Listbox(values=refined_list, key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window(
    "To-do App", layout=[[label], 
                         [input_box, add_button], [list_box, edit_button, complete_button],
                         [exit_button]], 
                         font=("Helvetica", 20))


while True: 
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functionMain.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functionMain.write_todos(todos)
            refined_todos = removeCharacter(todos)
            window["todos"].update(values=refined_todos)
        
        case "Edit":
            todo_to_edit= values["todos"][0] 
            new_todo = values["todo"] 
            todos = functionMain.get_todos()
            refined_todos = removeCharacter(todos)
            index = refined_todos.index(todo_to_edit)
            refined_todos[index] = new_todo
            txt_file_list = addCharacter(refined_todos)
            functionMain.write_todos(txt_file_list)
            window["todos"].update(values=refined_todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])


        case "Complete":
            todo_to_complete = values["todos"][0] + "\n"
            todos = functionMain.get_todos()
            todos.remove(todo_to_complete)
            refined_todos = removeCharacter(todos)
            txt_file_list = addCharacter(refined_todos)
            functionMain.write_todos(txt_file_list)
            window["todos"].update(values=refined_todos)
            window["todo"].update(value="")      

        case "Exit":
            break
        
        case sg.WIN_CLOSED:
            break

window.close()