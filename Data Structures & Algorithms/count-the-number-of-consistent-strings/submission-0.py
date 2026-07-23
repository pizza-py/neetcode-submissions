class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        return len(list(filter(lambda x: set([x[i] in allowedSet for i in range(len(x))]) == {True}, words)))
        