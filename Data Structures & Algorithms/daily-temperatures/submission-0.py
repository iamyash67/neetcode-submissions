class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = []
        # for i in range(len(temperatures)):
        #     count = 0
        #     found = False
        #     for j in range(i+1, len(temperatures)):
        #         count=count+1
        #         if temperatures[j] > temperatures[i]:
        #             found = True
        #             break
        #     result.append(count if found else 0)
        # return result
        result = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackt, stackidx = stack.pop()
                result[stackidx] = i - stackidx
            stack.append((temp, i))
        return result