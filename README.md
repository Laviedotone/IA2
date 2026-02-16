# IA2
# Implementaton of various operations

# Part one
### Implement a heap data-structure with a heap class
### Have an appropriate constructor and destructor

# Part two
## Build on to your previor program
#### -> Sort (heap_sort)
#### -> Extract max value (extract_max)
#### -> Insert values into the heap (insert)

# Analysis of the BEST and WORST case running times
## find_parent(index)
#### Best case: O(1)
#### Worst case: O(1)

## find_left
#### Best case: O(1)
####  WOrst case: O(1)

## find_right (index)
#### Best Case: O(1)
#### Worst Case: O(1)

## Heap(heapifiy)
#### Best Case: O(1) 
#### Worst Case: O(log n)

## Build_heap()
#### Best Case: O(n)
#### Worst Case: O(n)

## get_vaule(index)
#### Best Case: O(1)
#### Worst Case: O(1)

## extract_max()
#### Best Case: O(1) 
#### Worst Case: O(log n)

## insert(value)
#### Best CaSe: O(1)
#### Worst Case: O(log n)

## Heap_sort()
#### Best Case: O(nlogn)
#### Worst Case: O(nlogn)

##### SUMMARY: find_parent, find_left, find_right, get_value, and more similar functions with the same Best and Worst Case are know as constant-time operations. Since the operations will take the same amount of time regardless of what input you give it.

# To run the IA2 Assignment
## python3 test_heap.py