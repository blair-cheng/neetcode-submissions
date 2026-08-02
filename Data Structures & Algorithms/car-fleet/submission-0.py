class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # time[i] = (target - position[i])/speed[i]
        # time = car at position n-1 ~0 need how much time arrive target
        # cars = [[position, speed],range position from max ]
        time = []
        cars = sorted(zip(position, speed),reverse = True)

        for pos, spd in cars:
            t = (target - pos)/spd
            time.append(t)

            if len(time) >= 2 and time[-1]<=time[-2]:
                time.pop()
        return len(time)

