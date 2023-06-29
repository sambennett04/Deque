import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque(0)
    self.__stack = Stack()
    self.__queue = Queue()

  def test_empty_deque_string(self):
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_push_front_to_empty(self):
    self.__deque.push_front('A')
    self.assertEqual('[ A ]', str(self.__deque))

  def test_push_front_with_1(self):
    self.__deque.push_front('A')
    self.__deque.push_front('B')
    self.assertEqual('[ B, A ]', str(self.__deque))

  def test_push_front_with_2(self):
    self.__deque.push_front('A')
    self.__deque.push_front('B')
    self.__deque.push_front('C')
    self.assertEqual('[ C, B, A ]', str(self.__deque))

  def test_push_back_to_empty(self):
    self.__deque.push_back('A')
    self.assertEqual('[ A ]', str(self.__deque))
  
  def test_push_back_with_one(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    self.assertEqual('[ A, B ]', str(self.__deque))

  def test_push_back_with_two(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    self.__deque.push_back('C')
    self.assertEqual('[ A, B, C ]', str(self.__deque))

  def test_push_back_and_front_alternating(self):
    self.__deque.push_front('A')
    self.__deque.push_back('B')
    self.__deque.push_front('C')
    self.__deque.push_back('D')
    self.assertEqual('[ C, A, B, D ]', str(self.__deque))

  def test_get_empty_length_deque(self):
    self.assertEqual(0, len(self.__deque))

  def test_get_one_length_with_push_front(self):
    self.__deque.push_front('A')
    self.assertEqual(1, len(self.__deque))

  def test_get_one_length_with_push_back(self):
    self.__deque.push_back('A')
    self.assertEqual(1, len(self.__deque))

  def test_get_two_length_with_push_front(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Data')
    self.assertEqual(2, len(self.__deque))

  def test_get_two_length_with_push_back(self):
    self.__deque.push_back('Structures')
    self.__deque.push_back('Data')
    self.assertEqual(2, len(self.__deque))

  def test_get_four_length_alternate_push(self):
    self.__deque.push_front('A')
    self.__deque.push_back('B')
    self.__deque.push_front('C')
    self.__deque.push_back('D')
    self.assertEqual(4, len(self.__deque))

  def test_pop_front_empty_deque_return(self):
    returned = self.__deque.pop_front()
    self.assertEqual(None, returned)

  def test_pop_front_empty_deque_str(self):
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_empty_deque_return(self):
    returned = self.__deque.pop_back()
    self.assertEqual(None, returned)

  def test_pop_back_empty_deque_str(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_with_0_remaining_return(self):
    self.__deque.push_front('A')  
    returned = self.__deque.pop_front()
    self.assertEqual('A', returned)
    
  def test_pop_front_with_0_remaining_deque_change(self):
    self.__deque.push_front('A')  
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_with_0_reaminging_return(self):
    self.__deque.push_back('A')  
    returned = self.__deque.pop_back()
    self.assertEqual('A', returned)

  def test_pop_back_with_0_reaminging_deque_change(self):
    self.__deque.push_back('A')  
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_with_0_remaining_after_push_front(self):
    self.__deque.push_front('A')
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_with_0_remaining_after_push_back(self):
    self.__deque.push_back('A')
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_with_1_remaining_return(self):
    self.__deque.push_front('A')
    self.__deque.push_front('B')
    returned = self.__deque.pop_front()
    self.assertEqual('B', returned)

  def test_pop_front_with_1_remaining_deque_change(self):
    self.__deque.push_front('A')
    self.__deque.push_front('B')
    self.__deque.pop_front()
    self.assertEqual('[ A ]', str(self.__deque))

  def test_pop_back_with_1_remaining_return(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    returned = self.__deque.pop_back() 
    self.assertEqual('B', returned)

  def test_pop_back_with_1_remaining_deque_change(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    self.__deque.pop_back() 
    self.assertEqual('[ A ]', str(self.__deque))

  def test_get_0_length_after_pop_front(self):
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

  def test_get_0_length_after_pop_back(self):
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))

  def test_get_one_length_after_pop_front(self):
    self.__deque.push_back('A')
    self.__deque.push_front('B')
    self.__deque.pop_front()
    self.assertEqual(1, len(self.__deque))

  def test_get_one_length_after_pop_back(self):
    self.__deque.push_back('A')
    self.__deque.push_front('B')
    self.__deque.pop_back()
    self.assertEqual(1, len(self.__deque))

  def test_get_two_length_after_pop_front(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Data')
    self.__deque.push_back('Howls')
    self.__deque.pop_front()
    self.assertEqual(2, len(self.__deque))

  def test_get_two_length_after_pop_back(self):
    self.__deque.push_back('Structures')
    self.__deque.push_back('Data')
    self.__deque.push_back('Howls')
    self.__deque.pop_back()
    self.assertEqual(2, len(self.__deque))

  def test_peek_front_on_nothing(self):
    self.assertEqual(None, self.__deque.peek_front())

  def test_peek_back_on_nothing(self):
    self.assertEqual(None, self.__deque.peek_back())

  def test_peek_front_on_one(self):
    self.__deque.push_back('Data')
    self.assertEqual('Data', self.__deque.peek_front())
  
  def test_peek_back_on_one(self):
    self.__deque.push_back('Data')
    self.assertEqual('Data', self.__deque.peek_back())

  def test_peek_front_on_two(self):
    self.__deque.push_back('Data')
    self.__deque.push_front('Structures')
    self.assertEqual('Structures', self.__deque.peek_front())

  def test_peek_back_on_two(self):
    self.__deque.push_back('Data')
    self.__deque.push_front('Structures')
    self.assertEqual('Data', self.__deque.peek_back())

  def test_empty_stack_string(self):
    self.assertEqual('[ ]', str(self.__stack))

  def test_push_to_empty(self):
    self.__stack.push('A')
    self.assertEqual('[ A ]', str(self.__stack))

  def test_push_to_one(self):
    self.__stack.push('A')
    self.__stack.push('B')
    self.assertEqual('[ B, A ]', str(self.__stack))

  def test_push_to_two(self):
    self.__stack.push('A')
    self.__stack.push('B')
    self.__stack.push('C')
    self.assertEqual('[ C, B, A ]', str(self.__stack))

  def test_get_empty_length_stack(self):
    self.assertEqual(0, len(self.__stack))

  def test_get_one_length_stack(self):
    self.__stack.push('A')
    self.assertEqual(1, len(self.__stack))
    
  def test_get_two_length_stack(self):
    self.__stack.push('A')
    self.__stack.push('B')
    self.assertEqual(2, len(self.__stack))

  def test_pop_on_empty_stack_return(self):
    returned = self.__stack.pop()
    self.assertEqual(None, returned)

  def test_pop_on_empty_stack_str(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_with_0_remaining_return(self):
    self.__stack.push('A')
    returned = self.__stack.pop()
    self.assertEqual('A', returned)

  def test_pop_with_0_remaining_stack_change(self):
    self.__stack.push('A')
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_with_1_remaining_returned(self):
    self.__stack.push('A')
    self.__stack.push('B')
    returned = self.__stack.pop()
    self.assertEqual('B', returned)

  def test_pop_with_1_remaining_stack_change(self):
    self.__stack.push('A')
    self.__stack.push('B')
    self.__stack.pop()
    self.assertEqual('[ A ]', str(self.__stack))

  def test_push_twice_pop_thrice_return(self):
    self.__stack.push(8)
    self.__stack.push(-7)
    self.__stack.pop()
    self.__stack.pop()
    returned = self.__stack.pop()
    self.assertEqual(None, returned)

  def test_push_twice_pop_thrice_str(self):
    self.__stack.push(8)
    self.__stack.push(-7)
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_push_twice_pop_thrice_length(self):
    self.__stack.push(8)
    self.__stack.push(-7)
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_get_zero_length_after_pop(self):
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_get_one_length_after_pop(self):
    self.__stack.push('A')
    self.__stack.push('B')
    self.__stack.pop()
    self.assertEqual(1, len(self.__stack))

  def test_get_two_length_after_pop(self):
    self.__stack.push('Data')
    self.__stack.push('Data')
    self.__stack.push('Howls')
    self.__stack.pop()
    self.assertEqual(2, len(self.__stack))

  def test_peek_on_nothing(self):
    self.assertEqual(None, self.__stack.peek())

  def test_peek_on_one(self):
    self.__stack.push('A')
    self.assertEqual('A', self.__stack.peek())

  def test_peek_on_two(self):
    self.__stack.push('A')
    self.__stack.push('B')
    self.assertEqual('B', self.__stack.peek())
  
  def test_get_empty_length_queue(self):
    self.assertEqual('[ ]', str(self.__queue))
  
  def test_enqueue_to_empty(self):
    self.__queue.enqueue('A')
    self.assertEqual('[ A ]', str(self.__queue))

  def test_enqueue_to_1(self):
    self.__queue.enqueue('A')
    self.__queue.enqueue('A')
    self.assertEqual('[ A, A ]', str(self.__queue))

  def test_enqueue_to_2(self):
    self.__queue.enqueue('A')
    self.__queue.enqueue('B')
    self.__queue.enqueue('C')
    self.assertEqual('[ A, B, C ]', str(self.__queue))
  
  def test_get_one_length_queue(self):
    self.__queue.enqueue('A')
    self.assertEqual(1, len(self.__queue))

  def test_get_two_length_queue(self):
    self.__queue.enqueue('A')
    self.__queue.enqueue('A')
    self.assertEqual(2, len(self.__queue))

  def test_deque_on_empty_return(self):
    returned = self.__queue.dequeue()
    self.assertEqual(None, returned)

  def test_deque_on_empty_str(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_deque_on_empty_length(self):
    self.__queue
    self.assertEqual(0, len(self.__queue))

  def test_dequeue_to_empty_return(self):
    self.__queue.enqueue('A')
    returned = self.__queue.dequeue()
    self.assertEqual('A',returned)

  def test_dequeue_to_empty_queue_change(self):
    self.__queue.enqueue('A')
    self.__queue.dequeue()
    self.assertEqual('[ ]',str(self.__queue))

  def test_dequeue_to_1_return(self):
    self.__queue.enqueue('A')
    self.__queue.enqueue('B')
    returned = self.__queue.dequeue()
    self.assertEqual('A',returned)

  def test_dequeue_to_1_queue_change(self):
    self.__queue.enqueue('Y')
    self.__queue.enqueue('X')
    self.__queue.dequeue()
    self.assertEqual('[ X ]',str(self.__queue))
  
  def test_enqueue_twice_dequeue_thrice_return(self):
    self.__queue.enqueue(8)
    self.__queue.enqueue(-7)
    self.__queue.dequeue()
    self.__queue.dequeue()
    returned = self.__queue.dequeue()
    self.assertEqual(None, returned)

  def test_enqueue_twice_dequeue_thrice_str(self):
    self.__queue.enqueue(8)
    self.__queue.enqueue(-7)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_enqueue_twice_dequeue_thrice_length(self):
    self.__queue.enqueue(8)
    self.__queue.enqueue(-7)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))
    
  def test_peek_on_nothing_queue(self):
    self.assertEqual(None, self.__queue.peek())

  def test_peek_on_one(self):
    self.__queue.enqueue('A')
    self.assertEqual('A', self.__queue.peek())

  def test_peek_on_two(self):
    self.__queue.enqueue('A')
    self.__queue.enqueue('B')
    self.assertEqual('A', self.__queue.peek())



  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

if __name__ == '__main__':
  unittest.main()

