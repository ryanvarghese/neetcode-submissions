class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            encoded_string += '#' + str(len(word)) + '#' + word
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                length = 0
                i += 1
                r = i
                while s[r] != '#' and r < len(s):
                    r += 1
                length = int(s[i: r])
                i = r + 1
                end = i + length
                word = s[i: end]
                decoded_string.append(word)
                i = end
        return decoded_string


                


