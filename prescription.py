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
      """
      Adds a new prescription to the 'prescription_database.csv' file. If the file is empty,
      it also writes the headers. This method assumes the Prescription object contains all necessary fields.

      Args:
          prescription (Prescription): The Prescription object to add to the database.

      Raises:
          IOError: If the file could not be opened or written to.
      """
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
      """
      Reads all prescriptions from the 'prescription_database.csv' file and returns them as a list of dictionaries.

      Returns:
          list of dict: A list of all prescriptions read from the file, each represented as a dictionary.

      Raises:
          FileNotFoundError: If the 'prescription_database.csv' file does not exist.
      """
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
      """
      Updates an existing prescription in the 'prescription_database.csv' file based on the name provided. 
      It replaces the old prescription data with the updated data.

      Args:
          name (str): The name of the prescription to update.
          updated_prescription (Prescription): The new prescription data to replace the old one.

      Returns:
          bool: True if the update was successful, False otherwise.

      Raises:
          IOError: If the file could not be opened or written to.
      """
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
      """
      Updates the entire prescription database by overwriting it with new data.

      This method takes a list of dictionaries where each dictionary represents a prescription item. 
      Each prescription item must contain keys for 'Name', 'Expiration Date', 'Price', and 'Stock'.
      The entire existing database file will be overwritten with the data provided.

      Parameters:
          prescriptions (list of dict): A list of dictionaries with each dictionary containing 
                                        details of a prescription, including name, expiration date,
                                        price, and stock level.

      Raises:
          IOError: If the file cannot be opened or written to.
          ValueError: If an incorrect format is provided in the prescriptions list.
      """
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
      """
      Deletes a prescription from the 'prescription_database.csv' file based on the prescription name.

      Args:
          name (str): The name of the prescription to delete.

      Raises:
          IOError: If the file could not be opened or written to.
      """
      prescriptions = Prescription.read_prescriptions()
      with open('prescription_database.csv', mode='w', newline='') as file:
          fieldnames = ['Name', 'Expiration Date', 'Price', 'Stock']
          writer = csv.DictWriter(file, fieldnames=fieldnames)
          writer.writeheader()
          for prescription in prescriptions:
              if prescription['Name'].lower() != name.lower():
                  writer.writerow(prescription)