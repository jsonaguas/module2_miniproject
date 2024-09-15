to_do_list = {}
def add_task():
    title = input("Title of tasks? ")
    description=input("Brief description of task? ")
    status = input("Complete or Incomplete? ")
    to_do_list[title] = {"description": description, "status": status}
    print(f"{title} added!")

def view_tasks():
    if len(to_do_list) != 0:
        for title, task in to_do_list.items():
            print(f"Title: {title}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print()
    else:
        print("No tasks to display")
    

def mark_task():
    if len(to_do_list) != 0:
        title = input("Title of task to mark as complete? ")
        to_do_list[title]["status"] = "Complete"
        print(f"{title} marked as complete!")
    else:
        print("No tasks to mark as complete")

def delete_task():
    if len(to_do_list) != 0:
        title = input("Title of task to delete? ")
        del to_do_list[title]
        print(f"{title} deleted!")
    else:
        print("No tasks to delete")    

def main():
    try:
        welcome =int(input(''' Welcome to the To-Do List App!
                Menu:
                1. Add a task
                2. View tasks
                3. Mark a task as complete
                4. Delete a task
                5. Quit
            Hi, what would you like to do?    '''))
        if welcome == 1:
            add_task()
        elif welcome == 2:
            view_tasks()
        elif welcome == 3:
            mark_task()
        elif welcome == 4:
            delete_task()
        elif welcome == 5:
            print("Goodbye!")

    except ValueError:
        print("Please enter a valid number")
        welcome =int(input(''' Welcome to the To-Do List App!
                Menu:
                1. Add a task
                2. View tasks
                3. Mark a task as complete
                4. Delete a task
                5. Quit
            Hi, what would you like to do?    '''))

main()