import argparse
from lib.utils.args import build_parser
from lib.utils import storage
from lib.controllers.user_controller import UsersController
from lib.controllers.task_controller import TaskController
from lib.controllers.projects_controller import ProjectController

def main():
  parser = build_parser()
  args = parser.parse_args()

  users_file = storage.get_setting("users_file", "./data/users.json")
  tasks_file = storage.get_setting("tasks_file", "./data/tasks.json")
  projects_file = storage.get_setting("projects_file", "./data/projects.json")

  with UsersController(users_file) as user_controller, \
      ProjectController(projects_file) as project_controller, \
      TaskController(tasks_file) as task_controller:
    
    if args.command == "add-user":
      user_controller.add_user(vars(args))
    
    elif args.command == "list-users":
      user_controller.list_users()

    elif args.command == "add-project":
      project_controller.add_project(vars(args))

    elif args.command == "list-projects":
      project_controller.list_projects()
    
    elif args.command == "assign-user":
      project_controller.assign_user(vars(args))
    
    elif args.command == "list-user-projects":
      project_controller.list_user_projects(vars(args))

    elif args.command == "view-project":
      project_controller.view_project(vars(args), task_controller)
    
    elif args.command == "add-task":
      task_controller.add_task(vars(args))

    elif args.command == "complete-task":
      task_controller.complete_task(vars(args))
    
    elif args.command == "list-tasks":
      task_controller.list_tasks(vars(args))

    else:
      parser.print_help()


if __name__ == "__main__":
 main()