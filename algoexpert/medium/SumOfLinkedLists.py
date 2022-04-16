# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    new_list = LinkedList(0)
    current = new_list
    node1 = linkedListOne
    node2 = linkedListTwo
    carry = 0
    while node1 is not None or node2 is not None or carry != 0:
        value1 = node1.value if node1 is not None else 0
        value2 = node2.value if node2 is not None else 0
        total = value1 + value2 + carry
        new_node = LinkedList(total % 10)
        current.next = new_node
        current = new_node

        carry = total // 10
        node1 = node1.next if node1 is not None else None
        node2 = node2.next if node2 is not None else None

    return new_list.next


l1 = LinkedList(2)
l1.next = LinkedList(4)
l1.next.next = LinkedList(7)
l1.next.next.next = LinkedList(1)

l2 = LinkedList(9)
l2.next = LinkedList(4)
l2.next.next = LinkedList(5)

l3 = sumOfLinkedLists(l1, l2)
while l3 is not None:
    print(l3.value)
    l3 = l3.next
