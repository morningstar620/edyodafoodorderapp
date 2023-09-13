#foodordering_app

class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

class Admin:
    def __init__(self):
        self.food_items = [FoodItem(1, "Tandoori Chicken", "4 piece", 240.0, 10, 50),
            FoodItem(2, "Vegan Burger", "1 piece", 320.0, 15, 30),
            FoodItem(3, "Tuffle Cake", "500 mg", 900.0, 5, 4000),]

def display_food_menu(food_items):
    print("Food Menu:")
    for i, item in enumerate(food_items):
        print(f"{i+1}. {item.name} ({item.quantity}) [INR {item.price}]")

def admin_add_food(admin, name, quantity, price, discount, stock):
    food_id = len(admin.food_items) + 1  # Generate a food ID by counting existing items
    food_item = FoodItem(food_id, name, quantity, price, discount, stock)
    admin.food_items.append(food_item)
    print(f"Food ID: {food_id} - {name} added to the menu.")

def admin_edit_food(admin, food_id, name, quantity, price, discount, stock):
    for item in admin.food_items:
        if item.food_id == food_id:
            item.name = name
            item.quantity = quantity
            item.price = price
            item.discount = discount
            item.stock = stock
            print(f"Food item with ID {food_id} edited successfully.")
            return
    print(f"Food item with ID {food_id} not found.")

def admin_remove_food(admin, food_id):
    for item in admin.food_items:
        if item.food_id == food_id:
            admin.food_items.remove(item)
            print(f"Food item with ID {food_id} removed from the menu.")
            return
    print(f"Food item with ID {food_id} not found.")

def user_register(users, full_name, phone_number, email, address, password):
    user = User(full_name, phone_number, email, address, password)
    users.append(user)
    print(f"User {full_name} registered successfully.")

def user_login(users, email, password):
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None

def user_place_order(user, food_items, selected_items):
    total_cost = 0
    order_details = []
    for index in selected_items:
        if 0 < index <= len(food_items):
            food_item = food_items[index - 1]
            total_cost += food_item.price
            order_details.append(f"{food_item.name} ({food_item.quantity}) [INR {food_item.price}]")

    if total_cost == 0:
        print("No items selected for the order.")
        return


    print("Selected items for the order:")
    for item in order_details:
        print(item)
    print(f"Total Cost: INR {total_cost}")
    confirm_order=input("confirm the order: yes/no")
    if confirm_order == 'yes':
        user.orders.append(order_details)
        print("Order placed successfully.")
    elif confirm_order =='no' :
         print("order cancelled")
    else :
         print("invalid choice")

def user_view_order_history(user):
    if not user.orders:
        print("No order history available.")
        return

    print("Order History:")
    for i, order in enumerate(user.orders, start=1):
        print(f"Order {i}:")
        for item in order:
            print(item)


def user_update_profile(user, full_name, phone_number, address, password):
    user.full_name = full_name
    user.phone_number = phone_number
    user.address = address
    user.password = password
    print("User profile updated successfully.")

if __name__ == "__main__":
    admin = Admin()
    users = []

    while True:
        print("\nWelcome to the Food Ordering App!")
        print("1. Admin Login")
        print("2. User Register")
        print("3. User Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Admin Login
            admin_password = input("Enter admin password: ")
            if admin_password == "adminpass":
                while True:
                    print("\nAdmin Menu:")
                    print("1. Add New Food Item")
                    print("2. Edit Food Item")
                    print("3. View Food Menu")
                    print("4. Remove Food Item")
                    print("5. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        # Add New Food Item
                        name = input("Enter food name: ")
                        quantity = input("Enter quantity: ")
                        price = float(input("Enter price: "))
                        discount = float(input("Enter discount: "))
                        stock = int(input("Enter stock: "))
                        admin_add_food(admin, name, quantity, price, discount, stock)

                    elif admin_choice == "2":
                        # Edit Food Item
                        food_id = int(input("Enter FoodID to edit: "))
                        name = input("Enter new food name: ")
                        quantity = input("Enter new quantity: ")
                        price = float(input("Enter new price: "))
                        discount = float(input("Enter new discount: "))
                        stock = int(input("Enter new stock: "))
                        admin_edit_food(admin, food_id, name, quantity, price, discount, stock)

                    elif admin_choice == "3":
                        # View Food Menu
                        display_food_menu(admin.food_items)

                    elif admin_choice == "4":
                        # Remove Food Item
                        food_id = int(input("Enter FoodID to remove: "))
                        admin_remove_food(admin, food_id)

                    elif admin_choice == "5":
                        # Logout
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Admin login failed. Incorrect password.")

        elif choice == "2":
            # User Register
            full_name = input("Enter your full name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Enter your password: ")
            user_register(users, full_name, phone_number, email, address, password)

        elif choice == "3":
            # User Login
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            logged_user = user_login(users, email, password)
            if logged_user:
                while True:
                    print("\nUser Menu:")
                    print("1. Place New Order")
                    print("2. Order History")
                    print("3. Update Profile")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        # Place New Order
                        display_food_menu(admin.food_items)
                        selected_items = [int(x) for x in input("Enter food item numbers (e.g., 1 2 3): ").split()]
                        user_place_order(logged_user, admin.food_items, selected_items)

                    elif user_choice == "2":
                        # Order History
                        user_view_order_history(logged_user)

                    elif user_choice == "3":
                        # Update Profile
                        full_name = input("Enter new full name: ")
                        phone_number = input("Enter new phone number: ")
                        address = input("Enter new address: ")
                        password = input("Enter new password: ")
                        user_update_profile(logged_user, full_name, phone_number, address, password)

                    elif user_choice == "4":
                        # Logout
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("User login failed. Incorrect email or password.")

        elif choice == "4":
            # Exit
            print("Thank you for using the Food Ordering App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
