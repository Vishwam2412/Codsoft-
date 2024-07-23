import json
from datetime import datetime, date

class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "description": self.description,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["description"])
        task.completed = data["completed"]
        if data["due_date"]:
            task.due_date = date.fromisoformat(data["due_date"])
        return task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def update_task(self, index, description, due_date):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description
            self.tasks[index].due_date = due_date

    def get_tasks(self):
        return self.tasks

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            self.tasks = []

def print_tasks(todo_list):
    tasks = todo_list.get_tasks()
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task.completed else " "
            due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
            print(f"{i + 1}. [{status}] {task.description} (Due: {due_date})")

def get_date_input():
    while True:
        date_str = input("Enter due date in same format with '-' (YYYY-MM-DD) or leave blank for no due date: ")
        if not date_str:
            return None
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    todo_list = ToDoList()
    filename = "todo_list.json"
    todo_list.load_from_file(filename)

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Update task")
        print("6. Save and quit")

        choice = input("Enter your choice [1-6]: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = get_date_input()
            todo_list.add_task(Task(description, due_date))
            print("Task added successfully.")

        elif choice == '2':
            print_tasks(todo_list)

        elif choice == '3':
            print_tasks(todo_list)
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)
            print("Task marked as completed.")

        elif choice == '4':
            print_tasks(todo_list)
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(index)
            print("Task removed successfully.")

        elif choice == '5':
            print_tasks(todo_list)
            index = int(input("Enter the task number to update: ")) - 1
            description = input("Enter new task description: ")
            due_date = get_date_input()
            todo_list.update_task(index, description, due_date)
            print("Task updated successfully.")

        elif choice == '6':
            todo_list.save_to_file(filename)
            print("To-Do List saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()