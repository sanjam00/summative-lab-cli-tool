from lib.utils import storage

def main():
  print(f"[START]")

  users_file = storage.get_setting("users_file", "./data/users.json")
  tasks_file = storage.get_setting("tasks_file", "./data/tasks.json")
  projects_file = storage.get_setting("projects_file", "./data/projects.json")

  print(f"users_file={users_file}")
  print(f"tasks_file={tasks_file}")
  print(f"projects_file={projects_file}")

  print(f"[END]")

if __name__ == "__main__":
 main()