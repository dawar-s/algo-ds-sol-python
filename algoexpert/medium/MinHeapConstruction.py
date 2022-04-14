# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        for parent_node_idx in range((len(array) - 2) // 2, -1, -1):
            self.siftDown(array, parent_node_idx)
        return array

    def siftDown(self, heap, idx=0):
        parent_idx = idx
        left_child_idx = 2 * parent_idx + 1
        while left_child_idx < len(heap):
            right_child_idx = 2 * parent_idx + 2 if 2 * parent_idx + 2 < len(heap) else -1
            if right_child_idx != -1 and heap[right_child_idx] < heap[left_child_idx]:
                swap_idx = right_child_idx
            else:
                swap_idx = left_child_idx
            if heap[swap_idx] < heap[parent_idx]:
                heap[parent_idx], heap[swap_idx] = heap[swap_idx], heap[parent_idx]
                parent_idx = swap_idx
                left_child_idx = 2 * parent_idx + 1
            else:
                return

    def siftUp(self, heap):
        idx = len(heap) - 1
        parent_idx = (idx - 1) // 2
        while idx > 0:
            if heap[parent_idx] <= heap[idx]:
                break
            heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def peek(self):
        if len(self.heap) == 0:
            raise IndexError('peek from an empty heap')
        return self.heap[0]

    def remove(self):
        if len(self.heap) == 0:
            raise IndexError('remove from an empty heap')
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        removed_value = self.heap.pop()
        if len(self.heap) == 0:
            return removed_value
        self.siftDown(self.heap)
        return removed_value

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap)


a = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
print('Heap', a.heap)
a.insert(76)
print('Insert 76', a.heap)
print('Peek', a.peek())
print('Heap after peek', a.heap)
print('Remove', a.remove())
print('Heap after remove', a.heap)
print('Peek', a.peek())
a.insert(-10)
print('Insert -10', a.heap)
