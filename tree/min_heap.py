# https://runestone.academy/ns/books/published/pythonds/Trees/BinaryHeapImplementation.html

class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def insert(self, ele):
        self.heap_list.append(ele)
        self.current_size += 1
        self.perc_up(self.current_size)

    def min_child(self, i):
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] > self.heap_list[(i * 2) + 1]:
                return (i * 2) + 1
            else:
                return i * 2

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            min_child = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child

    def build_heap(self, arr):
        self.heap_list.extend(arr)
        self.current_size += len(arr)

        i = self.current_size // 2

        while i > 0:
            self.perc_down(i)
            i -= 1

    def del_min(self):
        out = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return out


heap = BinaryHeap()
heap.build_heap([9, 5, 6, 2, 3, 12, 100, -1, 23, 123])

print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
