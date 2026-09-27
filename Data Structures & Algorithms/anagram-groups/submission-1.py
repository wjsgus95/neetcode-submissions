from collections import Counter, defaultdict
from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        counters = []
        def get_hash(counter: Counter) -> str:
            hash_val = ""
            for c in ascii_lowercase:
                hash_val += c
                hash_val += str(counter[c])
            return hash_val

        for s in strs:
            counter = Counter(s)
            counters.append(counter)
            table[get_hash(counter)].append(s)
        
        ans = []
        for key, value in table.items():
            ans.append(value)
        return ans
