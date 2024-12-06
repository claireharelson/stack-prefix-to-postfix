# This script creates a class to define a stack object to hold string type items
from math import inf


class Stack:
    def __init__(self, max_height: int or inf):
        """
        Holds string object items in a traditional stack
        max_height: The maximum number of items to be held in the stack
        """
        self.max_items = max_height
        self.items = []

    def is_empty(self) -> bool:
        """
        Determines if the stack is currently empty or not
        return: TRUE if the stack currently has no items and FALSE otherwise
        """
        return len(self.items) > 0

    def is_full(self) -> bool:
        """
        Determines if the stack is currently full
        return: TRUE if the stack is full and FALSE otherwise
        """
        return len(self.items) >= self.max_items

    def pop(self) -> str:
        """
        Removes one item from the top of the stack and returns it
        return: the current item on the top of the stack
        """
        return self.items.pop()

    def push(self, insert_me: str) -> None:
        """
        Pushes an item on to the stack
        insert_me: the item to insert - Note: item needs to be of type str
        """
        if self.max_items <= len(self.items):
            raise OverflowError("Stack exceeds max height")
        elif type(insert_me) is not str:
            raise AssertionError(f"This is a string type stack! Please don't input {type(insert_me)}")
        else:
            self.items.append(insert_me)

    def peek(self) -> str:
        """
        Shows the user the item that is currently at the top of the stack
        return: The string item from the top of the stack
        """
        top_item = self.items.pop()
        self.items.append(top_item)
        return top_item
