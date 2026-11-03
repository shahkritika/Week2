# A2: Save and load inventory as JSON (self-contained)
import json
import os

class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"[{self.item_id}] {self.name} | Qty: {self.quantity} | Price: ${self.price:.2f}"

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity, price):
        self.items[item_id] = Item(item_id, name, quantity, price)
        print(f"Added: {self.items[item_id]}")

    def list_items(self):
        if not self.items:
            print("Inventory is empty.")
            return
        print("\n=== Inventory ===")
        for item in self.items.values():
            print(f"  {item}")
        print(f"Total items: {len(self.items)}\n")

DATA_FILE = "inventory_data.json"

def save_inventory(inventory, filepath=DATA_FILE):
    data = {}
    for item_id, item in inventory.items.items():
        data[item_id] = {"name": item.name, "quantity": item.quantity, "price": item.price}
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Inventory saved to '{filepath}'")


def load_inventory(filepath=DATA_FILE):
    inventory = Inventory()
    if not os.path.exists(filepath):
        print(f"No saved inventory found at '{filepath}'.")
        return inventory
    with open(filepath, "r") as f:
        data = json.load(f)
    for item_id, info in data.items():
        inventory.items[item_id] = Item(item_id, info["name"], info["quantity"], info["price"])
    print(f"Inventory loaded from '{filepath}'")
    return inventory


# --- Test ---
inv = Inventory()
inv.add_item("001", "Notebook", 30, 2.99)
inv.add_item("002", "Pen", 150, 0.75)
inv.add_item("003", "Eraser", 80, 0.50)
inv.list_items()

save_inventory(inv)

print("\nLoading inventory from file...")
inv2 = load_inventory()
inv2.list_items()
