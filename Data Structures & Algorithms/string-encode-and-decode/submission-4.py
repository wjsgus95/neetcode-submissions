class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + ':' + s)
        return ''.join(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = []

        def decode_token(begin: int) -> int:
            digits = []
            index = begin
            while s[index] != ':':
                digits.append(s[index])
                index += 1

            index += 1
            size = int(''.join(digits))

            content = s[index:index+size]
            decoded.append(content)

            return index + size
        
        pointer = 0
        while pointer < len(s):
            pointer = decode_token(pointer)
        
        return decoded
