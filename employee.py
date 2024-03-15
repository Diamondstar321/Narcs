class Employee:
  def __init__(self, name, id, password):
    """
    This function is intitilizer for the attributes of the Employee class
    Args:
    name (str): The name of the employee)
    id (str): The id of the employee
    password (str): The password of the employee
    Returns: None
    Rises: None
    """
    self.name = name
    self._id= id
    self._password = password

  def setName(self,name):
    """
    This function is used to set the name of the employee
    Args: 
    name (str): The name of the employee
    Returns: None
    Rises: None
    """
    self.name = name
    print("Employee name is set to: ", self.name)

  def getEmployeeName(self):
    """
    This function is used to get the name of the employee
    Args: None
    Returns: str: The name of the employee
    Rises: None
    """
    return self.name

  def setID(self, id):
    """
    This function is used to set the id of the employee
    Args:
    id (str): The id of the employee
    Returns: None
    Rises: None
    """
    self._id = id
    print("Please enter your ID: ", self._id)

  def setPassword(self, password):
    """ 
    This function is used to set the password of the employee 
    Args:
    password (str): The password of the employee
    Returns: None
    Rises: None
    """
    self._password = password
    print("Please enter your password: ", self._password)
