class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
                
# Örnek liste
nums = [1, 2, 3, 4, 4]
solution = Solution()
result = solution.containsDuplicate(nums)
print("Contains Duplicate:", result)
