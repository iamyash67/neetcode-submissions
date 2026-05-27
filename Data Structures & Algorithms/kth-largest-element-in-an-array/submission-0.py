class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            minHeap.append(-n)
        heapq.heapify(minHeap)
        while k>0:
            largest = -heapq.heappop(minHeap)
            k-=1
        return largest
        