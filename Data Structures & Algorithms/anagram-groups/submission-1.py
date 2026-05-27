class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash1 = defaultdict(list)
        # for s in strs:
        #     sortedset=''.join(sorted(s))
        #     hash1[sortedset].append(s)
        # return list(hash1.values())
                
        hash2 = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for n in s:
                count[ord(n)-ord("a")] += 1
            hash2[tuple(count)].append(s)
        return list(hash2.values())