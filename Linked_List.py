class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            self.prev = None 
            self.next = None 
            self.val = val


    def __init__(self):
        self._header = self.__Node(None)
        self._trailer = self.__Node(None)
        self._header.next = self._trailer 
        self._trailer.prev = self._header 
        self.currentPointer = None 
        self.__size = 0 

    #The len method returns the size of the Linked List in O(1), because the size is kept track of and altered everytime something is added to or removed from the Linked List 
    def __len__(self):
        return self.__size

    #The append_element method is in O(1), because using the previous pointer of the trailer sentinel, the last node in the Linked List can be identitified and thus we have two know places to insert a new node
    def append_element(self, val):
        self.__size = self.__size + 1 
        newNode = self.__Node(val)
        a = self._trailer.prev 
        a.next = newNode 
        newNode.prev = a 
        newNode.next = self._trailer
        self._trailer.prev = newNode 

    #The walkListToBeforePoint method runs in O(n) worst case, because in order to access the node before a node we must walk the linked list and thus the amount of calls to cur.next is based on the size of the LL
    def walkListToBeforePoint(self, index):
        if index > self.__size or self.__size == 0:
            raise IndexError
        if index == 0:
            cur = self._header.next
        halfWayPoint = self.__size//2
        if (index-1) > halfWayPoint:
            cur = self._trailer.prev
            for i in range((self.__size - (index))):
                cur = cur.prev
        else:
            cur = self._header.next
            for i in range (index-1):
                cur = cur.next
        
        return cur
        
    #The insert_element_at method runs in o(n) worst case, because it calls walkListToBeforePoint to identify the point prior to desired insertion index inorder to have control of the arrows to the nodes before and after the desired insertion index
    def insert_element_at(self, val, index):
        newNode = self.__Node(val)
        if index == self.__size:
            raise IndexError
        if index == 0: 
            inserter = self._header
        else:
            inserter = self.walkListToBeforePoint(index)
        newNode.next = inserter.next
        newNode.prev = inserter
        inserter.next = newNode 
        newNode.next.prev = newNode
        self.__size = self.__size + 1

    #The remove_element_at method runs in o(n) worst case, because like the insert_element_at method it calls walkListToBeforePoint to "stand" directly before the node it needs to remove and rearange pointers
    def remove_element_at(self, index):
        removed=self.walkListToBeforePoint(index+1)
        if index == 0:
            removed = self._header.next
            remover = self._header
        else:
            remover = self.walkListToBeforePoint(index) 
        remover.next = remover.next.next
        remover.next.prev = remover
        self.__size = self.__size - 1
        return removed.val

    #The get_element_at method runs in 0(n) worst case, because it must walk the linked list to find the desired node indicated by the index and return the value
    def get_element_at(self, index):
        return self.walkListToBeforePoint(index+1).val
    
    #The rotate_left method runs in O(1) as it does not need to walk the list to dertirmine any values and can seemply swap the values at the end and beginning of the Linked List using the prev/next pointers from the header/trailer
    def rotate_left(self):
        if self.__size == 1:
            return self 
        if self.__size == 0:
            return self
        cur = self._header.next 
        saveEnd = self._trailer.prev
        self._header.next = cur.next 
        self._header.next.prev = self._header
        self._trailer.prev = cur 
        cur.next = self._trailer 
        cur.prev = saveEnd
        saveEnd.next = cur 
        
    #The str method runs in O(n) because it itterates through the entire linked list and cast each value to a string and store it in an array, it thens itterates through the new array and prints all the values in the proper format    
    def __str__(self):
        data = []
        cur = self._header.next
        if self.__size == 0:
            stringRep = "[ ]"
            return stringRep
        while cur != self._trailer: 
            data.append(str(cur.val))
            cur = cur.next 
        stringRep = ", ".join(data)
        stringRep = f"[ {stringRep} ]"
 
        return stringRep

    #The iter method runs in 0(1) time, because it simply assigns the current pointer to the header sentinel 
    def __iter__(self):
        self.currentPointer = self._header
        return self

    #The next method runs in O(1) time, because it returns the value of the next Node 
    def __next__(self):
        if self.currentPointer is self._trailer.prev:
            raise StopIteration
        self.currentPointer = self.currentPointer.next 
        return self.currentPointer.val 

    #The reveresed method runs in O(n) time as it must walk through the linked list in reverse and place all the values into a new linked list as it accesses them, thus creating a new linked list with elements in the reverse order from the original
    def __reversed__(self):
        current = self._trailer.prev
        reversedLinkedList = Linked_List() 
        while current != self._header:
            reversedLinkedList.append_element(current.val)
            current = current.prev 
        return reversedLinkedList

if __name__ == '__main__':
    a = Linked_List() 
    empty = Linked_List()
    b = Linked_List()
    c = Linked_List()
    d = Linked_List()
    print("tests for append")
    a.append_element(6)
    a.append_element(5)
    a.append_element(4)
    a.append_element(3)
    a.append_element(2)
    a.append_element(1)
    a.append_element(0)
    b.append_element('A')
    c.append_element('Z')
    d.append_element('X')
    print(a)
    #testing walk to point
    #print(a.walkListToBeforePoint(2).val)
    #exit(0)
    print("tests for insert_element_at")
    print("testing for inserting on one element linked List")
    b.insert_element_at('B',0)
    print("test for inserting closer to trailer")
    a.insert_element_at(9,3)
    print(a)
    print("test for inserting closer to the header")
    a.insert_element_at(6,2)
    print(a)
    print("test for inserting at head of linked list")
    a.insert_element_at(7,0)
    print(a)
    #a.insert_element_at(1,10) ---> test for IndexError Exception
    #a.insert_element_at(1,7) ---> test for inserting at tail error
    #empty.insert_element_at(1,2) ---> test for inserting on emptylist
    print("test for printing empty linked lists")
    print(empty)
    print("tests for remove element at")
    print("testing for removing on one element linked List")
    print(c.remove_element_at(0))
    print(c)
    print("test for removing closer to the header")
    print(a.remove_element_at(3))
    print(a)
    print("test for removing at head of the linked list")
    print(a.remove_element_at(0))
    print(a)
    print("test for removing closer to the trailer of the linked list")
    print(a.remove_element_at(5))
    print(a)
    #print(a.remove_element_at(10)) ---> test for IndexError Exception
    #empty.remove_element_at(2) ---> test for inserting on emptylist
    print("tests for get element at")
    #empty.get_element_at(1) --> test for getting on emptylist
    #a.get_element_at(10) --> test for getting with out of bounds index
    print("test for getting element at the near the trailer list")
    print(a.get_element_at(4))
    print("test for getting element near the header/at header of the list")
    print(a.get_element_at(0))
    print("tests for rotate element")
    empty.rotate_left()
    a.rotate_left() 
    d.rotate_left()
    print(a) 
    print(d) 

    print("tests for iter")
    for x in a:
        print(x)

    print("tests for reversed")
    print(reversed(a))
    

