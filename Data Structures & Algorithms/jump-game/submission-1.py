class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ptr = 0
        while ptr < len(nums)-1:
            print(ptr)
            moves = {}
            for i in range(1, nums[ptr]+1):
                if ptr+i+nums[ptr+i] >= len(nums)-1:
                    return True
                moves[i] = i+nums[ptr+i] if nums[ptr+i] != 0 else 0
            
            if not moves:
                return False
            bestMove = max(moves, key=moves.get)
            if moves[bestMove] == 0:
                return False
            else:
                ptr += bestMove
        return True
