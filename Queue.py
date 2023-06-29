from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque(0)

  #the queue's str method runs in O(n) times as it refernces the array_deques or the linked_list deques str method which both run in linear time 
  def __str__(self):
    return str(self.__dq)

  #the queue's len method runs in constant time as it refernces the array_deques or the linked_list deques len methods, which both run in constant time 
  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)

  #the enqueue method runs in constant time as it references the push back method from either LL_Deque or ARR_Deque and both run in constant time 
  def enqueue(self, val):
    # TODO replace pass with your implementation.
    self.__dq.push_back(val)

  #the dequeue method runs in constant time as it refrences the pop_front method from either LL_Deque or ARR_Deque and both run in constant time 
  def dequeue(self):
    # TODO replace pass with your implementation.
    return self.__dq.pop_front()

  #the peek method runs in constant tiem as it references the peek_front method from either LL_Deque or ARR_Deque and both run in constant time 
  def peek(self):
    # TODO replace pass with your implementation.
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
