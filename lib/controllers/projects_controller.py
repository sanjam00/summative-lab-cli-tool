from lib.models.projects import Project
from .base_controller import BaseController


class ProjectController(BaseController):
  def __init__(self, filepath):
    self.filepath = filepath
    self.data = []
    
  model_class = Project

  """
  TO-DO:
  add project
  list projects
  assign a user to a project
  list all projects assigned to a user
  view project details
  """