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

            if len(time) >= 1 and t <= time[-1]:
                continue
            else:
                time.append(t)
        return len(time)

