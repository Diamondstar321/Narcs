import csv
from datetime import datetime


class Prescription:

  def __init__(self, name, expiration_date, price, stock):
    """
    Function to initialize the prescription object

    Args:
      name (str): Name of the prescription
      expiration_date (str): Expiration date of the prescription
      price (float): Price of the prescription
      stock (int): Stock of the prescription
    Returns: None
    Raises: None
    """
    self.name = name
    self.expiration_date = expiration_date
    self.price = price
    self.stock = stock
  
  def set_prescription_name(self, name):
    """
    Function that sets the prescription name
    Args:
      name (str): Name of the prescription
    Returns: None
    Raises: None
    """
    self.name = name

  def get_prescription_name(self):
    """
    Function that gets the prescription name
    Args: None
    Returns: str: Name of the prescription
    Raises: None
    """
    return self.name

  def set_expiration_date(self, date):
    """
    Function that sets the expiration date of the prescription.
    Args: 
      date (str): Expiration date of the prescription
    Returns: None
    Raises: None
    """
    self.expiration_date = date

  def get_expiration_date(self):
    """
    Retrieves the expiration date of the prescription.
    Args: None
    Returns: str: Expiration date of the prescription
    Raises: None
    """
    return self.expiration_date

  def set_price(self, price):
    """
    Function that sets the price of the prescription.
    Args:
      price (float): Price of the prescription
    Returns: None
    Raises: None
    """
    self.price = price

  def get_price(self):
    """
    Retrieves the price of the prescription.
    Args: None
    Returns: float: Price of the prescription
    Raises: None
    """
    return self.price


  def set_stock(self, stock):
    """
    Function that sets the stock of the prescription.
    Args: 
      stock (int): Stock of the prescription
    Returns: None
    Raises: None 
    """
    self.stock = stock

  def get_stock(self):
    """
    Retrieves the stock of the prescription.
    Args: None
    Returns: int: Stock of the prescription
    Raises: None
    """
    return self.stock

#read|write|update|delete operations

  @staticmethod
  def add_prescription(prescription):
      with open('prescription_database.csv', mode='a', newline='') as file:
          fieldnames = ['Name', 'Expiration Date', 'Price', 'Stock']
          writer = csv.DictWriter(file, fieldnames=fieldnames)
          if file.tell() == 0:  # Check if file is at the start to write the header
              writer.writeheader()
          writer.writerow({
              'Name': prescription.name,
              'Expiration Date': prescription.expiration_date,
              'Price': prescription.price,
              'Stock': prescription.stock
          })
  
  @staticmethod
  def read_prescriptions():
      prescriptions = []
      try:
          with open('prescription_database.csv', mode='r') as file:
              reader = csv.DictReader(file)
              for row in reader:
                  prescriptions.append(row)
      except FileNotFoundError:
          print("The database file does not exist.")
      return prescriptions
  
  @staticmethod
  def update_prescription(name, updated_prescription):
      prescriptions = Prescription.read_prescriptions()
      updated = False
      with open('prescription_database.csv', mode='w', newline='') as file:
          fieldnames = ['Name', 'Expiration Date', 'Price', 'Stock']
          writer = csv.DictWriter(file, fieldnames=fieldnames)
          writer.writeheader()
          for prescription in prescriptions:
              if prescription['Name'].lower() == name.lower():
                  writer.writerow({
                      'Name': updated_prescription.name,
                      'Expiration Date': updated_prescription.expiration_date,
                      'Price': updated_prescription.price,
                      'Stock': updated_prescription.stock
                  })
                  updated = True
              else:
                  writer.writerow(prescription)
      return updated

  @staticmethod
  def update_prescription_database(prescriptions):
      """Update the entire prescription database with new data."""
      with open('prescription_database.csv', mode='w', newline='') as file:
          fieldnames = ['Name', 'Expiration Date', 'Price', 'Stock']
          writer = csv.DictWriter(file, fieldnames=fieldnames)
          writer.writeheader()
          for prescription in prescriptions:
              writer.writerow({
                  'Name': prescription['Name'],
                  'Expiration Date': prescription['Expiration Date'],
                  'Price': prescription['Price'],
                  'Stock': prescription['Stock']
              })

  
  @staticmethod
  def delete_prescription(name):
      prescriptions = Prescription.read_prescriptions()
      with open('prescription_database.csv', mode='w', newline='') as file:
          fieldnames = ['Name', 'Expiration Date', 'Price', 'Stock']
          writer = csv.DictWriter(file, fieldnames=fieldnames)
          writer.writeheader()
          for prescription in prescriptions:
              if prescription['Name'].lower() != name.lower():
                  writer.writerow(prescription)
  


  
          

