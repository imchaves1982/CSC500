# Week 4: Milestone Project
# Irene East

# Build the ItemToPurchase class

class ItemToPurchase:
    # Default constructor function
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0): #Did 0.0 to assign variable as float
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    # Method to print item cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

# Prompt the user for two items and create two objects

def main():
    # Create first item
    print("Item 1")
    item_name1 = input("Enter the item name:\n")
    item_price1 = float(input("Enter the item price:\n"))
    item_quantity1 = int(input("Enter the item quantity:\n"))
    item1 = ItemToPurchase(item_name1, item_price1, item_quantity1)
    
    # Create second item
    print("\nItem 2")
    item_name2 = input("Enter the item name:\n")
    item_price2 = float(input("Enter the item price:\n"))
    item_quantity2 = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase(item_name2, item_price2, item_quantity2)
    
    # Do the calculations and output the total cost
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total_cost}")

# Run the main function. 
if __name__ == "__main__":
    main()
