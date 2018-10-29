# implementation of stack
# simple implementation of postfix evluation
import re


class Stack():

    # a Stack object contains an attribute named items that is a list of items in the stak
    # The initiate method sets items to the empty list
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    # use same-named list method to remove and return the last item of the list
    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


# Evaluating postfix
def postfix_eval(string):
    token_list = re.split("([^0-9])", string)
    stack = Stack()
    count = 0
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            temp_sum = stack.pop() + stack.pop()
            stack.push(temp_sum)
        elif token == "*":
            temp_product = stack.pop() * stack.pop()
            stack.push(temp_product)
        else:
            stack.push(int(token))
            count += 1
    return stack.pop()


# test case 1 + 2 * 3
print(postfix_eval("2 3 * 1 +"))



