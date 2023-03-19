import functionMain
todos= functionMain.get_todos()
def removeCharacter(list):
    new_list =[]
    for item in list:
        new_list.append(item.replace("\n",""))
    return new_list

def addCharacter(list):
    new_list = []
    for item in list:
        new_list.append(item + "\n")
    return new_list

if __name__ == "__main__":
    removed_todos = removeCharacter(todos)
    print(removed_todos)
    added_todos = addCharacter(removed_todos)
    print(added_todos)