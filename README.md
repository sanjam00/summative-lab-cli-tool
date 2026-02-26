# CLI Project Manager Tool

The Command-Line Project Manager Tool is built in Python using an MVC-style architecture. This tool allows users to create and manage users, projects, and tasks.

# Features

- Create and list users
- Create and list projects
- View project details
- Assign users to projects
- List projects assigned to a specific user
- Create and list tasks
- Mark tasks and projects as complete

# Installation

This application was built in a virtual environment in Python 3.14.0.

To install and run a virtual environment:
```bash
pip install pipenv

pipenv install

pipenv shell
```
Refer to the requirements.txt file for necessary requirements and dependencies.

# Usage

## Run commands using:
```python
pipenv run python main.py <command> [options]

# if not using pipenv:
python main.py <command> [options]

# for a list of available commands:
python main.py -h

#for help with a specific command:
python main.py <command> -h
```

## Example: Adding a user
```python
#for help with a specific command, example:
python main.py add-user -h

python main.py add-user --name "James" --email "james@email.com"
```

Refer to help-preview.txt to see a preview of the help menu.

# Project Structure

summative-lab-cli-tool/
│
├── main.py
├── README.md
├── requirements.txt
├── help-preview.txt
├── settings.json
│
├── data/
│   ├── users.json
│   ├── projects.json
│   └── tasks.json
│
└── lib/
    ├── controllers/
    │   ├── base_controller.py
    │   ├── user_controller.py
    │   ├── projects_controller.py
    │   └── task_controller.py
    │
    ├── models/
    │   ├── user.py
    │   ├── project.py
    │   └── task.py
    │
    └── utils/
        └── args.py
        └── storage.py

# Data Storage

All data is stored in JSON files inside the data/ directory:
  users.json
  projects.json
  tasks.json

Data persists between program runs.

# Future Improvements

- Use unique IDs for projects, tasks, and when assigning a user to a project.
    Eliminates room for user error by eliminating the need to type a name exactly as entered in the system.
- Add task description, due dates, and priority status.
- Add deletion capability
    Currently, there is no possibility to delete a user, project or task. This is necessary for large scale use.
- Add search and filtering.
- Automatically mark project as complete.
    Once all tasks have been completed under a project, it should be auto-marked as complete.
- Vaildation features
    Example: validate email format and date format, etc.
- Improve error handling by implementing error messages and exit codes instead of relying on print messages.

# Author

Sanaeya James
Software Engineering Student