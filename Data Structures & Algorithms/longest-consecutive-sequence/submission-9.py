class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        if nums == []:
            return 0
        length = 1
        print(ordered)
        differences = [ordered[i+1]-ordered[i] for i in range(len(ordered)-1)]
        print(differences)
        
        lengths = []
        for element in differences:
            if element == 1:
                length += 1
            elif element == 0:
                pass
            else:
                lengths.append(length)
                length = 1
        lengths.append(length)
        print(lengths)
        return max(lengths)
