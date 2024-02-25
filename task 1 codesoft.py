# task 1
# to do list

def print_tasks():
    task_list.sort(key=lambda x: (-int(x[2]), x[0]), reverse=True)
    for row in task_list:
        print(f"{row[0]} - Importance: {row[2]} - Due: {row[1]}")

task_list = []

while True:
    print("""TODO List Management System
    1: Add
    2: View
    3: Remove
    4: Edit
    5: Exit""")
    w = input()
    if w == '1':
        add = input("What do you want to add: ")
        due = input("When it is due: ")
        impo = input("Importance(1-4): ")
        while not (1 <= int(impo) <= 4):
            print("Invalid importance. Please enter a number between 1 and 4.")
            impo = input("Importance(1-4): ")
        row = [add, due, impo]
        task_list.append(row)
    elif w == '2':
        print_tasks()
    elif w == '3':
        rem = input("What do you want to remove: ")
        task_list = [row for row in task_list if row[0] != rem]
    elif w == '4':
        old_task = input("Which task do you want to edit? ")
        for i, row in enumerate(task_list):
            if row[0] == old_task:
                new_task = input("What do you want to change it to: ")
                new_due = input("When it is due: ")
                new_impo = input("Importance(1-4): ")
                while not (1 <= int(new_impo) <= 4):
                    print("Invalid importance. Please enter a number between 1 and 4.")
                    new_impo = input("Importance(1-4): ")
                task_list[i] = [new_task, new_due, new_impo]
    elif w == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please choose a number between 1-5.")
        