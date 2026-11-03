# A1: Finished CLI Inventory System with full OOP, JSON persistence, and GitHub PR workflow

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "inventory_data.json")


class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id  = item_id
        self.name     = name
        self.quantity = int(quantity)
        self.price    = float(price)

    def to_dict(self):
        return {
            "item_id":  self.item_id,
            "name":     self.name,
            "quantity": self.quantity,
            "price":    self.price,
        }

    def __str__(self):
        return f"[{self.item_id}] {self.name:<20} Qty: {self.quantity:<6} Price: ${self.price:.2f}"


class Inventory:
    def __init__(self):
        self.items = {}

    # ── CRUD ─────────────────────────────────────────────────────────────────
    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            print(f"  [!] Item '{item_id}' already exists. Use 'update'.")
            return
        self.items[item_id] = Item(item_id, name, quantity, price)
        print(f"  [+] Added:   {self.items[item_id]}")

    def remove_item(self, item_id):
        if item_id not in self.items:
            print(f"  [!] Item '{item_id}' not found.")
            return
        print(f"  [-] Removed: {self.items.pop(item_id)}")

    def update_item(self, item_id, quantity=None, price=None):
        item = self.items.get(item_id)
        if not item:
            print(f"  [!] Item '{item_id}' not found.")
            return
        if quantity is not None: item.quantity = int(quantity)
        if price    is not None: item.price    = float(price)
        print(f"  [~] Updated: {item}")

    def list_items(self):
        if not self.items:
            print("  Inventory is empty.")
            return
        print(f"\n  {'ID':<8} {'Name':<20} {'Qty':<8} {'Price'}")
        print("  " + "-" * 48)
        for item in self.items.values():
            print(f"  {item}")
        print(f"\n  Total: {len(self.items)} item(s)\n")

    def search(self, keyword):
        results = [i for i in self.items.values() if keyword.lower() in i.name.lower()]
        if not results:
            print(f"  No items matching '{keyword}'.")
            return
        print(f"\n  Search results for '{keyword}':")
        for item in results:
            print(f"  {item}")

    # ── Persistence ──────────────────────────────────────────────────────────
    def save(self, filepath=DATA_FILE):
        with open(filepath, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.items.items()}, f, indent=4)
        print(f"  [OK] Saved to '{filepath}'")

    def load(self, filepath=DATA_FILE):
        if not os.path.exists(filepath):
            return
        with open(filepath, "r") as f:
            data = json.load(f)
        loaded_items = {}
        for d in data.values():
            item = Item(d["item_id"], d["name"], d["quantity"], d["price"])
            loaded_items[item.item_id] = item
        self.items = loaded_items
        print(f"  [OK] Loaded {len(self.items)} item(s) from '{filepath}'")


# ── CLI Menu ─────────────────────────────────────────────────────────────────
def menu():
    print("\n" + "=" * 50)
    print("   CLI Inventory Manager - Milestone 1")
    print("=" * 50)
    print("  1. List all items")
    print("  2. Add item")
    print("  3. Update item")
    print("  4. Remove item")
    print("  5. Search item")
    print("  6. Save & Exit")
    print("=" * 50)
    return input("  Choice: ").strip()


def run():
    inv = Inventory()
    inv.load()

    while True:
        choice = menu()
        if choice == "1":
            inv.list_items()
        elif choice == "2":
            iid = input("  Item ID   : ").strip()
            nam = input("  Name      : ").strip()
            qty = input("  Quantity  : ").strip()
            prc = input("  Price ($) : ").strip()
            inv.add_item(iid, nam, qty, prc)
        elif choice == "3":
            iid = input("  Item ID        : ").strip()
            qty = input("  New Quantity (Enter to skip): ").strip() or None
            prc = input("  New Price    (Enter to skip): ").strip() or None
            inv.update_item(iid, qty, prc)
        elif choice == "4":
            iid = input("  Item ID: ").strip()
            inv.remove_item(iid)
        elif choice == "5":
            kw = input("  Search keyword: ").strip()
            inv.search(kw)
        elif choice == "6":
            inv.save()
            print("  Goodbye!\n")
            break
        else:
            print("  [!] Invalid choice.")


if __name__ == "__main__":
    run()
