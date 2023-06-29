from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  #the str method runs in O(n) time because it references the liked list str function which,
  #itterates through the entire linked list and cast each value to a string and store it in an array, it thens itterates through the new array and prints all the values in the proper format
  def __str__(self):
    return str(self.__list)

  #the len method runs in constant time because it returns the inherited value returned by the linked list len method which simply returns the self.__size field
  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  #the push_front method runs in constant time, because it either uses the append_element(val) function from Linked_List.py which inserts using the previous pointer of the trailer sentinel and thus the last node in the Linked List can be identitified. Making the two position requirment for insertion possible 
  # or it uses insert_element_at(val,0) which is inserting at the very beginning of the list and thus it does not have to walk any length of list to insert so the operation is constant 
  def push_front(self, val):
    # TODO replaxsce pass with your implementation.
    # Use the head position for the front.
    if len(self.__list) == 0:
      self.__list.append_element(val)
    else:
      self.__list.insert_element_at(val,0)
  
  #the pop_front method runs in constant time because it uses the remove element at function to remove at the very beginning of a linked list, which requires no itterating("walking") and thus is constant 
  def pop_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if (len(self.__list) == 0):
      return None
    else:
      return self.__list.remove_element_at(0)

  #the peek_front method runs in constant time as it uses the get element at function to return first element in a linked list, which requires no itterating("walking") and thus is constant 
  def peek_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list) == 0:
      return None
    return self.__list.get_element_at(0)

  #the push back method runs in constant time as it uses the append element function(see comment on push_front for explanation of how the append element function is constant)
  def push_back(self, val):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    self.__list.append_element(val)
  
  #the pop_back method runs in O(n), becasuse it uses the remove element at method from linked list to remove and return the last element in the linked list.
  #To do this the remve_element_at method walks to one node before the end of the list and thus its run time is based directly on the size of the linked list. Meaning its run time is linear
  def pop_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if (len(self.__list) == 0):
      return None
    else:
      return self.__list.remove_element_at(len(self.__list) - 1)

  #the peek_back method runs in O(n) time as it uses the get_element_at method to "walk" the linked list to the last element and return that value. Thus the run time is based on the length of the linked list
  def peek_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if (len(self.__list) == 0):
      return None
    return self.__list.get_element_at(len(self.__list) - 1)

# Unit tests make the main section unneccessary.
if __name__ == '__main__':
 a = Linked_List_Deque() 
 a.push_front('A')
 a.push_front('B')
 a.push_front('C')
 a.pop_front()
 a.pop_front()
 a.pop_front()
 print(str(a))
