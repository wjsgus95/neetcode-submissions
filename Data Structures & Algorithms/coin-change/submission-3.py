class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = dict()

        if amount == 0:
            return 0

        queue = deque()
        for coin in coins:
            dp[coin] = 1
            queue.append((1, coin))
        
        while queue:
            change, accumulated = queue.popleft()
            if accumulated == amount:
                return change
            
            for coin in coins:
                next_accumulated = accumulated + coin

                if next_accumulated > amount:
                    continue
                
                if next_accumulated in dp and dp[next_accumulated] <= change + 1:
                    continue

                dp[next_accumulated] = change + 1
                queue.append((change + 1, next_accumulated))
        
        return -1
