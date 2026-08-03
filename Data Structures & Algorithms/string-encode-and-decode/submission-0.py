class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr: list[str] = []

        for x in strs:
            encoded_arr.append(self._length_to_bytes(x) + x)

        return "".join(encoded_arr)

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        decoded_strings: list[str] = []

        while i < n:
            length = self._bytes_to_length(s[i:i+4])
            i += 4

            decoded_strings.append(s[i:i+length])
            i += length
        
        return decoded_strings

    def _length_to_bytes(self, x: str) -> str:
        length = len(x)
        bytes_list = []

        for i in range(4):
            bytes_list.append(chr(length >> (i * 8)))

        bytes_list.reverse()

        return "".join(bytes_list)

    def _bytes_to_length(self, bytes_str: str) -> int:
        result = 0
        
        for c in bytes_str:
            result = result * 256 + ord(c)

        return result
