class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()
        # dup = 0
        # for i in nums:
        #     if i in seen:
        #         dup = i
        #     seen.add(i)
        # return dup

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
