"""
Python implementations of a stack

Python Stack data structure Implementations:
    1. list
        pros:
            - quicker l[index] 
        cons:
            - insertions get expensive due to memory allocations as the collection grows
            - not thread safe
    2. collections.deque
        pros:
            - insertions not expensive even with big collection
            - .pop() and .append() only thread safe. Not safe in general becaus of the
              other methods
        cons:
            - slower deque[index]
    3. queue.LifoQueue
        pros:
            - Thread safe
        cons:
            - slower
"""
from collections import deque
from queue import LifoQueue

# Stack implementation with deque and list
class Stack:
    """Stack base class for list and deque
    """

    def __init__(self, stack: (list, deque)):
        self.stack = stack()

    def pop(self):
        try:
            value = self.stack.pop()
            return value
        except IndexError:
            print('\n Stack Empty!')

    def push(self, val):
        return self.stack.append(val)

    def len_(self):
        return len(self.stack)

    def __str__(self):
        return self.stack.__str__()


if __name__ == '__main__':
    # queue.LifoQueue
    lifo_q_stack = LifoQueue()

    lifo_q_stack.put('a')
    lifo_q_stack.put('b')
    lifo_q_stack.put('c')
    print(f'\n lifo_q_stack : {lifo_q_stack}')
    print(lifo_q_stack.get())
    print(lifo_q_stack.get())
    print(lifo_q_stack.get(), end='\n'+('>>>>>>>>>>>'*10)+'\n')
    # print(lifo_q_stack.get())

    # list
    list_stack = Stack(list)
    list_stack.push(3)
    list_stack.push([2,'2323'])
    list_stack.push(1)
    print(f'\n list_stack : {list_stack}')
    for i in range(list_stack.len_()+1):
        print(list_stack.pop())
    print('Next:',end='\n'+('>>>>>>>>>>>'*10)+'\n')

    # deque
    deque_stack = Stack(deque)
    deque_stack.push(3)
    deque_stack.push([2,'2323'])
    deque_stack.push(1)
    print(f'\n deque_stack : {deque_stack}')
    for i in range(deque_stack.len_()+1):
        print(deque_stack.pop())
    print('Next:',end='\n'+('>>>>>>>>>>>'*10)+'\n')
    


