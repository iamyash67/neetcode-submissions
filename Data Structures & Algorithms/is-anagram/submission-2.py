class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count1 , count2 = {} , {}
        for i in s:
            count1[i] = count1.get(i, 0) + 1
        for j in t:
            count2[j] = count2.get(j, 0) + 1
        return count1.items() == count2.items()