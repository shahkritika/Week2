# A1: Item and Inventory classes — add, remove, update, list

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
        self.items = {}  # item_id -> Item

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            print(f"Item '{item_id}' already exists. Use update instead.")
            return
        self.items[item_id] = Item(item_id, name, quantity, price)
        print(f"Added: {self.items[item_id]}")

    def remove_item(self, item_id):
        if item_id not in self.items:
            print(f"Item '{item_id}' not found.")
            return
        removed = self.items.pop(item_id)
        print(f"Removed: {removed}")

    def update_item(self, item_id, quantity=None, price=None):
        if item_id not in self.items:
            print(f"Item '{item_id}' not found.")
            return
        item = self.items[item_id]
        if quantity is not None:
            item.quantity = quantity
        if price is not None:
            item.price = price
        print(f"Updated: {item}")

    def list_items(self):
        if not self.items:
            print("Inventory is empty.")
            return
        print("\n=== Inventory ===")
        for item in self.items.values():
            print(f"  {item}")
        print(f"Total items: {len(self.items)}\n")


# --- Test ---
inv = Inventory()
inv.add_item("001", "Apple", 100, 0.50)
inv.add_item("002", "Banana", 50, 0.25)
inv.add_item("003", "Cherry", 200, 1.99)
inv.list_items()
inv.update_item("002", quantity=75, price=0.30)
inv.remove_item("001")
inv.list_items()

