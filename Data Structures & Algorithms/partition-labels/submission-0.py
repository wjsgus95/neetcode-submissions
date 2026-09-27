class Solution:
    # 'abcabc'
    # { a: 3, b: 4, c: 5}
    def partitionLabels(self, s: str) -> List[int]:
        window = set()

        last_positions = dict()
        for i, c in enumerate(s):
            last_positions[c] = i
        
        ans = []
        size = 0
        for i in range(len(s)):
            window.add(s[i])
            size += 1

            closeable = True
            for c in window:
                if last_positions[c] > i:
                    closeable = False
                    
            if closeable:
                ans.append(size)
                window = set()
                size = 0
        
        return ans
