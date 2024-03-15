class Prescription:
  def __init__(self, name, expiration_date, shelf_life, price):
    """
    Function to initialize the prescription object

    Args:
      name (str): Name of the prescription
      expiration_date (str): Expiration date of the prescription
      shelf_life (int): Shelf life of the prescription
      price (float): Price of the prescription
    Returns: None
    Raises: None
    """
    self.name = name
    self.expiration_date = expiration_date
    self.shelf_life = shelf_life
    self.price = price

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
  
  def set_shelf_life(self, shelf_life):
    """
    Function that sets the shelf life of the prescription.
    Args:
      shelf_life (int): Shelf life of the prescription
    Returns: None
    Raises: None
    """
    self.shelf_life = shelf_life

  def get_shelf_life(self):
    """
    Retrieves the shelf life of the prescription.
    Args: None
    Returns: int: Shelf life of the prescription
    Raises: None
    """
    return self.shelf_life
    
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