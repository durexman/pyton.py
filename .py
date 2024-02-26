import random

class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

class ShoppingList:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity, unit, store):
        if store not in self.items:
            self.items[store] = []
        self.items[store].append((item, quantity, unit))
        print(f"'{quantity} {unit} of {item}' added to the shopping list for {store}.")

    def remove_item(self, item, store):
        if store in self.items:
            for i, (i_name, _, _) in enumerate(self.items[store]):
                if i_name == item:
                    del self.items[store][i]
                    print(f"'{item}' removed from the shopping list for {store}.")
                    return
            print(f"'{item}' not found in the shopping list for {store}.")
        else:
            print(f"'{item}' not found in the shopping list for {store}.")

    def view_list(self):
        print("Shopping List:")
        for store, items in self.items.items():
            print(f"\n{store}:")
            for item, quantity, unit in items:
                print(f"- {quantity} {unit} of {item}")

class ReminderSystem:
    def __init__(self):
        self.locations = {}

    def add_location(self, store, location):
        self.locations[store] = location

    def remind(self, current_location, shopping_list):
        for store, location in self.locations.items():
            if location == current_location:
                if store in shopping_list.items:
                    print(f"Reminder: You have items to buy at {store}!")
                    print("Shopping List:")
                    for item, quantity, unit in shopping_list.items[store]:
                        print(f"- {quantity} {unit} of {item}")

# Define lists of praises and encouragements
praises = [
    "Great job! Keep up the good work!",
    "Well done! You're making progress!",
    "Fantastic! You're doing an amazing job!",
    # Add more praises as needed
]

encouragements = [
    "Don't worry, keep trying! You'll get it next time.",
    "It's okay, everyone has off days. Keep pushing forward!",
    "Hang in there! You're capable of overcoming any challenge.",
    # Add more encouragements as needed
]

def main():
    # Initialize shopping list and reminder system
    shopping_list = ShoppingList()
    reminder_system = ReminderSystem()

    while True:
        print("\nMenu:")
        print("1. Manage Shopping List")
        print("2. Add Location for Reminder")
        print("3. Check Location for Reminders")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                # Manage Shopping List
                print("\nManage Shopping List:")
                print("1. Add Item")
                print("2. Remove Item")
                print("3. View List")
                print("4. Back to Main Menu")

                shopping_choice = input("Enter your choice: ")

                if shopping_choice == "1":
                    item = input("Enter the item to add: ")
                    quantity = input("Enter the quantity: ")
                    unit = input("Enter the unit (e.g., kg, lbs): ")
                    store = input("Enter the store for the item: ")
                    shopping_list.add_item(item, quantity, unit, store)
                elif shopping_choice == "2":
                    item = input("Enter the item to remove: ")
                    store = input("Enter the store for the item: ")
                    shopping_list.remove_item(item, store)
                elif shopping_choice == "3":
                    shopping_list.view_list()
                elif shopping_choice == "4":
                    continue
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

            elif choice == "2":
                # Add Location for Reminder
                store = input("Enter the store name: ")
                location = input("Enter the location (e.g., address or GPS coordinates): ")
                reminder_system.add_location(store, location)
                print(f"Location added for {store}.")

            elif choice == "3":
                # Check Location for Reminders
                current_location = input("Enter your current location: ")
                reminder_system.remind(current_location, shopping_list)

            elif choice == "4":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except EOFError:
            print("Error: Input was unexpectedly terminated. Please try again.")

            if __name__ == "__main__":
                main()
