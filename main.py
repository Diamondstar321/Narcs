import csv
import os
from prescription import Prescription
from order import Order
from menu_definitions import menu_main, home_menu, admin_menu
from menu import Menu
from option import Option
from session import Session
from shopping_cart import ShoppingCart
from datetime import datetime, timedelta

def login(session):
    """
    Authenticate a user based on username and password.
    Args:
        session (Session): The current session object which holds session data.
    Returns:
        None: Modifies the session state depending on authentication success.
    """
    username = input("Username: ")
    password = input("Password: ")
    with open('account_information.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['UserName'] == username and row['Password'] == password:
                session.logged_in = True
                session.user_data = {"UserName": username, "IsEmployee": row['IsEmployee']}
                if row['IsEmployee'].lower() == 'true':
                    session.current_menu = admin_menu
                    print("Login successful! Welcome, Admin.")
                else:
                    session.current_menu = home_menu
                    print("Login successful! Welcome, User.")
                return
        print("Invalid credentials!")

def logout(session):
    """
    Logs out the current user and resets the session.
    Args:
        session (Session): The current session object to be modified.
    Returns:
        None: Resets the user's session state.
    """
    session.logged_in = False
    session.user_data = None
    session.current_menu = menu_main
    print("Logged out.\n")

def register(session):
    """
    Registers a new user by asking for user details and storing them.
    Args:
        session (Session): The current session object.
    Returns:
        None: Updates the account information database with new user details.
    """
    if session.logged_in:
        print("Already logged in. Log out to create a new account.")
        return
    full_name = input("Full name: ")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    admin = input("Are you an employee? (y/n): ")
    is_employee = False
    if admin.lower() == 'y':
        honesty = input('Are you telling the truth? (y/n): ')
        if honesty.lower() == 'y':
            is_employee = True

    file_exists = os.path.isfile('account_information.csv')
    with open('account_information.csv', 'a', newline='') as csvfile:
        fieldnames = ['FullName', 'UserName', 'Password', 'IsEmployee']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'FullName': full_name, 'UserName': username, 'Password': password, 'IsEmployee': is_employee})
    print("\nAccount created for username:", username)

def create_account(session):
    """
    Facilitates the creation of a user account.
    Args:
        session (Session): The current session object.
    Returns:
        None: Delegates to the `register` function.
    """
    register(session)

