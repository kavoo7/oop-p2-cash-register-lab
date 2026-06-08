#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initialize a cash register with optional discount.
        
        Args:
            discount (int): Discount percentage (0-100). Defaults to 0.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """Get the discount percentage."""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """Set the discount percentage with validation.
        
        Args:
            value (int): Discount percentage must be between 0-100 inclusive.
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0
    
    def add_item(self, item, price, quantity=1):
        """Add an item to the cash register.
        
        Args:
            item (str): Name of the item
            price (float): Price of the item
            quantity (int): Quantity of items to add. Defaults to 1.
        """
        # Update total
        self.total += price * quantity
        
        # Add item to items list (once per quantity)
        for _ in range(quantity):
            self.items.append(item)
        
        # Record transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })
    
    def apply_discount(self):
        """Apply the discount to the total.
        
        Prints the new total after discount is applied.
        Removes the last transaction from previous_transactions.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Calculate discounted total
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            
            # Remove last transaction
            if self.previous_transactions:
                self.previous_transactions.pop()
            
            print(f"After the discount, the total comes to ${self.total:.0f}.")
    
    def void_last_transaction(self):
        """Remove the last transaction from the register.
        
        Updates total and items list accordingly.
        """
        if not self.previous_transactions:
            print("There is no transaction to void.")
        else:
            # Get last transaction
            last_transaction = self.previous_transactions.pop()
            
            # Update total
            self.total -= last_transaction["price"] * last_transaction["quantity"]
            
            # Remove items from items list
            for _ in range(last_transaction["quantity"]):
                self.items.remove(last_transaction["item"])
