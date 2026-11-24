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

show_menu() 
add_task()
view_task()      