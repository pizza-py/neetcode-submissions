class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = ""
        new = [t.join(sorted(string)) for string in strs]
        output = {}
        added = []
        for i in range(len(new)):
            if new[i] not in added:
                added.append(new[i])
                output[new[i]] = [strs[i]]
            else:
                output[new[i]].append(strs[i])
        return list(output.values())

        