def manage_account_info(session):
    """
    Allows viewing and manipulation of account information in the database.
    Args:
        session (Session): The current session object.
    Returns:
        None: Can modify account data or simply list accounts.
    """
    print("\nAccount Information Database")
    while True:
        choice = input("\n1. View Accounts\n2. Add New Account\n3. Delete Account\n4. Return to Main Menu\nSelect an option: ")
        print('')
        if choice == '1':
            # View all accounts
            try:
                with open('account_information.csv', 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    # Print headers based on the fieldnames attribute of the reader
                    if reader.fieldnames:
                        print(f"{'Full Name':<20} {'User Name':<20} {'Is Employee':<12}")
                        print("="*54)
                    for row in reader:
                        print(f"{row['FullName']:<20} {row['UserName']:<20} {row['IsEmployee']:<12}")
            except FileNotFoundError:
                print("No account information available.")
        elif choice == '2':
            #Add a new account
            full_name = input("Full name: ")
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            is_employee = input("Is this user an employee? (y/n): ").lower() == 'y'
            file_exists = os.path.isfile('account_information.csv')
            with open('account_information.csv', 'a', newline='') as csvfile:
                fieldnames = ['FullName', 'UserName', 'Password', 'IsEmployee']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow({'FullName': full_name, 'UserName': username, 'Password': password, 'IsEmployee': is_employee})
            print("New account added successfully.")
        elif choice == '3':
            #Delete an account
            username_to_delete = input("Enter the username of the account to delete: ")
            accounts = []
            deleted = False
            with open('account_information.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['UserName'] != username_to_delete:
                        accounts.append(row)
                    else:
                        deleted = True
            if deleted:
                with open('account_information.csv', 'w', newline='') as csvfile:
                    fieldnames = ['FullName', 'UserName', 'Password', 'IsEmployee']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(accounts)
                print(f"Account for username '{username_to_delete}' deleted successfully.")
            else:
                print("Account not found.")
        elif choice == '4':
            return
        else:
            print("Invalid option selected.")


def manage_customer_orders(session):
    """
    Manages customer orders by viewing and updating order statuses.
    Args:
        session (Session): The current session object.
    Returns:
        None: Allows admin to update the status of orders.
    """
    print("\n--- Customer Orders ---")
    try:
        with open('order_database.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames if reader.fieldnames is not None else ['Order Number', 'Customer Name', 'Order Details', 'Status', 'Shipping Address', 'Total Cost']
            orders = list(reader)

            if not orders:
                print("No orders available.")
                return

            for order in orders:
                print("\nOrder Information:")
                print(f"{'Order Number':<15}: {order['Order Number']}")
                print(f"{'Customer Name':<15}: {order['Customer Name']}")
                print(f"{'Order Details':<15}: {order['Order Details']}")
                print(f"{'Status':<15}: {order['Status']}")
                print(f"{'Shipping Address':<15}: {order['Shipping Address']}")
                print(f"{'Total Cost':<15}: {order['Total Cost']}")

        status_options = {
            '1': 'Order Placed',
            '2': 'Order Shipped',
            '3': 'Order Delivered',
            '4': 'Order Cancelled'
        }

        order_number = input("\nEnter Order Number to update status, or 'exit' to return: ")
        if order_number.lower() == 'exit':
            return

        print("\nSelect new status:")
        for key, value in status_options.items():
            print(f"{key}: {value}")

        status_choice = input("Enter choice (1-4): ")
        new_status = status_options.get(status_choice, None)
        if new_status is None:
            print("Invalid status choice. Returning to menu.")
            return

        order_found = False
        for order in orders:
            if order['Order Number'] == order_number:
                order['Status'] = new_status
                print(f"Order {order_number} status updated to {new_status}.")
                order_found = True
                break
        if not order_found:
            print("Order Number not found.")

        # Save updates back to the CSV file
        with open('order_database.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(orders)

    except FileNotFoundError:
        print("The order database file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def manage_inventory(session):
    """
    Provides inventory management functionalities.
    Args:
        session (Session): The current session object which may dictate access level.
    Returns:
        None: Allows for viewing, adding, updating, or deleting inventory items.
    """
    while True:
        print("\nPrescription Inventory Management")
        choice = input("\n1. View Full Inventory\n2. Add New Item\n3. Update Item\n4. Delete Item\n5. Return to Admin Menu\nSelect an option: ")
        print('')

        if choice == '1':
            try:
                with open('prescription_database.csv', 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    if not reader.fieldnames:
                        print("The inventory file is empty.")
                        return
                    print(f"{'Product Name':<20} {'Expiration Date':<12} {'Price':<10} {'Stock':<10}")
                    for row in reader:
                        print(f"{row['Name']:<20} {row['Expiration Date']:<12} ${row['Price']:<10} {row['Stock']:<10}")
            except FileNotFoundError:
                print("The pharmacy inventory file does not exist.")
            except KeyError:
                print("Error reading from the inventory file. Please check the data format.")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == '2':
            name = input("Enter drug name: ")
            while True:
                expiration_date = input("Enter new expiration date (Months (1-12)): ")
                if expiration_date.isdigit() and 1 <= int(expiration_date) <= 12:
                    break
                else:
                    print("Invalid input. Please enter a month between 1 and 12.")
            price = int(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            new_prescription = Prescription(name, expiration_date, price, stock)
            Prescription.add_prescription(new_prescription)
            print("New inventory item added successfully.")

        elif choice == '3':
            existing_name = input("Enter the name of the prescription to update: ").strip().lower()
            prescriptions = Prescription.read_prescriptions()
            prescription_found = any(prescription['Name'].strip().lower() == existing_name for prescription in prescriptions)
            if not prescription_found:
                print("Prescription not found.")
            else:
                updated = False
                for prescription in prescriptions:
                    if prescription['Name'].strip().lower() == existing_name:
                        expiration_date = input("Enter new expiration date (Months (1-12)): ")
                        while not (expiration_date.isdigit() and 1 <= int(expiration_date) <= 12):
                            print("Invalid input. Please enter a month between 1 and 12.")
                            expiration_date = input("Enter new expiration date (Months (1-12)): ")
                        price = int(input("Enter new price: "))
                        stock = int(input("Enter new stock quantity: "))
                        updated_prescription = Prescription(prescription['Name'], expiration_date, price, stock)
                        Prescription.update_prescription(prescription['Name'], updated_prescription)
                        updated = True
                        break
                if updated:
                    print("Prescription updated successfully.")

        elif choice == '4':
            name_to_delete = input("Enter the name of the item to delete: ").strip().lower()
            if Prescription.delete_prescription(name_to_delete):
                print(f"Prescription '{name_to_delete}' deleted successfully.")
            else:
                print("Prescription deleted.")

        elif choice == '5':
            return

        else:
            print("Invalid option selected.")


def view_pharmacy_inventory(session):
    """
    Displays the inventory of available pharmacy items.
    Args:
        session (Session): The current session object.
    Returns:
        None: Outputs the list of available pharmacy items to the console.
    """
    print("\n--- Pharmacy Inventory ---")
    try:
        with open('prescription_database.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames:
                print("The inventory file is empty.")
                return
            expected_fields = ["Name", "Expiration Date", "Price", "Stock"]
            if not all(field in reader.fieldnames for field in expected_fields):
                print("Missing required columns in the inventory file.")
                return
            print(f"{'Product Name':<20} {'Price':<10} {'Stock':<10}")
            for row in reader:
                name = row['Name']
                price = row['Price']
                stock = row['Stock']
                print(f"{name:<20} ${price:<10} {stock:<10}")
    except FileNotFoundError:
        print("The pharmacy inventory file does not exist.")
    except KeyError:
        print("Error reading from the inventory file. Please check the data format.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_new_order(session):
    """
    Facilitates the creation of a new order by the customer, adding items to a shopping cart and selecting a payment method.
    Args:
        session (Session): The current session object.
    Returns:
        None: Outputs the result of the order process, including a receipt if successful.
    """
    shopping_cart = ShoppingCart()
    prescriptions = Prescription.read_prescriptions()

    print("\nAvailable Prescriptions:")
    for idx, prescription in enumerate(prescriptions, start=1):
        print(f"{idx}. {prescription['Name']} - ${prescription['Price']} (Stock: {prescription['Stock']})")

    while True:
        choice = input("\nEnter prescription number to add to cart or type 'done' to finalize: ")
        if choice.lower() == 'done':
            if not shopping_cart.items:
                print("No items in your cart to finalize. Please add some items.")
                continue
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(prescriptions):
            idx = int(choice) - 1
            selected_prescription = prescriptions[idx]
            quantity = int(input(f"Enter quantity for {selected_prescription['Name']}: "))
            if quantity <= int(selected_prescription['Stock']):
                shopping_cart.add_item(selected_prescription, quantity)
            else:
                print(f"Not enough stock for {selected_prescription['Name']}. Available stock: {selected_prescription['Stock']}")
        else:
            print("Invalid choice. Please select a valid prescription number.")

    print("\nSelect a payment method:")
    print("1: Card")
    print("2: PayPal")
    print("3: Pay-in-4")
    payment_method = input("Enter your payment option (1-3): ")
    payment_methods = {
        '1': 'Card',
        '2': 'PayPal',
        '3': 'Pay-in-4'
    }
    
    for item_name, details in shopping_cart.items.items():
        for prescription in prescriptions:
            if prescription['Name'] == item_name:
                prescription['Stock'] = str(int(prescription['Stock']) - details['quantity'])

    Prescription.update_prescription_database(prescriptions)

    customer_name = session.user_data.get('UserName', 'Unknown Customer')
    order_number = generate_order_number()
    delivery_date = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
    shipping_address = input("Enter shipping address: ")
    status = "Order Placed"

    new_order = Order(customer_name, order_number, shopping_cart, delivery_date, shipping_address, status)
    new_order.print_receipt(shopping_cart)
    new_order.save_to_order_database()
    print("Order created successfully and receipt printed.")
    return


def generate_order_number():
    """
    Generates a random order number for new orders.
    Returns:
        int: A random number between 1000 and 9999 as the order number.
    """
    import random
    return random.randint(1000, 9999)


def view_order_history(session):
    """
    Allows a customer to view their order history.
    Args:
        session (Session): The current session object containing user details.
    Returns:
        None: Displays the order history of the logged-in customer.
    """
    customer_name = session.user_data.get('UserName')
    if not customer_name:
        print("No customer information found. Please log in.")
        return

    print("\n--- Your Order History ---")
    try:
        with open('order_database.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            default_fieldnames = ['Order Number', 'Customer Name', 'Order Details', 'Status', 'Shipping Address', 'Total Cost']
            fieldnames = reader.fieldnames if reader.fieldnames is not None else default_fieldnames
            orders = list(reader)

            if not orders:
                print("No order history available.")
                return

            for order in orders:
                if order['Customer Name'] == customer_name:
                    print("\nOrder Information:")
                    print(f"{'Order Number':<15}: {order['Order Number']}")
                    print(f"{'Customer Name':<15}: {order['Customer Name']}")
                    print(f"{'Order Details':<15}: {order['Order Details']}")
                    print(f"{'Status':<15}: {order['Status']}")
                    print(f"{'Shipping Address':<15}: {order['Shipping Address']}")
                    print(f"{'Total Cost':<15}: {order['Total Cost']}")

            order_number = input("\nEnter Order Number to CANCEL, or type 'exit' to return: ")
            if order_number.lower() == 'exit':
                return

            for order in orders:
                if order['Order Number'] == order_number and order['Customer Name'] == customer_name:
                    if order['Status'] in ['Order Placed', 'Order Shipped']:
                        order['Status'] = 'Cancelled'
                        print(f"Order {order_number} has been cancelled.")
                        break
                    else:
                        print("This order cannot be cancelled.")
                        break
            else:
                print("Order number not found or does not belong to you.")

            with open('order_database.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(orders)

    except FileNotFoundError:
        print("The order database file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_account_information(session):
    """
    Allows users to edit their account information.
    Args:
        session (Session): The current session object.
    Returns:
        None: Updates the user's account information based on input.
    """
    if not session.logged_in:
        print("You must be logged in to edit account information.")
        return

    print("\n--- Edit Account Information ---")
    current_username = session.user_data['UserName']

    try:
        with open('account_information.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            accounts = list(reader)

        new_username = input("Enter your new username (leave blank to keep current): ").strip()
        new_password = input("Enter your new password (leave blank to keep current): ").strip()

        for account in accounts:
            if account['UserName'] == current_username:
                if new_username:
                    if any(acc['UserName'] == new_username for acc in accounts if acc['UserName'] != current_username):
                        print("Username already exists. Try a different username.")
                        return
                    account['UserName'] = new_username
                if new_password:
                    account['Password'] = new_password
                break

        with open('account_information.csv', 'w', newline='') as csvfile:
            fieldnames = ['FullName', 'UserName', 'Password', 'IsEmployee']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(accounts)

        session.user_data['UserName'] = new_username if new_username else current_username
        print("Account information updated successfully.")

    except FileNotFoundError:
        print("The account database file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    The main function that runs the main loop of the program, handling user inputs and actions.
    Returns:
        None: Keeps running until the user decides to exit the application.
    """
    session = Session()
    globals_dict = {
        "session": session,
        "login": login,
        "logout": logout,
        "register": register,
        "create_account": create_account,
        "manage_account_info": manage_account_info,
        "manage_inventory": manage_inventory,
        "view_pharmacy_inventory": view_pharmacy_inventory,
        "create_new_order": create_new_order,
        "manage_customer_orders": manage_customer_orders,
        "view_order_history": view_order_history,
        "edit_account_information": edit_account_information
    }

    while True:
        action_text = session.current_menu.menu_prompt()
        if action_text == "pass":
            print("Application has been exited.")
            break
        exec(action_text, globals_dict)

if __name__ == "__main__":
    main()
