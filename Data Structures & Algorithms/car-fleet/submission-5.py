class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        sort the zip(position, speed) in ascending order

        fleets = []

        iterate backwards
            compute the time at which each car will arrive.

            if not stack or stack[-1] <= time
                fleets.append(time)
            
        return len(fleets)



        target=10
        position=[0,4,2] -> [(0 2) (4 1) (2 3)]
        speed=[2,1,3]

        []

        target=10
        position=[4,1,0,7]
        speed=[2,2,1,1]

        zip(p,s) -> [(4 2) (1 2) (0 1) (7 1)]
        sorted(zip(p, s)) -> [(0 1) (1 2) (4 2) (7 1)]
        sorted(zip(p, s), reverse=True) -> [(7 1) (4 2) (1 2) (0 1)]


        '''
        # O(NLog(N)) Time | O(N) Space

        data = sorted(zip(position, speed), reverse=True)
        fleet_times = [] # [3]

        for _, (p, s) in enumerate(data):
            t = (target - p) / s # 3

            if not fleet_times or fleet_times[-1] < t:
                fleet_times.append(t)
            
        return len(fleet_times)