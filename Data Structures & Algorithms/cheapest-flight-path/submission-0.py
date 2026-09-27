from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for i in range(len(flights)):
            from_i, to_i, price_i = flights[i]
            graph[from_i][to_i] = price_i

        queue = deque() 
        queue.append((src, k, 0))

        ans = float('inf')
        while queue:
            node, stops, accumulated = queue.popleft()

            for neighbor in graph[node]:
                price = graph[node][neighbor]

                if neighbor == dst:
                    ans = min(ans, accumulated + price)

                if stops > 0:
                    queue.append((neighbor, stops - 1, accumulated + price))
        
        return ans if ans < float('inf') else -1
