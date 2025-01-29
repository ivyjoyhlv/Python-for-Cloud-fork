# Student A: Define the Item class representing an item in the inventory
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

# Student B: Define the Inventory class  representing the inventory system
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def total_value(self):
        return sum(item.total_cost() for item in self.items)

# Student C: Write a test function
def test_inventory_system():
    inv = Inventory()
    
    # Create sample items
    item1 = Item("Butter Cookies", 50, 5)
    item2 = Item("Sweet Tarts", 100, 2)
    item3 =  Item("Chocolate Cookies", 68, 4)
    
    # Add items to inventory
    inv.add_item(item1)
    inv.add_item(item2)
    inv.add_item(item3)
    
    # Print total inventory value
    print("Total Inventory Value:", inv.total_value())

# Student D: Runs the inventory
if __name__ == "__main__":
    test_inventory_system()
