class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

    def __str__(self):
        return f'{self.value} '

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def printl(self):
        current = self.head
        while current:
            print(current)
            current = current.next
            if self.contains_cycle():
                break

    def contains_cycle(l_list):
        checked = set()
        current = l_list.head
        while current:
            if current in checked:
                return True
            checked.add(current)
            current = current.next
        return False


if __name__=='__main__':
    n1 = Node(2)
    n2 = Node(20)

    l = LinkedList()
    l.push(n1)
    l.push(n2)
    l.push(Node(1))
    l.push(Node(34))
    l.push(Node(0))

    l.printl()

        
    print(l.contains_cycle())
    l.head.next.next = l.head.next
    l.printl()
    print(l.contains_cycle())

