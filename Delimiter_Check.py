import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
  contents = ''
  with open (filename) as f:
    contents = f.read()
  delimeterStack = Stack()
  lookUp = {'(' : ')', '[' : ']','{' : '}'} #keys and values are a sepperate list that you can itterate through 
  for token in contents:
    if token in lookUp.keys() : #if its an open parenthesis 
      delimeterStack.push(token)
    elif token in lookUp.values():
      if len(delimeterStack) == 0:
        return False
      top_tok = delimeterStack.pop()
      if lookUp[top_tok] != token:
        return False
  return len(delimeterStack) == 0 #returns boolean value that tells us if the stack is empty 

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


