# This script creates a class to convert prefix to postfix notation
from cmath import inf
from charels1_lab1.stack import Stack


class Convert:
    def __init__(self, prefix: str):
        """
        Creates Convert object
        prefix: string in prefix form
        """
        self.prefix = prefix
        self.postfix = ''

    def converter(self) -> str:
        """
        Takes in a string in prefix form and uses a stack to convert directly to postfix form
        return: string in postfix form
        """
        # Define acceptable operators and operands that can be added to a stack
        operators = ['+', '-', '*', '/', '$']
        operands = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U,' 'V', 'W', 'X', 'Y', 'Z']
        lower_operands = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Initialize a new stack using Stack class with max height of infinity (an int can be passed in instead to
        # limit stack size if desired)
        new_stack = Stack(inf)
        prefix_stack = Stack(inf)

        # Initialize a postfix variable and prefix variable to iterate right to left through prefix phrase
        postfix_phrase = self.postfix
        prefix = self.prefix.strip()
        prefix_phrase = ''
        total_operands = 0
        total_operators = 0

        # iterate through prefix string, add items to stack, pop from stack to create reversed order prefix string
        for item in prefix:
            prefix_stack.push(item)
        while prefix_stack.is_empty():
            prefix_phrase += f'{prefix_stack.pop()}'

        for letter in prefix_phrase:
            if letter in operators or letter == '^':
                total_operators += 1
            elif letter in operands or lower_operands or numbers:
                total_operands += 1

        if total_operands == 0 and total_operators == 0:    # skips over empty lines
            pass
        elif total_operands != (total_operators + 1):
            raise AssertionError(f"Incorrect ratio of operators to operands in {prefix_phrase}.")
            # accounts for statements with more operators than operands

        # for loop parses through each individual character in the string
        for item in prefix_phrase:
            if item == '^':
                new_stack.push('$')
                # accounts for different method of writing exponentiation

            elif item in operands:
                new_stack.push(item)
                # pushes a letter on to the stack

            elif item in lower_operands:
                new_stack.push(item.upper())
                # accounts for operands that may be passed in as lowercase

            elif item in operators:
                out1 = new_stack.pop()
                out2 = new_stack.pop()
                combined = out1 + out2 + item
                new_stack.push(combined)
                # pops the two previous operands and pushes them back on the stack with the operator

            elif item == ' ' or '\n':
                continue
                # skips over spaces and new line characters

            elif item not in operands or operators:
                raise AssertionError(f"{item} is not compatible with this stack")
                # raises error if any non-compatible characters get passed in as string objects (i.e. '5', '%')

            else:
                new_stack.push(item)
                # checks any remaining potential assertion errors from the Stack class (max height, non-str type)

        while new_stack.is_empty():
            postfix_phrase += f'{new_stack.pop()}'

        return postfix_phrase
