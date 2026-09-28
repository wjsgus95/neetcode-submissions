class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        N = len(gas)
        diff = [gas[i] - cost[i] for i in range(N)]
        print(diff)
        balance = 0

        begin = 0
        for index in range(N):
            balance += diff[index]

            if balance < 0:
                begin = index + 1
                balance = 0

        return begin
            