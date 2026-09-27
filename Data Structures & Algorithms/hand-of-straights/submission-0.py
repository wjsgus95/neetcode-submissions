class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = [0] * 1001
        for num in hand:
            counts[num] += 1
        
        queue = deque()
        expected = 0
        for i, c in enumerate(counts):
            if c < expected:
                return False
            elif c > expected:
                queue.append((i + groupSize - 1, c - expected))
                expected += c - expected
            
            if queue and queue[0][0] == i:
                old_i, old_c = queue.popleft()
                expected -= old_c

        return True