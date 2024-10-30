class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def middle_node(head):
    middle_pointer = head
    faster_pointer = head.next
    while faster_pointer and faster_pointer.next:
        faster_pointer = faster_pointer.next.next
        middle_pointer = middle_pointer.next
    return middle_pointer

def merge(l1, l2):
    head = Node(None)
    tail = head

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return head.next

def mergesort(head):
    if not head or not head.next:
        return head
    middle = middle_node(head)
    after_middle = middle.next
    middle.next = None
    left = mergesort(head)
    right = mergesort(after_middle)

    sorted_list = merge(left, right)

    return sorted_list

nodes = Node(7)
nodes = Node(3, next=nodes)
nodes = Node(1, next=nodes)
nodes = Node(9, next=nodes)

order_list = mergesort(nodes)

while order_list is not None:
    print(order_list.value)
    order_list = order_list.next