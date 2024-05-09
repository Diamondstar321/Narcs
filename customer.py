from prescription import Prescription
import csv

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

  def __init__(self, name: str, address: str, payment_information: str,
               prescription: str, id: str, password: str):
    """initialize all attributes"""
    self.name = name
    self.address = address
    self.payment_information = payment_information
    self.prescription = prescription
    self.id = id
    self.password = password

  def set_name(self, database_name, current_name, new_name):
    """
    set the name of the customer
    Args:
      name (str): The name of the customer

      Returns: None
      Raises: None
    """
    with open(database_name, 'r') as csvfile:
      rows = csv.reader(csvfile)
      data = list(rows)

    rowNum = data.index(current_name)
    data[rowNum][0] = new_name

    with open(database_name, 'w', newline='') as csvfile:
      write = csv.writer(csvfile)
      write.writerows(data)

  def set_address(self, database_name, current_address, new_address):
    """
    set the address of the customer
    Args:
      address (str): The address of the customer

      Returns: None 
      Raises: None
    """
    with open(database_name, 'r') as csvfile:
      rows = csv.reader(csvfile)
      data = list(rows)

    rowNum = data.index(current_address)
    data[rowNum][0] = new_address

    with open(database_name, 'w', newline='') as csvfile:
      write = csv.writer(csvfile)
      write.writerows(data)

  def set_payment_information(self, database_name, current_payment_information,
                              new_payment_information):
    """
    set the payment information of the customer
    Args:
      payment_information (str): The payment information of the customer

      Returns: None
      Raises: None
    """
    with open(database_name, 'r') as csvfile:
      rows = csv.reader(csvfile)
      data = list(rows)

    rowNum = data.index(current_payment_information)
    data[rowNum][0] = new_payment_information

    with open(database_name, 'w', newline='') as csvfile:
      write = csv.writer(csvfile)
      write.writerows(data)

  def get_prescription(self, database_name):
    """
    get the prescription of the customer
    Args:
      prescription (str): The prescription of the customer

      Returns: prescritpion (str)
      Raises: None

    """
    with open(database_name, 'r') as csvfile:
      rows = csv.reader(csvfile)

      for row in rows:
        return row[
            4]  # The prescription is the 4th element in the customer's row in the database

  def set_id(self, database_name, current_id, new_id):
    """
    set the id of the customer
    Args:
      id (str): The id of the customer

    Returns: None
    Raises: None
    """
    with open(database_name, 'r') as csvfile:
      rows = csv.reader(csvfile)
      data = list(rows)

    rowNum = data.index(current_id)
    data[rowNum][0] = new_id

    with open(database_name, 'w', newline='') as csvfile:
      write = csv.writer(csvfile)
      write.writerows(data)

  def set_password(self, database_name, current_password, new_password):
    """
    set the password of the customer
    Args:
      password (str): The password of the customer

    Returns: None
    Raises: None
    """
    with open(database_name, 'r') as csvfile:
      rows = csv.reader(csvfile)
      data = list(rows)

    rowNum = data.index(current_password)
    data[rowNum][0] = new_password

    with open(database_name, 'w', newline='') as csvfile:
      write = csv.writer(csvfile)
      write.writerows(data)
