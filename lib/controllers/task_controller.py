from lib.models.task import Task
from .base_controller import BaseController

class TaskController(BaseController):
  def __init__(self, filepath):
    self.filepath = filepath
    self.data = []

  model_class = Task

  def add_task(self, args):
    if any(t.title == args["title"] for t in self.data):
      print(f"Task with title '{args['title']}' already exists.")
      return None

    task = Task(
      title=args["title"],
      complete=args["complete"]
    )

    self.data.append(task)

    print(f"Task '{task.title}' was added successfully")

    return task

  def complete_task(self, args):
    for task in self.data:
      if task.title == args["title"]:
        task.complete = True
        print(f"{task.title} was successfully marked as complete! Good work!")
        return task
      
    print(f"{args['title']} not found in task list.")
    return None
    
  def list_task(self):
    for task in self.data:
      if task.complete == True:
        print(f"{task.title} - Completed")
      else:
        print(f"{task.title} - Imcomplete")
