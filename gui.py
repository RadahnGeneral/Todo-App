import PySimpleGUI as sg
import functionMain
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")

def removeCharacter(list):
    new_list =[]
    for item in list:
        new_list.append(item.replace("\n",""))
    return new_list
todos_list = functionMain.get_todos()
refined_list = removeCharacter(todos_list)

list_box = sg.Listbox(values=todos_list, key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window(
    "To-do App", layout=[[label], 
                         [input_box, add_button], [list_box, edit_button]], 
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
            window["todos"].update(values=todos)
        case sg.WIN_CLOSED:
            break
        case "Edit":
            todo_to_edit= values["todos"][0] 
            new_todo = values["todo"] 

            todos = functionMain.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functionMain.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])

window.close()