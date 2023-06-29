#how do we decide between the Array Deque methods and the Linked_List Deque methods 
from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque(0)

  #the stack's str method runs in O(n) times as it refernces the array_deques or the linked_list deques str method which both run in linear time 
  def __str__(self):
    return str(self.__dq)

  #the stack's len method runs in constant time as it refernces the array_deques or the linked_list deques len methods, which both run in constant time 
  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)

  #the stack's push method runs in constant time as it references the push_front method from LL_Deque or ARR_Deque which both run in constant time 
  def push(self, val):
    # TODO replace pass with your implementation.
    self.__dq.push_front(val)

  #the stack's pop method runs in constant time because it reference the pop_front method from LL_Deque or ARR_Deque which both run in constant time 
  def pop(self):
    # TODO replace pass with your implementation.
    return self.__dq.pop_front()

  #the stack's peek method runs in constant time, because it references the peek_front() from either the LL_Deque or the ARR_Deque which both run in constant time 
  def peek(self):
    # TODO replace pass with your implementation.
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
