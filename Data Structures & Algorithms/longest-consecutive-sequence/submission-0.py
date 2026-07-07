class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_seq = 0

        for num in hashset: 
            # Dès qu'on trouve un starter, on calcule la séquence
            if (num - 1) not in hashset:
                temp = num
                max_len = 1

                while temp + 1 in hashset:
                    temp += 1
                    max_len += 1
                
                max_seq = max(max_seq, max_len)

        return max_seq