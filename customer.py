from prescription import Prescription


class Customer(Prescription):
  """
  A class to represent a customer
  Args:
    name (str): The name of the customer
    address (str): The address of the customer
    payment_information (str): The payment information of the customer
    prescription (str): The prescription of the customer)
    id (str): The id of the customer
    password (str): The password of the customer

    Returns: None
    Raises: None
  """
  def __init__(self, name : str, address : str, payment_information : str, 
               prescription : str, id : str, password : str):
    """initialize all attributes"""
    self.name = name
    self.address = address
    self.payment_information = payment_information
    self.prescription = prescription
    self.id = id
    self.password = password
  

  def set_name(self, name):
    """
    set the name of the customer
    Args:
      name (str): The name of the customer
      
      Returns: None
      Raises: None
    """
    pass

  def set_address(self, address):
    """
    set the address of the customer
    Args:
      address (str): The address of the customer

      Returns: None 
      Raises: None
    """
    pass

  def set_payment_information(self, payment_information):
    """
    set the payment information of the customer
    Args:
      payment_information (str): The payment information of the customer

      Returns: None
      Raises: None
    """
    self.payment_information = payment_information

  def get_prescription(self, prescription) -> str:
    """
    get the prescription of the customer
    Args:
      prescription (str): The prescription of the customer

      Returns: prescritpion (str)
      Raises: None
      
    """
    return self.prescription

  def set_id(self, id):
    """
    set the id of the customer
    Args:
      id (str): The id of the customer

    Returns: None
    Raises: None
    """
    self.id = id

  def set_password(self, password):
    """
    set the password of the customer
    Args:
      password (str): The password of the customer

    Returns: None
    Raises: None
    """
    self.password = password