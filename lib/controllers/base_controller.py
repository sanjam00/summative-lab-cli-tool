from lib.utils import storage

class BaseController:
  def __enter__(self):
    self.data = [
      self.model_class.from_dict(item)
      for item in storage.load_data(self.filepath)
    ]
    return self

  def __exit__(self, exc_type, exc, tb):
    storage.save_data(
      self.filepath,
      [item.to_dict() for item in self.data]
    )