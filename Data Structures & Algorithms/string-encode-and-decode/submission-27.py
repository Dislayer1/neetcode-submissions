class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(word)) + "#" + word for word in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the end of the length.
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1

            # Read exactly 'length' characters.
            result.append(s[start:start + length])
            i = start + length

        return result