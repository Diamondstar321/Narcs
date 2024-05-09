import csv
from prescription import Prescription

class ShoppingCart:
    """
    A simple shopping cart for managing purchases within a pharmacy application.
    It allows for adding items to the cart, removing them, and printing a receipt with total costs.

    Attributes:
        items (dict): A dictionary to store prescription items with their names as keys and details (name, quantity, price) as values.
    """

    def __init__(self):
        """
        Initializes a new instance of the ShoppingCart with an empty dictionary for storing items.
        """
        self.items = {}

    def add_item(self, prescription, quantity):
        """
        Adds a prescription item to the shopping cart or updates the quantity if the item already exists.

        Args:
            prescription (dict): The prescription details including its name and price.
            quantity (int): The quantity of the prescription item to add.
        """
        if prescription['Name'] in self.items:
            self.items[prescription['Name']]['quantity'] += quantity
        else:
            self.items[prescription['Name']] = {
                'name': prescription['Name'],
                'quantity': quantity,
                'price': float(prescription['Price'])
            }

    def print_receipt(self):
        """
        Prints a receipt for all items in the shopping cart, including subtotal, tax, and total costs.
        """
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
        """
        Removes a specified quantity of a prescription item from the shopping cart. 
        If the quantity to remove matches or exceeds what's in the cart, the item is removed entirely.

        Args:
            prescription (dict): The prescription to remove.
            quantity (int): The quantity to remove.
        """
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
        """
        Reads all prescription details from the database file.

        Returns:
            list: A list of prescription data from the database.
        """
        prescriptions = []
        try:
            with open('prescription_database.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    prescriptions.append(row)
        except FileNotFoundError:
            print("The database file does not exist.")
        return prescriptions
