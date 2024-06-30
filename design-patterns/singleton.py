class Singleton:

  __instance=None
  @staticmethod
  def get_instance():
    if Singleton.__instance==None:
      Singleton()
    return Singleton.__instance
  
  def __init__(self):
    if Singleton.__instance :
      raise Exception("Singleton object already exists")
    else:
      Singleton.__instance=self
      

