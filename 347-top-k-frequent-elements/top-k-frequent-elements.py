class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        sorted_keys = sorted(hashmap.items(), key= lambda x: x[1], reverse=True)
        print(f"sorted keys are: {sorted_keys}")

        top_k_keys = [key for key, count in sorted_keys[:k]]

            
        return top_k_keys