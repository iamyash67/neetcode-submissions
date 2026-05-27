class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for m in range(0,n+1):
            count = 0
            b = m
            while b:
                if b & 1:
                    count += 1
                b = b >> 1
            res.append(count)
        return res

