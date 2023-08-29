class Solution(object):
    def removeElement(self, nums, val):


        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
solution = Solution()

nums = [3, 2, 3, 2, 3, 3]
val = 3

new_length = solution.removeElement(nums, val)

print("New Length:", new_length)
print("Modified List:", nums[:new_length])