from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__front = None 
    self.__back = None
    self.__length = 0
    # TODO replace pass with any additional initializations you need.
    pass
    
  #the str method runs in linear time (o(n)), because it first itterates from front to back of the deque and copies those values into an array. then using .join it creates the proper str structure and returns
  def __str__(self):
    if self.__length == 0:
      return "[ ]"
    stringRep = ""
    data = []
    i = self.__front
    while i != self.__back:
      element = self.__contents[i]
      if element != None:
        data.append(str(element))
      i = (i+1) % self.__capacity
    data.append(str(self.__contents[self.__back]))
    stringRep = ", ".join(data)
    return f"[ {stringRep} ]"
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).

  #the len method runs in constant time o(1) as it returns the self.__length field which is increased/decreased based on insertion or deletion  
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    # not equal to the capcity but equal to the distance from front to back 
    return self.__length

  #the __grow method runs in linear time as it must itterate over the indexs from self.__front to self.__back in order to place the elements from self.__contents starting at index 0 in doubleCapacityCopy
  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    doubleCapacityCopy = [None] * (self.__capacity*2)
    if self.__back == self.__front:# case 1 is if theres one element
      doubleCapacityCopy[0] = self.__contents[self.__back]
    if self.__back + 1 == self.__front: # case 2 is if the back is one behind front
      index = self.__front
      c = 0
      while c < self.__length:
        element = self.__contents[index] 
        doubleCapacityCopy[c] = element
        index = (index + 1) % self.__capacity
        c += 1
    if self.__front == 0 and self.__back == self.__capacity-1: #case 3 front zero back at capacity or in order
      for i in range(self.__back+1):
        doubleCapacityCopy[i] = self.__contents[i]
    self.__front = 0 
    self.__back = self.__capacity - 1
    self.__contents = doubleCapacityCopy
    self.__capacity = self.__capacity * 2
    
  #push_front runs in constant time as it simply calculates the new front after insertion and then replaces the element at self.__contents[self.__front] with val
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__length == 0:
      self.__contents[0] = val
      self.__front = 0
      self.__back = 0
      self.__length = 1
    else:
      if (self.__front == 0 and self.__back == self.__capacity - 1) or (self.__back + 1 == self.__front):
        self.__grow()
      self.__front = self.__front - 1
      self.__front = self.__front + self.__capacity
      self.__front = self.__front % self.__capacity
      self.__contents[self.__front] = val
      self.__length = self.__length + 1

    #print(str(f"contents after push front{self.__contents}"))

  #the pop_front() method runs in constant time as it simply moves the self.__front val one index to the right through addition    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__length == 0:
      return None
    else:
      poppedElement = None 
      poppedElement = self.__contents[self.__front]
      self.__front = self.__front + 1
      self.__front = self.__front % self.__capacity
      self.__length -= 1
      return poppedElement

  #the peek front method returns the value stored at the self.__front index of self.__contents and is thus a constant time operation 
  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__length == 0:
      return None 
    return self.__contents[self.__front]
    
  #push_back runs in constant time as it calculates the new back after a possible insertion and then replaces the element at self.__contents[self.__back] with that val
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__length == 0:
      self.__contents[0] = val
      self.__front = 0
      self.__back = 0
      self.__length = 1
    else:
      if (self.__front == 0 and self.__back == self.__capacity - 1) or (self.__front + 1 == self.__back):
        self.__grow()
      self.__back = self.__back + 1
      self.__back = self.__back % self.__capacity
      self.__contents[self.__back] = val
      self.__length = self.__length + 1

  #pop back runs in constant time as it moves the value of self.__back by subrtacting one and using modular to make sure theres no negative indexing 
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__length == 0:
      return None
    else:
      poppedElement = None 
      poppedElement = self.__contents[self.__back]
      self.__back = self.__back - 1
      self.__back = self.__back + self.__capacity
      self.__back = self.__back % self.__capacity
      self.__length = self.__length - 1
      return poppedElement

  #the peek back method runs in constant time becasue it returns the value stored at the self.__back index of self.__contents and is thus a constant time operation 
  def peek_back(self):
    # TODO replace pass with your implementation.
    if self.__length == 0:
      return None 
    return self.__contents[self.__back]

#No main section is necessary. Unit tests take its place.
# if __name__ == '__main__':
#   a = Array_Deque() 
#   a.push_front('Apple')
#   print(a.returnFront())
#   print(a.returnBack())
#   print(str(a))
#   a.push_front('Pear')
#   print(a.returnFront())
#   print(a.returnBack())
#   print(str(a))
#   a.push_front('Orange')
#   print(a.returnFront())
#   print(a.returnBack())
#   print(str(a))
#   a.push_front('Dragonfruit')
#   print(a.returnFront())
#   print(a.returnBack())
#   print(str(a))
#   a.push_front('Eating')
#   print(a.returnFront())
#   print(a.returnBack())
#   print(str(a))



