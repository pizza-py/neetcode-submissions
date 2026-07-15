class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for number in nums:
            if str(number) not in counter.keys():
                counter[str(number)] = 1
            else:
                counter[str(number)] += 1
        print(counter)
        ordered = sorted(counter.keys(), key = lambda x: counter[x], reverse = True)
        return ordered[0 : k]
