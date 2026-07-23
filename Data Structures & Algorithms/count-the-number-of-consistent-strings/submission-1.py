class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len(list(filter(lambda x: set([x[i] in set(allowed) for i in range(len(x))]) == {True}, words)))
        