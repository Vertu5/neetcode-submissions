#Basic colution 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        countw_1,  takew_1 = 0, True
        countw_2, takew_2 = 0, True

        word =""
        while countw_1 < len(word1) or countw_2 < len(word2):

            if countw_1 < len(word1) and takew_1 == True:
                
                word += word1[countw_1] 
                countw_1 += 1
            else: takew_1 = False
            
            if countw_2 < len(word2) and takew_2 == True:
                
                word += word2[countw_2] 
                countw_2 += 1
            else: takew_2 = False

        return word



