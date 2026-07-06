class Solution:
    def __init__(self):
        self.delimiter = '#'

    def encode(self, strs: list[str]) -> str:
        pieces = []

        for string in strs:
            chunk = f"{len(string)}{self.delimiter}{string}"
            pieces.append(chunk)

        return "".join(pieces)
    
    def decode(self, s: str) -> list[str]:
        decoded_words = []
        cursor = 0  # Ton pointeur principal

        while cursor < len(s): 
            j = cursor          

            while s[j] != '#':
                j += 1

            #now we can delimitate our int or the size of the word
            length_word = int(s[cursor:j])  
            word_start = j + 1
            word_end = word_start + length_word  

            # We can then take the word 
            word = s[word_start:word_end]
            decoded_words.append(word)

            cursor = word_end  
        
        return decoded_words