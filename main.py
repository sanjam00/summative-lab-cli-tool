from lib.utils import storage
from lib.controllers.user_controller import UsersController
from lib.controllers.task_controller import TaskController
from lib.controllers.projects_controller import ProjectController

def main():
  print(f"[START]")

  users_file = storage.get_setting("users_file", "./data/users.json")
  tasks_file = storage.get_setting("tasks_file", "./data/tasks.json")
  projects_file = storage.get_setting("projects_file", "./data/projects.json")

  with UsersController(users_file) as user_controller:
    user_controller.add_user({"name": "James", "email": "james001@gmail.com"})
    user_controller.add_user({"name": "Echo", "email": "echoechoecho3@gmail.com"})

    user_controller.list_user()

  with TaskController(tasks_file) as task_controller:
    
    #this works:
    # task_controller.add_task({"title": "Implement argparse",
    #                           "project": "Summative Lab",
    #                           "complete": False})
    pass

  with ProjectController(projects_file) as project_controller:

    #works:
    # project_controller.add_project({"title": "Summative Lab3", 
    #                                 "description": "The final lab for the month, should include everything learned this month.", 
    #                                 "due date": "2/25/2026", 
    #                                 "assigned to": "Sanaya James", 
    #                                 "complete": False})

    project_controller.list_projects()

    #works:
    # project_controller.view_project({"title": "Summative Lab"}, task_controller)
    # project_controller.view_project({"title": "Summative Lab2"}, task_controller)
    # project_controller.view_project({"title": "Summative Lab3"}, task_controller)

    #works:
    # project_controller.assign_user({"project": "Summative Lab",
    #                                "user": "James"})

    #works:
    project_controller.list_user_projects({"user": "Sanaya James"})

  print(f"[END]")

if __name__ == "__main__":
 main()