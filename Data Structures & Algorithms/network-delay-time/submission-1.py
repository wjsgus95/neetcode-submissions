class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_times = [float('inf')] * n
        k -= 1
        min_times[k] = 0

        graph = defaultdict(set)
        for u, v, t in times:
            graph[u-1].add((v-1, t))
        
        heap = []
        heap.append((0, k))

        while heap:
            accumulated, src = heapq.heappop(heap)

            for dst, time in graph[src]:
                new_accumulated = accumulated + time
                if new_accumulated < min_times[dst]:
                    min_times[dst] = new_accumulated
                    heapq.heappush(heap, (new_accumulated, dst))
        
        return -1 if max(min_times) == float('inf') else max(min_times)
