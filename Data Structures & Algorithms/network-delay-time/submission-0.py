class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_times = [float('inf')] * n
        k -= 1
        min_times[k] = 0

        graph = defaultdict(set)
        for u, v, t in times:
            graph[u-1].add((v-1, t))
        
        queue = deque() 
        queue.append((k, 0))

        while queue:
            src, accumulated = queue.popleft()

            for dst, time in graph[src]:
                new_accumulated = accumulated + time
                if new_accumulated < min_times[dst]:
                    min_times[dst] = new_accumulated
                    queue.append((dst, new_accumulated))
        
        return -1 if max(min_times) == float('inf') else max(min_times)
