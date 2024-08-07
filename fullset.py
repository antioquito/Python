# Sample Menu Script with Multiple Prices

# Define the menu with items and their prices
menu = {
    "Coffee": {"Small": 2.50, "Medium": 3.00, "Large": 3.50},
    "Tea": {"Small": 2.00, "Medium": 2.50, "Large": 3.00},
    "Sandwich": {"Small": 4.00, "Medium": 5.50, "Large": 7.00},
    "Salad": {"Small": 3.50, "Medium": 4.50, "Large": 5.50},
    "Smoothie": {"Small": 3.50, "Medium": 4.50, "Large": 5.50}
}

# Function to display the menu
def display_menu():
    print("Welcome to the Café!")
    print("Here is our menu:")
    for item, sizes in menu.items():
        print(f"\n{item}:")
        for size, price in sizes.items():
            print(f"  {size}: ${price:.2f}")

# Function to view the price of a selected item
def view_price():
    item = input("\nEnter the item name: ").title()
    if item in menu:
        size = input("Enter the size (Small, Medium, Large): ").title()
        if size in menu[item]:
            print(f"The price of {item} ({size}) is ${menu[item][size]:.2f}")
        else:
            print("Invalid size. Please choose Small, Medium, or Large.")
    else:
        print("Invalid item. Please choose an item from the menu.")

# Main function to run the program
def main():
    while True:
        print("\n1. Display Menu")
        print("2. View Price of Item")
        print("3. Exit")
        choice = input("Please choose an option (1-3): ")
        
        if choice == "1":
            display_menu()
        elif choice == "2":
            view_price()
        elif choice == "3":
            print("Thank you for visiting the Café!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the main function
if __name__ == "__main__":
    main()
