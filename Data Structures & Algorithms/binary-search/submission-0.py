class Solution:
    def _computeMiddle(self,left,right) -> int:
        return (left + right) // 2

    def search(self, nums: List[int], target: int) -> int:
        # Tes variables de départ
        left = 0
        right = len(nums) - 1

        # "Tant que la condition est vraie, je continue"
        while left <= right:
            middle = self._computeMiddle(left,right)
            # 2. Tu fais tes conditions (if, elif, else)
            if target == nums[middle] :
                return middle
            elif target > nums[middle] :
                left = middle + 1
                middle = self._computeMiddle(left,right)
            else : 
                right = middle - 1
                middle = self._computeMiddle(left,right)

        return -1 