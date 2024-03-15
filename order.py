from prescription import Prescription
from customer import Customer
from employee import Employee

class Order(Customer, Employee, Prescription):

  def __init__(self, name: str, orderNumber: int, prescription: str, deliveryDate: str, shippingAddress: str, employeeName: str):
    """
    This function is the initializer for the Order class.
    Args:
      name (str): The name of the order
      orderNumber (int): The order number of the order
      prescription (str): The prescription of the order
      shiipingAddress (str): The shipping address of the order
      deliveryDate (str): The delivery date of the order
      employeeName (str): The name of the employee who is delivering the order
    """
    self.name = name 
    self.order_number = orderNumber
    self.prescription = prescription
    self.delivery_date = deliveryDate
    self.shipping_address = shippingAddress
    self.employee_name = employeeName
  
  def getName(self) -> str:
    """
    Returns the customer's name
    Args:None
    Returns: str: The customer's name
    Raises: None
    """
    return self.name
  
  def getOrderNumber(self) -> int:
    """
    Returns the order number
    Args: None
    Returns: int: The order number
    Raises: None
    """
    return self.order_number
  
  def getPrescription(self) -> str:
    """ 
    This function returns the prescription of the order
    Args:None
    Returns the prescription
    Raises: None
    """
    return self.prescription
  
  def getDeliveryDate(self) -> str:
    """
    Returns the order delivery date
    Args: None
    Returns: str: The order delivery date
    Raises: None
    """
    return self.delivery_date
  
  def getShippingAddress(self) -> str:
    """
    This function returns the shipping address of the order
    Args: None
    Returns the customer's shipping address
    Raises: None
    """
    return self.shipping_address
  
  def getEmployeeName(self) -> str:
    """
    Returns the employee responsible for fulfilling the order
    Args: None
    Returns: str: The name of the employee
    Raises: None
    """
    return self.employee_name
  