# Bucket sort solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums) + 1)] # we know buckets can only range from [1,n] as that is the frequency
        for n in nums:
            freq[n] = 1 + freq.get(n,0) # nice syntactic sugar with freq.get
        for n, count in freq.items():
            buckets[count].append(n) # bucket sort by element freq

        result = []
        for bucket in reversed(buckets):
            for n in bucket:
                result.append(n)
                if len(result) == k:
                    return result
        
        return result
# Min heap solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        for n in nums:
            freq[n] = 1 + freq.get(n,0)
        for n, count in freq.items():
            heapq.heappush(heap,(count,n))
            if len(heap) > k: # if heap has more than k elements than the top of the heap cannot be in the final result
                heapq.heappop(heap)

        result = []
        for count, n in heap:
            result.append(n)
        
        return result