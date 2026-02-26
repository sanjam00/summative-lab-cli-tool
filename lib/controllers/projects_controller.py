from lib.models.projects import Project
from .base_controller import BaseController


class ProjectController(BaseController):
  def __init__(self, filepath):
    self.filepath = filepath
    self.data = []
    
  model_class = Project

  def add_project(self, args):
    if any(p.title == args['title'] for p in self.data):
      print(f"Project '{args['title']}' already exists")
      return None

    project = Project(
            title=args["title"],
            description=args["description"],
            due_date=args["due_date"],
            assigned_to=args["assigned_to"],
            complete=False
        )
    
    self.data.append(project)

    print(f"Project '{project.title}' added successfully.")

  def list_projects(self, args=None):
    if not self.data:
      print("No projects found.")
      return

    for project in self.data:
      status = "✅" if project.complete else "❌"
      print(f"[{status}] {project.title}")

  def complete_project(self, args):
    for project in self.data:
      if project.title == args["title"]:
        project.complete = True
        print(f"Project '{project.title}' marked as complete.")
        return project

    print(f"Project '{args['title']}' not found.")
    return None

  def view_project(self, args, task_controller):
    project = next((p for p in self.data if p.title == args["title"]), None)

    if not project:
      print(f"Project '{args['title']}' not found.")
      return

    print("\n--- Project Details ---")
    print(f"Title: {project.title}")
    print(f"Description: {project.description}")
    print(f"Assigned To: {project.assigned_to}")
    print(f"Due Date: {project.due_date}")
    print(f"Completed: {'Yes' if project.complete else 'No'}")

    project_tasks = [
      t for t in task_controller.data
      if t.project_title == project.title
    ]

    print("\nTasks:")
    if not project_tasks:
      print("  No tasks yet.")
    else:
      for task in project_tasks:
        status = "✅" if task.complete else "❌"
        print(f"  - [{status}] {task.title}")

  def assign_user(self, args, user_controller):
    project = next((p for p in self.data if p.title == args["project"]), None)

    if not project:
      print(f"Project '{args['project']}' not found.")
      return None
    
    user = next((u for u in user_controller.data if u.name == args["user"]), None)

    if not user:
      print(f"User '{args['user']}' not found.\nPlease enter a user that exists in the system. If the desired user does not exist, consider adding them with 'add-user'.")
      return None

    project.assigned_to = user.name

    print(f"User '{user.name}' assigned to project '{project.title}'.")
    return project
  
  def list_user_projects(self, args):
    user_name = args["user"]

    user_projects = [
      p for p in self.data
      if p.assigned_to == user_name
    ]

    if not user_projects:
      print(f"No projects assigned to '{user_name}'.")
      return

    print(f"Projects assigned to '{user_name}':")

    for project in user_projects:
      status = "✅" if project.complete else "❌"
      print(f" - [{status}] {project.title}")