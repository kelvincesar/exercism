'''
Linked list:
- Permitir adicionar elemento ao final;
- Permitir adicionar elemento no inicio;
- Permitir remover elemento no final;
- Permitir remover elemento no inicio;
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, value):
        node = Node(value)
    
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def add_to_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        return

    def pop_front(self):
        if self.head is None:
            return None
        pop = self.head
        self.head = self.head.next
        return pop
    
    def pop_end(self):
        if self.head is None:
            return None
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        pop = current.next
        current.next = None
        return pop

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def middle_node(self):
        faster_pointer = middle_pointer = self.head
        while faster_pointer and faster_pointer.next:
            faster_pointer = faster_pointer.next.next
            middle_pointer = middle_pointer.next
        return middle_pointer

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def __str__(self):
        values = []
        if self.head is None:
            return ''
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)
        



tst = LinkedList()
tst.add_to_end(1)
tst.add_to_end(2)
tst.add_to_end(3)
assert str(tst) == "1 -> 2 -> 3"
tst.pop_end()
assert str(tst) == "1 -> 2"
tst.pop_front()
assert str(tst) == "2"

tst = LinkedList()
tst.add_to_front(1)
tst.add_to_front(2)
tst.add_to_front(3)
assert str(tst) == "3 -> 2 -> 1"
tst.pop_end()
assert str(tst) == "3 -> 2"
tst.pop_front()
assert str(tst) == "2"
tst.pop_front()
assert str(tst) == ""

tst = LinkedList()
tst.add_to_end(1)
tst.add_to_end(2)
tst.add_to_end(3)
print(tst, tst.head.value)
tst.reverse()
assert str(tst) == "3 -> 2 -> 1"
print(tst, tst.head.value)
