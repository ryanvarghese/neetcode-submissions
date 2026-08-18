import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        topK = []
        for val in counts.keys(): 
            hq.heappush(topK, (counts[val], val))
            while len(topK) > k:
                hq.heappop(topK)
        return [val for count, val in topK]    
