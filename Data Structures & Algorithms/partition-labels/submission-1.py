class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        window = set()

        last_positions = dict()
        for i, c in enumerate(s):
            last_positions[c] = i
        
        ans = []
        size = 0
        end = 0
        for i in range(len(s)):
            window.add(s[i])
            size += 1

            end = max(end, last_positions[s[i]])
            if end <= i:
                ans.append(size)
                window = set()
                size = 0
        
        return ans
