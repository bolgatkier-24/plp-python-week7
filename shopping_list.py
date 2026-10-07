# shopping_list.py

# Start with an empty list
shopping_list = []

print("Welcome to your Shopping List Manager!")

while True:
    print("\nMenu:")
    print("  - add: Add an item")
    print("  - remove: Remove an item")
    print("  - show: Show all items")
    print("  - done: Quit the program")
    
    choice = input("What would you like to do? (add/remove/show/done): ").strip().lower()
    
    if choice == "add":
        item = input("Enter the item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' has been added to your list.")
        else:
            print("Item name cannot be empty.")
            
    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        # Check membership with 'in' before acting to avoid crashes
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your list.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        if not shopping_list:
            print("Your shopping list is currently empty.")
        else:
            print("\nYour Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
                
    elif choice == "done":
        print("Goodbye! Thanks for using the Shopping List Manager.")
        break
    else:
        print("Invalid choice. Please type add, remove, show, or done.")
