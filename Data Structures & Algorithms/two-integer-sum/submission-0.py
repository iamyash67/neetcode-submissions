class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):
        #     for j in range(0,len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #             return [i,j]
        hashmap = {}
        for i,n in enumerate(nums):
            hashmap[n]=i
        for i,n in enumerate(nums):
            difference = target - n
            if difference in hashmap and hashmap[difference] != i:
                return [i,hashmap[difference]]