todo_list = []

def formatResult(todo_list):
    formatted = ""
    for item in todo_list:
        formatted += item+"\n"
    return formatted
    
    
def addToList(todo):
    todo_list.append(todo)
    return formatResult(todo_list)

def removeFromList(todo):
    todo_list.remove(todo)
    return formatResult(todo_list)

def listTodo():
    return formatResult(todo_list)

while True:
    print("\nTo-Do List Options:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")
    
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        print(listTodo())
    if choice == 2:
        todo = input("Enter your todo to add: ")
        print(addToList(todo))
    if choice == 3:
        todo = input("Enter your todo remove: ")
        print(removeFromList(todo))
    if choice == 4:
        break
    