class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        E = len(tickets)
        visited = [False] * E

        graph = defaultdict(list)
        for index, (src, dst) in enumerate(tickets):
            graph[src].append((dst, index))
        
        for src in graph:
            graph[src].sort()

        ans = ["JFK"]
        def backtrack(src: str) -> bool:
            if len(ans) == E + 1:
                return True
            
            for dst, index in graph[src]:
                if not visited[index]:
                    visited[index] = True
                    ans.append(dst)

                    if backtrack(dst):
                        return True

                    visited[index] = False
                    ans.pop()
            
            return False
        
        backtrack("JFK")
        return ans
        