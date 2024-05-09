from prescription import Prescription
from shopping_cart import ShoppingCart
import csv


class Order:
  def __init__(self, name, orderNumber, shoppingCart, deliveryDate, shippingAddress, status):
      self.name = name
      self.order_number = orderNumber
      self.shopping_cart = shoppingCart
      self.delivery_date = deliveryDate
      self.shipping_address = shippingAddress
      self.status = status
    
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
  
  def getStatus(self) -> str:
    """
    Returns the employee responsible for fulfilling the order
    Args: None
    Returns: str: The name of the employee
    Raises: None
    """
    return self.status

  def save_to_order_database(self):
    """
    Saves the order details to a CSV file named 'order_database.csv'. It computes the subtotal and tax to determine
    the total cost of the order and formats the ordered items into a readable string.

    The method checks if the file already contains headers. If not, it adds them before appending the order details.
    Each order's details include the order number, customer name, delivery date, shipping address, order status,
    detailed order items, and the total cost.

    Raises:
        FileNotFoundError: If the 'order_database.csv' file does not exist, it handles this exception by creating
        a new file and writing the header.
    """
    subtotal = sum(item['price'] * item['quantity'] for item in self.shopping_cart.items.values())
    tax = subtotal * 0.08
    total_cost = subtotal + tax
    order_details = '; '.join([f"{item['name']} (x{item['quantity']})" for item in self.shopping_cart.items.values()])

    headers = ['Order Number', 'Customer Name', 'Delivery Date', 'Shipping Address', 'Status', 'Order Details', 'Total Cost']
    try:
        with open('order_database.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            has_headers = next(reader, None)
    except FileNotFoundError:
        has_headers = False

    with open('order_database.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        if not has_headers:
            writer.writeheader()
        writer.writerow({
            'Order Number': self.order_number,
            'Customer Name': self.name,
            'Delivery Date': self.delivery_date,
            'Shipping Address': self.shipping_address,
            'Status': self.status,
            'Order Details': order_details,
            'Total Cost': f"${total_cost:.2f}"
        })

  def print_receipt(self, shopping_cart):
    """
    Prints the receipt for the order. It displays the order number and then calls the `print_receipt` method
    on the ShoppingCart instance to print each item in the cart along with its quantity and price, and the total cost.

    Args:
        shopping_cart (ShoppingCart): The ShoppingCart object containing the items in the current order.
    """
    print(f"Receipt for Order #{self.order_number}")
    shopping_cart.print_receipt()



  