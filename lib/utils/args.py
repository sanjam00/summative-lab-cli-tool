import argparse
from rich_argparse import RichHelpFormatter, HelpPreviewAction
from lib.controllers.user_controller import UsersController
from lib.controllers.projects_controller import ProjectController
from lib.controllers.task_controller import TaskController
from lib.utils import storage

users_file = storage.get_setting("users_file", "./data/users.json")
tasks_file = storage.get_setting("tasks_file", "./data/tasks.json")
projects_file = storage.get_setting("projects_file", "./data/projects.json")

def build_parser():
  parser = argparse.ArgumentParser(
    description="CLI Project Manager Tool",
    formatter_class=RichHelpFormatter
    )
  
  # Generate help preview. Found in help-preview.txt
  parser.add_argument(
    "--generate-help-preview",
    action=HelpPreviewAction,
    path="help-preview.txt", 
)

  subparsers = parser.add_subparsers(dest="command")

  # ---------------- Users ----------------
  #   Add User
  add_user = subparsers.add_parser("add-user", help="Add a new user")
  add_user.add_argument("--name", required= True, help="User's full name")
  add_user.add_argument("--email", required=True, help="User's email address")

  #   List Users (list all users)
  subparsers.add_parser("list-users", help="List all users")

  # ---------------- Projects ----------------
  #   Add Project
  add_project = subparsers.add_parser("add-project", help="Add a new project")
  add_project.add_argument("--title", required=True, help="Project title")
  add_project.add_argument("--description", required=True)
  add_project.add_argument("--due_date", required=True)
  add_project.add_argument("--assigned_to", required=True, help="User's full name, as entered in the database")

  #   List Projects (list all projects)
  subparsers.add_parser("list-projects", help="List all projects")

  #   Assign User (assign a user to a project)
  assign_user = subparsers.add_parser("assign-user", help="Assign a user to a project")
  assign_user.add_argument("--project", required=True, help="Project title")
  assign_user.add_argument("--user", required=True, help="User's full name, as entered in the database")

  #   List user projects (list all projects assigned to a user)
  list_user_projects = subparsers.add_parser("list-user-projects", help="List all projects assigned to a user")
  list_user_projects.add_argument("--user", required=True, help="User's full name, as entered in the database")

  #   View projects (view project details)
  view_project = subparsers.add_parser("view-project", help="View project details")
  view_project.add_argument("--title", required=True, help="Project title")

  # ---------------- Tasks ----------------
  #   Add task (add a new task to a project)
  add_task = subparsers.add_parser("add-task", help="Add a new task to a project")
  add_task.add_argument("--title", required=True, help="Task name")
  add_task.add_argument("--project", required=True, help="Project title")

  #   Complete task (mark a task as complete)
  complete_task = subparsers.add_parser("complete-task", help="Mark a task as complete")
  complete_task.add_argument("--title", required=True, help="Task name")

  #   List tasks (list all tasks in a project)
  list_tasks = subparsers.add_parser("list-tasks", help="List all tasks in a project")
  list_tasks.add_argument("--project", required=True, help="Project title")

  return parser