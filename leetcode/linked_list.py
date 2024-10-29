'''
Linked list:
- Permitir adicionar elemento ao final;
- Permitir adicionar elemento no inicio;
- Permitir remover elemento no final;
- Permitir remover elemento no inicio;
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add_to_front(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        return

    def add_to_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1
    
    def pop_front(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def pop_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            value = self.head.value
            self.head = None
            self.size -= 1
            return value
        
        current = self.head
        while current.next and current.next.next is not None:
            current = current.next
        
        value = current.next.value
        current.next = None
        self.size -= 1
        return value

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)    
    
def invert_linked_list(ll: LinkedList):
    # Initialize three pointers: curr, prev and next
    curr = ll.head
    prev = None

    # Traverse all the nodes of Linked List
    while curr is not None:

        # Store next
        next_node = curr.next

        # Reverse current node's next pointer
        curr.next = prev

        # Move pointers one position ahead
        prev = curr
        curr = next_node

    # Return the head of reversed linked list
    return prev


tst = LinkedList()
tst.add_to_end(1)
tst.add_to_end(2)
tst.add_to_end(3)
print(tst)
tst.pop_end()
print(tst)
tst.pop_front()
print(tst)

tst = LinkedList()
tst.add_to_front(1)
tst.add_to_front(2)
tst.add_to_front(3)
print(tst)
tst = invert_linked_list(tst)
print("invertida", tst)
tst.pop_end()
print(tst)
tst.pop_front()
print(tst)
tst.pop_front()
print(tst)

