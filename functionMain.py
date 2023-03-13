FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filepath=FILEPATH):
   
    with open(FILEPATH, "w") as file:
        file.writelines(todos)

# print(__name__)
# if __name__ == "__main__":
#     print(get_todos())