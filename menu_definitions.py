from menu import Menu
from option import Option

menu_main = Menu('Main', 'Please select one of the following options:', [
    Option("Login", "login(session)"),
    Option("Register", "create_account(session)"),
    Option("Exit this application", "pass")
])

home_menu = Menu('home', '\nHome (CUSTOMER):', [
    Option("View Pharmacy Inventory", "view_pharmacy_inventory(session)"),
    Option("Create a New Order", 'create_new_order(session)'),
    Option("View Order History", 'view_order_history(session)'),
    Option("Sign Out", "logout(session)")
])


admin_menu = Menu('admin', '\nHome (ADMIN):', [
    Option("Prescription Inventory Management", 'manage_inventory(session)'),
    Option("Account Information Database and Management", 'manage_account_info(session)'),
    Option("Customer Orders", 'manage_customer_orders(session)'),
    Option("Sign Out", "logout(session)")
])
