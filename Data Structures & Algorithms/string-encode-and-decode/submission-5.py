class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "0"
        delim = "@#12"
        encoded = delim.join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "0":
            return []
        decoded = s.split("@#12")
        return decoded
