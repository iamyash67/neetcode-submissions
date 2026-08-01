class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cursum = 0
        minlength = float("inf")
        for right in range(len(nums)):
            cursum += nums[right]
            while cursum >= target:
                minlength = min(minlength, right - left + 1)
                cursum -= nums[left]
                left += 1
        return 0 if minlength == float('inf') else minlength
                