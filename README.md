 Find Kth Largest Element in an Array (python)

This repository contains a Python implementation to find the k-th largest element in an unsorted array using the heap strategy from Python’s 'heapq' module.

Problem Statement

Find Kth Largest Element in an Array 
Given an unsorted list and an integer k, find the k-th largest element in the list.

Note: The k-th largest element means the element that would appear in position 'k' if the list were sorted in descending order.
 Approach: Heap

We use a heap of size 'k'. As we iterate through the array:
- Push every number into the heap.
- If the heap size exceeds 'k', we remove the smallest element.
- After processing all elements, the smallest in the heap (heap[0]) is the k-th largest element.
