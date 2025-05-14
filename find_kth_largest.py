import heapq

def find_kth_largest(nums: list, k: int) -> int:
    
    heap=[]
   
    for num in nums:
        heapq.heappush(heap,num)
        if len(heap) > k:  # if current heap is greater than k
            heapq.heappop(heap)

    return heap[0]  # It returns the 0th element which is kth largest element
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))  
