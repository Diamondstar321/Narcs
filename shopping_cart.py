import csv
from prescription import Prescription

class ShoppingCart:
  def __init__(self):
      self.items = {}

  def add_item(self, prescription, quantity):
    if prescription['Name'] in self.items:
        self.items[prescription['Name']]['quantity'] += quantity
    else:
        self.items[prescription['Name']] = {
            'name': prescription['Name'],
            'quantity': quantity,
            'price': float(prescription['Price']) 
        }

  def print_receipt(self):
    subtotal = 0
    print("Receipt:")
    print("========================================")
    for name, details in self.items.items():
        line_total = details['quantity'] * details['price']
        subtotal += line_total
        print(f"{details['quantity']} x {name} at ${details['price']:.2f} each: ${line_total:.2f}")

    tax = subtotal * 0.08
    total = subtotal + tax 

    print("========================================")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (8%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")



  def remove_item(self, prescription, quantity):
      if prescription['Name'] in self.items:
          if self.items[prescription['Name']]['quantity'] >= quantity:
              self.items[prescription['Name']]['quantity'] -= quantity
              print(f"{quantity} of {prescription['Name']} removed from the cart.")
              if self.items[prescription['Name']]['quantity'] == 0:
                  del self.items[prescription['Name']]
          else:
              print(f"Unable to remove {quantity}. Only {self.items[prescription['Name']]['quantity']} in cart.")
      else:
          print(f"No {prescription['Name']} in the cart to remove.")

  @staticmethod
  def read_prescriptions():
    prescriptions = []
    try:
      with open('prescription_database.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
          prescriptions.append(row)
    except FileNotFoundError:
      print("The database file does not exist.")
    return prescriptions

    
      
