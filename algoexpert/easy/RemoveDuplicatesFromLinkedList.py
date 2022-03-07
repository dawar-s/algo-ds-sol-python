# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    curr = linkedList
    while curr is not None:
        nextnode = curr.next
        while nextnode is not None and curr.value == nextnode.value:
            nextnode = nextnode.next
        curr.next = nextnode
        curr = nextnode

    return linkedList
