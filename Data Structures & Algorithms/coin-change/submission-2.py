class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = defaultdict(bool)

        if amount == 0:
            return 0

        queue = deque()
        for coin in coins:
            visited[coin] = True
            queue.append((1, coin))
        
        while queue:
            change, accumulated = queue.popleft()
            if accumulated == amount:
                return change
            
            for coin in coins:
                next_accumulated = accumulated + coin

                if next_accumulated > amount:
                    continue
                
                if visited[next_accumulated]:
                    continue

                visited[next_accumulated] = True
                queue.append((change + 1, next_accumulated))
        
        return -1