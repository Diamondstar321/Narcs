from prescription import Prescription

class Order(Prescription):

def __init__(self, name: str, orderNumber: int, prescription: str, deliveryDate: str, shippingAddress: str, employeeName: str):
    """
    Places an order with the specified prescription and customer information
    :param name: The customer's first and last name
    :param orderNumber: A unique number identifying the customer's order
    :param prescription: A string containing the customer's prescription
    :param delivery_date: 'MM/DD/YYYY' format for displaying the order's delivery date
    :param shipping_address: The customer's street address
    :param employee_name: The employee responsible for fulfilling the order"""

    self.name = name 
    self.order_number = orderNumber
    self.prescription = prescription
    self.delivery_date = deliveryDate
    self.shipping_address = shippingAddress
    self.employee_name = employeeName

def getName(self) -> str:
  """Returns the customer's name"""
  return self.name

def getOrderNumber(self) -> int:
  """Returns the order number"""
  return self.order_number

def getPrescription(self) -> str:
  """ Returns the prescription"""
  return self.prescription

def getDeliveryDate(self) -> str:
  """Returns the order delivery date"""
  return self.delivery_date

def getShippingAddress(self) -> str:
  """Returns the customer's shipping address"""
  return self.shipping_address

def getEmployeeName(self) -> str:
  """Returns the employee responsible for fulfilling the order"""
  return self.employee_name
