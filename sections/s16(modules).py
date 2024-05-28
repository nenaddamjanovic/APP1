from section_functions import get_todos, write_todos
import time

#  -----------------------------------------------------------------------------
now = time.strftime("%H:%M:%S, %d %b, %Y ")
print(f"Now it is: {now}")

while True:
    user_action = input("type add, show, edit, complete (then space and command) or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos()
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is not valid, format is ACTION NUMBER")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todos(todos)
            message = f"item {todo_to_remove} is completed and removed from list"
            print(message)
        except IndexError:
            print(f"There is no item with that number, there are only {len(todos)} items")
            continue
        except ValueError:
            print("Your command is not valid, format is ACTION NUMBER")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid.")

print("Bye!")
