from datetime import datetime
import json
import os

class TodoList:
    def __init__(self):
        self.file_name = "todos.json"
        self.todos = self.load_todos()
    
    def load_todos(self):
        if os.path.exists(self.file_name):
            with open(self.file_name) as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_task(self):
        task = input("Task description: ")
        priority = input("Priority (high/medium/low): ").lower()
        due_date = input("Due date (YYYY-MM-DD, optional): ")
        
        new_task = {
            "id": len(self.todos) + 1,
            "task": task,
            "priority": priority if priority in ['high', 'medium', 'low'] else 'medium',
            "created": datetime.now().strftime("%Y-%m-%d"),
            "completed": False,
            "due_date": due_date if due_date else None
        }
        
        self.todos.append(new_task)
        self.save_todos()
        print("Task added!")
    
    def list_tasks(self):
        print("\nYour Todo List:")
        for todo in sorted(self.todos, key=lambda x: x['priority']):
            status = "✓" if todo['completed'] else " "
            print(f"{todo['id']}. [{status}] {todo['task']}")
            print(f"   Priority: {todo['priority']} | Due: {todo['due_date'] or 'None'}")
    
    def complete_task(self):
        task_id = int(input("Enter task ID to complete: "))
        for todo in self.todos:
            if todo['id'] == task_id:
                todo['completed'] = True
                self.save_todos()
                print("Task marked as completed!")
                return
        print("Task not found!")

def main():
    todo = TodoList()
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Complete Task\n4. Exit")
        choice = input("Select option: ")
        
        if choice == '1':
            todo.add_task()
        elif choice == '2':
            todo.list_tasks()
        elif choice == '3':
            todo.complete_task()
        elif choice == '4':
            break

if __name__ == "__main__":
    main()

