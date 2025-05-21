class Task:
    def __init__(self,task_id,task_name, deadline,status,priority,color):
        self.task_id=task_id
        self.task_name=task_name
        self.deadline=deadline
        self.status=status
        self.priority=priority
        self.color=color
    def days_until_deadline():
        pass
    def color_your_task():
        pass
class TaskManagement():
    task_list =[]
    def add_task(task:Task):
        pass
    def list_tasks():
        pass
class PersonalTask (Task):
    def __init__(self, task_id, task_name, deadline, status, priority, color):
        super().__init__(task_id, task_name, deadline, status, priority, color)
    pass
class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline, status, priority, color):
        super().__init__(task_id, task_name, deadline, status, priority, color)
    pass

class TaskEditing():
    def find_task_by_id(task_id):
        pass
    def update_status(task_id, new_status): 
        pass
    def update_priority(task_id, new_priority): 
        pass
    def update_deadline(task_id, new_deadline): 
        pass
   
class TaskTracking():

    def get_status(task_id):
        pass
    def get_deadline(task_id): 
        pass
    def get_color(task_id): 
        pass



       
  