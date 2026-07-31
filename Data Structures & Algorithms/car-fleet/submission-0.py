class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionsAndSpeeds = sorted(zip(position,speed), key=lambda x: x[0])
        fleets = 0
        currentMaxTime = 0
        for i in range(len(positionsAndSpeeds)-1, -1, -1):
            myCar = positionsAndSpeeds[i]
            timeTaken = (target - myCar[0]) / myCar[1] 
            if timeTaken <= currentMaxTime:
                pass
            else:
                currentMaxTime = timeTaken
                fleets += 1
        
        return fleets
        