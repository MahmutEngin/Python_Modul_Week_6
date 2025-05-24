from abc import ABC, abstractmethod
from datetime import datetime, timedelta

SPECIAL_KEYWORDS = {
    "today": datetime.now().date(),
    "tomorrow": (datetime.now() + timedelta(days=1)).date(),
    "next week": (datetime.now() + timedelta(days=7)).date(),
}
class Task(ABC):
    def __init__(self, task_id, task_name, deadline, status="Pending", priority="Medium"):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = self.parse_deadline(deadline)
        self.status = status
        self.priority = priority
        self.color = None  # Will be set by subclass
    
    def parse_deadline(self, deadline):
        if isinstance(deadline, str) and deadline.lower() in SPECIAL_KEYWORDS:
            return SPECIAL_KEYWORDS[deadline.lower()]
        elif isinstance(deadline, str):
            return datetime.strptime(deadline, "%Y-%m-%d").date()
        return deadline

    def days_left(self):
        return (self.deadline - datetime.now().date()).days
    
    @abstractmethod
    def color_your_task(self):
        pass
class TaskManagement:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)
        print(f"Task added: {task.task_name} ({task.__class__.__name__})")

    def display_tasks(self):
        if not self.task_list:
            print("No tasks available.")
            return
        for task in self.task_list:
            print(f"ID: {task.task_id}, Name: {task.task_name}, Deadline: {task.deadline}, "
                  f"Status: {task.status}, Priority: {task.priority}, Color: {task.color}")
class PersonalTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline, priority="Low")
        self.color_your_task()

    def color_your_task(self):
        self.color = "Green"
        
class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline, priority="High")
        self.color_your_task()

    def color_your_task(self):
        self.color = "Red"
class TaskEditing:
    def __init__(self, task_list):
        self.task_list = task_list

    def find_task_by_id(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                return task
        return None

    def edit_task(self, task_id, attribute, new_value):
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"No task with ID {task_id} found.")
            return
        
        if attribute == "status":
            task.status = new_value
        elif attribute == "priority":
            task.priority = new_value
        elif attribute == "deadline":
            task.deadline = task.parse_deadline(new_value)
        else:
            print(f"Attribute {attribute} not editable.")
            return

        print(f"Task {task_id} updated: {attribute} = {new_value}")
class TaskTracking:
    def __init__(self, task_list):
        self.task_list = task_list

    def get_task_info(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                print(f"Status: {task.status}, Deadline: {task.deadline}, Color: {task.color}")
                return
        print(f"No task found with ID {task_id}.")
if __name__ == "__main__":
    manager = TaskManagement()
   
    task1 = PersonalTask(1, "Buy groceries", "tomorrow")
    task2 = WorkTask(2, "Submit report", "2025-06-01")
   
    manager.add_task(task1)
    manager.add_task(task2)

    manager.display_tasks()

    editor = TaskEditing(manager.task_list)
    editor.edit_task(1, "status", "Completed")
    editor.edit_task(2, "deadline", "next week")

    tracker = TaskTracking(manager.task_list)
    tracker.get_task_info(1)
    tracker.get_task_info(2)
       
#   Task II
"""

+--------------------+           +----------------+
|    NoteManager     |           |      Note      |
+--------------------+           +----------------+
| - notes: List<Note>|◄◄◄◄◄◄◄◄◄| - title: str    |
|                    |           | - content: str |
|                    |           | - created_at   |
+--------------------+           +----------------+
| + add_note(note)   |           | + display()    |
| + remove_note(t)   |           | + edit_content |
| + find_note(t)     |           +----------------+
+--------------------+

"""
