#!/usr/bin/env python3
# Wesley Stutzman
# Infix to post fix calculator

class Stack:
  # Create a list to use as the stack on init
  def __init__(self):
    self.items = []

  # Return a boolean value if the stack has items inside of it or not
  def is_empty(self):
    return self.items == []

  # Add an item onto the end of the stack
  def push(self, item):
    self.items.append(item)

  # Return the last item in the list to the user
  # Remove this last item from the list as well
  # Throw an error if there is no items in your list
  def pop(self):
    assert len(self.items) > 0
    return self.items.pop()

  # Check the last item in the list and return its value
  def peek(self):
    return self.items[len(self.items) - 1]

  # Return the current lise of the list
  def size(self):
    return len(self.items)


class BuildingOperation:
  def __init__(self):
    # assert function == ""
    self.stack = Stack()
  # Make sure the parenthases are balanced
  def checkValid(self, operation):
    # Hold all the values in a list
    paren = []
    # Hold the return values
    returnValue = True
    # Loop based on the size of the string
    for i in range (0, len(operation)):
      # If there is an open paren add it to the stack
      if operation[i] == "(":
        paren.append(operation[i])
      # If there is a close bracket pop the open paren off the stack
      if operation[i] == ")":
        # If the stack is emty it is unbalanced so return false
        if len(paren) == 0:
          returnValue = False
          break
        # Pop off the open paren if it matched a close paren
        paren.pop()
    # After you search everything if there is unmatching parens return false
    if len(paren) != 0:
      returnValue = False
    return returnValue
  
  # This is used to convert a number from infix to post-fix operation
  def buildPostfix(self, operation):
    # If it is not balanced throw an error
    assert self.checkValid(operation) == True
    # Hold the prioreties of the signs in a dictionary
    values = {}
    values['*'] = 3
    values['/'] = 3
    values['+'] = 2
    values['-'] = 2
    values['('] = 1
    # Break up all strings by white space and store it in a list
    token_list = operation.split()
    # Create a stack and a list to hold items during function
    temp = Stack()
    return_operation = []
    # Loop through the list of items and pull out each one
    for token in token_list:
      # If the token is a number add it to the list
      if token.isdigit():
        return_operation.append(token)
      # If it is an open paren add it to the stack for later
      elif token == "(":
        temp.push(token)
      # If it is a close paren dump the stack into the return value
      elif token == ")":
        holder = temp.pop()
        # Loop untill you are back at your open paren
        while holder != "(":
          return_operation.append(holder)
          holder = temp.pop()
      # If not a special case do this action
      else:
        # While you are not empty and your sign value is less then your current token value
        # Append items to the list
        while not temp.is_empty() and values[temp.peek()] >= values[token]:
          return_operation.append(temp.pop())
        # Once the stack is empty add the new token
        temp.push(token)
    # Once everything has been added make sure you empty your stack before leaving
    while not temp.is_empty():
      return_operation.append(temp.pop())
    # Return your new post fix operation
    return return_operation

    print(token_list)
  def buildStack(self):
    print("Testing")

  def prefixSolver(self, operation):
    holder = Stack()
    # Loop through all items in the passed in list
    for i in range(0,len(operation)):
      # If the item is an operator then do it matchinf function
      # Take the top 2 items off the stack because they should be numbers
      if operation[i] in "+-*/":
        val1 = int(holder.pop())
        val2 = int(holder.pop())
        if operation[i] == '+':
          holder.push(val1 + val2)
        elif operation[i] == '-':
          holder.push(val1 - val2)
        elif operation[i] == '*':
          holder.push(val1 * val2)
        elif operation[i] == '/':
          holder.push(val1 / val2)
      # If the item is a number add it to the stack untill a sign is found
      else:
        holder.push(operation[i])
    # Return the last item in the stack because it is your end value
    return holder.pop()
    
if __name__ == "__main__":

  operation = "2 * ( 5 + 6 ) + 32"
  function = BuildingOperation()
  temp = function.buildPostfix(operation)
  holder = ""
  for i in range(0,len(temp)):
    holder += temp[i] 
    holder += " "

  print(operation)
  print()
  print(holder + "= " + str(function.prefixSolver(temp)))
