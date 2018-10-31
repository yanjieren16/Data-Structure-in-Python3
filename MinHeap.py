# implementation of MinHeap using a list
# heap is a complete binary tree
# if parent at position p
# then left child at position p, right child at position 2p + 1


class BinaryHeap:

    def __init__(self):
        self.heap = [0]
        self.length = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i //2

    def add(self, k):
        self.heap.append(k)
        self.length += 1
        self.percolate_up(self.length)

    # swap the root with its smallest child less than the root
    # may repeat the swapping process with a node and its children
    # until the node is swapped into a position on the tree where it is already less than both children


    def percolate_down(self, i):
        while (i * 2) <= self.length:
            # mc holds the smaller child of i
            mc = self.min_child(i)
            # swap if the root > smaller child
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = self.heap[tmp]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.length:
            return i * 2
        else:
            # return smaller child
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def remove_min(self):
        min_value = self.heap[1]
        self.heap[1] = self.heap[self.length]
        self.length -= 1
        self.heap.pop()
        self.percolate_down(1)
        return min_value

    def build_heap(self, token_list):
        i = len(token_list) // 2
        self.length = len(token_list)
        self.heap = [0] + token_list[:]
        while i > 0:
            self.percolate_down(i)
            i -= 1


build_heap([0, 9, 5, 6, 2, 3])
