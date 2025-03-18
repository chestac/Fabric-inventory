import csv

class Material:
   
    def __init__(self, name, color, quantity, unit, price_per_unit):
        # Creates a new material    
        self.name = name
        self.color = color
        self.quantity = quantity
        self.unit = unit 
        self.price_per_unit = price_per_unit

    
    def get_name(self):
        return self.name

    
    def get_color(self):
        return self.color

    
    def get_quantity(self):
        return self.quantity

    def get_unit(self):
        return self.unit
    
    
    def get_price_per_unit(self):
        return self.price_per_unit
    
    def set_quantity(self, value):
        if value < 0:
            raise ValueError("❌ Quantity cannot be negative!")
        self._quantity = value

    def set_update_quantity(self, amount):
         #  Updates the quantity (adds or subtracts)
        self.quantity += amount

    def get_calculate_total_cost(self):
         # Calculates total cost of the material
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"🧵 {self.name} ({self.color}): {self.quantity} {self.unit} ($ {self.calculate_total_cost():.2f})"