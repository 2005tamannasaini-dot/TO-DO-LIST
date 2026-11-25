## TO-DO LIST PROJECT
 
tasks = []

def show_menu():
    print("\n========== TO-DO LIST===========")
    print("1. ADD TASK")
    print("2.VIEW TASK ")
    print("3. UPDATE TASK")
    print("4. DELETE TASK")
    print("5. EXIT")
 
def add_task():
    task = input("Enter a New Task:")
    tasks.append(task)
    print("Task Added Successfully.")

def view_task():
    if not tasks:
        print("NO Found Task.")
    else:
        print("===Your Tasks===")
        for task in tasks:
            print("Task:",task)

def update_task():
    update_task = input("Enter Task to update:")
    new_task = input("Enter New Taks:")

    if not tasks:
        print("No Found Task")

    else:
        for task in tasks:
            if task.lower() == update_task.lower():
                index = tasks.index(task)
                tasks[index] = new_task
                print("Contact updated successfully!")
                break

        else:
            print("Task not found.")


show_menu() 
add_task()
view_task()      
update_task()