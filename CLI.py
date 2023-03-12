from modules.functionMain import get_todos, write_todos
# import functionMain
import time

now = time.strftime("%b %d, %Y - %H:%M:%S")
print("It is ", now)
while True:
    todos = get_todos()
    user_action = input("Please type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        user_todo = user_action[4:] + "\n"
        todos.append(user_todo)

       
        write_todos(todos, "files/todos.txt")

        print(" ")
        print("-" * 30)
        print(" ")
    
    elif user_action.startswith("show"):
       

        print(" ")
        for index, value in enumerate(todos):
            value = value.strip("\n")
            print(f"{index+1}. {value}")

        print(" ")
        print("-" * 30)
        print(" ")

    elif user_action.startswith("edit"):
        try:
            chosenNumber = int(user_action[5:])
            chosenNumber = chosenNumber - 1

            new_todo = input("Please enter a new todo: ")
            todos[chosenNumber] = new_todo + "\n"

            write_todos(todos, "files/todos.txt")

            print("The todo list has been updated")

            print(" ")
            print("-" * 30)
            print(" ")
        except ValueError:
            print("")
            print("Your command is invalid, please try again!")
            continue


    elif user_action.startswith("complete"):
        try: 
            chosenNumber = int(input("Please enter the number of todo to mark as completed: "))
            chosenTodo = todos[chosenNumber - 1].strip("\n")
            todos.pop(chosenNumber - 1)

            write_todos(todos, "files/todos.txt")


            print(" ")
            print("-" * 30)
            print(f"{chosenTodo} has been removed from the list")
            print("-" * 30)
            print(" ")
        except IndexError:
            print("There is no item with that number, please try again")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("*******Error*******")
        print("You entered an unknown command, please try again")

        print(" ")
        print("-" * 30)
        print(" ")
