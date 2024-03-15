class Customer:
  '''A class to represent a customer'''
  def __init__(self, name : str, address : str, payment_information : str, 
               prescription : str, id : str, password : str):
    '''initialize all attributes'''
    self.name = name
    self.address = address
    self.payment_information = payment_information
    self.prescription = prescription
    self.id = id
    self.password = password
  

  def set_name(self, name):
    '''set the name of the customer'''
    pass

  def set_address(self, address):
    '''set the address of the customer'''
    pass

  def set_payment_information(self, payment_information):
    '''set the payment information of the customer'''
    pass

  def get_prescription(self, prescription):
    '''get the prescription of the customer'''
    pass

  def set_id(self, id):
    '''set the id of the customer'''
    pass

  def set_password(self, password):
    '''set the password of the customer'''
    pass