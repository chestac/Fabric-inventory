from material import Material
from inventory import Inventory
import os

my_inventory = Inventory()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Directory:", os.getcwd())  # Shows the working directory
print("Files in Directory:", os.listdir())  # Lists all files


def add_fabric_type():
    #Adds a new fabric type and price, ensuring it's saved and available immediately.
    name = input("Enter new fabric type: ").strip().title()
    
    if name in my_inventory.available_fabrics:
        print("⚠️ Fabric type already exists!")
        return
    
    try:
        price = float(input(f"Enter price per yard for {name}: "))

        # Save to fabrics.txt
        with open("fabrics.txt", "a") as file:
            file.write(f"{name},{price}\n")

        #Reload fabric types so the user can select them immediately
        my_inventory.load_fabric_types()

        print(f"✅ {name} added with price ${price:.2f} per yard.")
    except ValueError:
        print("❌ Invalid input. Please enter a number for price.")



def add_fabric_inventory():
    #Adds fabric to the inventory with color selection.
    available_fabrics = my_inventory.get_fabric_list()
    if not available_fabrics:
        print("❌ No fabric types available. Please add a fabric type first!")
        return
    
    print("\n📜 Available Fabric Types:")
    for i, fabric in enumerate(available_fabrics, start=1):
        print(f"{i}. {fabric}")
    
    try:
        choice = int(input(f"Select a fabric type (1-{len(available_fabrics)}): "))
        selected_fabric = available_fabrics[choice - 1]
        color = input("Enter fabric color: ")
        quantity = float(input(f"Enter the number of yards for {selected_fabric}: "))
        price_per_unit = my_inventory.available_fabrics[selected_fabric]
        my_inventory.add_material(Material(selected_fabric, color, quantity, "yards", price_per_unit))
        print(f"✅ Added {quantity} yards of {color} {selected_fabric} to inventory.")
    except (ValueError, IndexError):
        print("❌ Invalid selection. Please try again.")

def remove_fabric_inventory():
    #Removes fabric from the inventory.
    name = input("Enter fabric name to remove: ")
    color = input("Enter fabric color: ")
    quantity = float(input("Enter the number of yards to remove: "))
    my_inventory.remove_material(name, color, quantity)

my_inventory = Inventory()

def view_inventory():
    # Displays the inventory in a formatted table.
    my_inventory.list_inventory()  # Ensure this matches the function name in inventory.py


if __name__ == "__main__":
    while True:
        print("\n🧵\t  Sewing Inventory System\t  🪡")
        print("1️⃣ \t Add Fabric Type")
        print("2️⃣ \t Add Fabric to Inventory")
        print("3️⃣ \t Remove Fabric from Inventory")
        print("4️⃣ \t View Inventory")
        print("5️⃣ \t Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            add_fabric_type()
        elif choice == "2":
            add_fabric_inventory()
        elif choice == "3":
            remove_fabric_inventory()
        elif choice == "4":
            my_inventory.list_inventory()
        elif choice == "5":
            print("👋 Exiting... Happy sewing! 😎")
            break
        else:
            print("❌ Invalid option. Try again.")