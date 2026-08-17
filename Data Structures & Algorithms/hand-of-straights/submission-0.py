class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for thing in hand:
            if thing in count:
                count[thing] += 1
            else:
                count[thing] = 1
        
        while count:
            seqStart = min(count)
            for i in range(groupSize):
                if seqStart + i not in count:
                    return False
                else:
                    count[seqStart + i] -= 1
                    if count[seqStart+i] == 0:
                        count.pop(seqStart+i)
        return True

        