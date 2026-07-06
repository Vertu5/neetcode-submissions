class Solution:
    def sortColors(self, nums: list[int]) -> None:
        zero_indice = 0
        two_indice = len(nums) - 1
        i = 0 

        # On s'arrête quand i croise la zone des 2
        while i <= two_indice:
            if nums[i] == 1:
                i += 1
                
            elif nums[i] == 0:
                nums[i], nums[zero_indice] = nums[zero_indice], nums[i]
                zero_indice += 1
                i += 1
                
            else: # nums[i] == 2
               
                nums[i], nums[two_indice] = nums[two_indice], nums[i]
                two_indice -= 1
                # On NE FAIT PAS i += 1 ici parce que l on a pas encore regarder l element que l on a changer !