class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        z=zip(position,speed)
        cars=sorted(z,reverse=True)
        fleet=0
        time=0
        max=0
        for pos,s in cars:
            time=(target-pos)/s
            if time>max:
                max=time
                fleet+=1
        return fleet

