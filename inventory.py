import pandas as pd
from material import Material

class Inventory:
    def __init__(self):
 # Creates an inventory to store active materials.   
        self.active_materials = []  # Available materials list
        self.available_fabrics = {}  # Stores fabric types and prices
        self.load_inventory()
        self.load_fabric_types()

    def add_material(self, material):
 # Adds a new material to the active inventory.   
        self.active_materials.append(material)
        self.save_inventory()

    def remove_material(self, name, color, quantity):
 # Removes fabric from inventory.   
        for material in self.active_materials:
            if material.name == name and material.color == color:
                if material.quantity >= quantity:
                    material.update_quantity(-quantity)
                    self.save_inventory()
                    print(f"✅ Removed {quantity} {material.unit} of {color} {name} from inventory.")
                    return
                else:
                    print("❌ Not enough material to remove!")
                    return
        print("❌ Material not found!")

    def list_inventory(self):
 #Displays all materials in active inventory as a Pandas DataFrame.   
        data = [[m.get_name(), m.get_color(), m.get_quantity(), m.get_unit(), m.get_price_per_unit(), m.get_calculate_total_cost()] for m in self.active_materials]
        df = pd.DataFrame(data, columns=["Name", "Color", "Quantity", "Unit", "Price per Unit", "Total Cost"])
        if df.empty:
            print("❌ No materials in inventory.")
        else:
            print("🪡 Active Inventory:")
            # Prints table to see inventory table 
            print(df.to_string(index=False))

    def save_inventory(self):
 # Saves inventory to a file.   
        data = [[m.name, m.color, m.quantity, m.unit, m.price_per_unit] for m in self.active_materials]
        df = pd.DataFrame(data, columns=["Name", "Color", "Quantity", "Unit", "Price per Unit"])
        df.to_csv("inventory.txt", index=False)

    def load_inventory(self):
 # Loads inventory from a file.   
        try:
            df = pd.read_csv("inventory.txt")
            for _, row in df.iterrows():
                self.active_materials.append(Material(row["Name"], row["Color"], row["Quantity"], row["Unit"], row["Price per Unit"]))
        except FileNotFoundError:
            pass  # No inventory saved yet

    def load_fabric_types(self):
 # Loads fabric types and prices from a file.   
        try:
            df = pd.read_csv("fabrics.txt", header=None, names=["Name", "Price"])
            self.available_fabrics = {row["Name"]: row["Price"] for _, row in df.iterrows()}
        except FileNotFoundError:
            self.available_fabrics = {}

    def get_fabric_list(self):
 #Returns the list of available fabric types from the file.   
        return list(self.available_fabrics.keys())