from lib.models.task import Task
from .base_controller import BaseController

class TaskController(BaseController):
  def __init__(self, filepath):
    self.filepath = filepath
    self.data = []

  model_class = Task

  def add_task(self):
    pass

  def list_task(self):
    for task in self.data:
      print(f"{task.title} {task.complete}")
      print("Tasks listed")