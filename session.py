from menu_definitions import menu_main


class Session:
  def __init__(self):
      self.logged_in = False
      self.user_data = None
      self.current_menu = menu_main