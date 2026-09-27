class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        if N == 1:
            return 0

        parents = [i for i in range(N)]
        ranks = [0] * N

        def find(node: int) -> int:
            if node != parents[node]:
                parents[node] = find(parents[node])
            
            return parents[node]
        
        def union(n1: int, n2: int):
            p1 = find(n1)
            p2 = find(n2)

            if ranks[p1] < ranks[p2]:
                parents[p1] = p2
            elif ranks[p1] > ranks[p2]:
                parents[p2] = p1
            else:
                parents[p2] = p1
                ranks[p1] += 1

        edges = []
        for i in range(N):
            for j in range(i):
                dist_x = abs(points[j][0] - points[i][0])
                dist_y = abs(points[j][1] - points[i][1])
                dist = dist_x + dist_y

                edges.append((dist, i, j))
        edges.sort()

        ans = 0
        num_edges = 0
        for d, i, j in edges:
            if find(i) != find(j):
                union(i, j)
                ans += d
                num_edges += 1

                if num_edges == N - 1:
                    return ans
