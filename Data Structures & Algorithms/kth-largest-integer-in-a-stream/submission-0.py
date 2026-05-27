class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heapm = nums
        self.k = k
        heapq.heapify(self.heapm)
        while len(self.heapm) > self.k:
            heapq.heappop(self.heapm)

    def add(self, val: int) -> int:
        heapq.heappush(self.heapm , val)
        if len(self.heapm) > self.k:
            heapq.heappop(self.heapm)
        return self.heapm[0]

