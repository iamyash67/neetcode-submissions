class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minHeap = []
        # for n in nums:
        #     minHeap.append(-n)
        # heapq.heapify(minHeap)
        # while k>0:
        #     largest = -heapq.heappop(minHeap)
        #     k-=1
        # return largest
        k = len(nums) - k
        def quickSelect(l,r):
            p, pivot = l , nums[r]
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r]=nums[r],nums[p]
            if p>k:
                return quickSelect(l,p-1)
            if p<k:
                return quickSelect(p+1,r)
            else:
                return nums[p]
        return quickSelect(0,len(nums)-1)
        
        
