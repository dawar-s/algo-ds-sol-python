# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    length = 0
    node = head
    while node is not None:
        length += 1
        node = node.next
    prev = None
    current = head
    loop_count = length - k
    while loop_count > 0:
        loop_count -= 1
        prev = current
        current = current.next
    # Remove head case
    if prev is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    # Remove tail case
    if current.next is None:
        prev.next = None
        return
    prev.next = current.next