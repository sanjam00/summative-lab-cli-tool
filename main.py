from lib.utils import storage
from lib.controllers.user_controller import UsersController
from lib.controllers.task_controller import TaskController

def main():
  print(f"[START]")

  users_file = storage.get_setting("users_file", "./data/users.json")
  tasks_file = storage.get_setting("tasks_file", "./data/tasks.json")
  projects_file = storage.get_setting("projects_file", "./data/projects.json")

  # print(f"users_file={users_file}")
  # print(f"tasks_file={tasks_file}")
  # print(f"projects_file={projects_file}")

  # users_controller = UsersController(users_file)
  # users_controller.data = storage.load_data(users_file)
  # user = users_controller.add_user({"name": "Sanaya", "email": "sanjam@gmail.com", })
  # print(user)

  # storage.save_data = (users_file, [user.to_dict() for user in users_controller.data] )

  with UsersController(users_file) as user_controller:
    # user_controller.add_user({"name": "Sanaya", "email": "sanjam@gmail.com"})

    user_controller.list_user()

  with TaskController(tasks_file) as task_controller:
    task_controller.list_task()

  print(f"[END]")

if __name__ == "__main__":
 main()