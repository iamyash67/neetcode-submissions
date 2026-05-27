class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j] == target:
        #             return [i+1,j+1]
        l, r = 0,len(numbers)-1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1,r + 1]
            if total > target:
                r = r-1
            if total < target:
                l = l+1