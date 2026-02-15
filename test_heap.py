#File for testing Heap.py
# Use python3 test_heap.py to test Heap.py

from Heap import Heap

h = Heap([3,1,6, 5, 2, 4])
print("Initial Heap:", h.data)

h.insert(10)
print("After Insert:", h.data)

print("Extracted max:", h.extract_max())
print("After extract:", h.data) # 10 got out
print("Heap sort:", h.heap_sort()) # Highest to lowest

# 
