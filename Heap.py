# Heap.py
# Implementation Assignment 2 (IA2)


class Heap:
    def __init__(self, arr=None):
        if arr is None:
            self.data = []
        else: 
            self.data = arr
            self.build_heap()

    def __del__(self):
        del self.data

# Part 1: The funcions
    def find_left(self, index):
        left = 2 * index + 1
        return left if left < len(self.data) else None
    
    def find_right(self, index):
        right = 2 * index + 2
        return right if right < len(self.data) else None
    
    def find_parent(self, index):
        if index == 0:
            return None
        return (index - 1) // 2
    
    def get_value(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None
    
    def heap(self, index):
        #Heap goes down from the index
        largest = index
        left = self.find_left(index)
        right = self.find_right(index)

        if left is not None and self.data[left] > self.data[largest]:
            largest = left
        
        if right is not None and self.data[right] > self.data[largest]:
            largest = right
        
        if largest != index:
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            self.heap(largest)

    def build_heap(self):
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self.heap(i)

# Part 2: ADD on

    def extract_max(self):
        if len(self.data) == 0:
            return None
        
        max_value = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        if len(self.data) > 0:
            self.heap(0)
        return max_value
    
    def insert(self, value):
        self.data.append(value) # Insert a new value into the heap
        index = len(self.data) - 1
        parent = self.find_parent(index)

        # Using a Bubble up method to maintain the heap's propeerties
        while parent is not None and self.data[index] > self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = self.find_parent(index)
    
    def heap_sort(self):
        temp = self.data.copy()
        result = []

        while len(self.data) > 0:
            result.append(self.extract_max())

        self.data = temp # The original heap is restored
        return result
