from menu_definitions import menu_main

class Session:
  """
  Represents a user session with properties to track the user's login status, 
  associated data, and current menu context.

  Attributes:
      logged_in (bool): Indicates whether the user is logged in or not.
      user_data (dict or None): Stores user-specific data like username and employee status.
      current_menu (Menu): Holds the current menu instance that should be displayed to the user.

  The Session object is initialized with the user being logged out, having no user data,
  and set to display the main menu.
  """
  def __init__(self):
      self.logged_in = False
      self.user_data = None
      self.current_menu = menu_main
