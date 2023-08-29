class Solution(object):
    def merge_v0(self, nums1, m, nums2, n):

        i, j, k = m - 1, n - 1, m + n - 1
        
        while j >= 0:
            if i < 0 or nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
            
    """Time complexity: O(m+n)
            We are iterating through both arrays once, so the time complexity is O(m+n).

    Space complexity: O(1)
            We are not using any extra space, so the space complexity is O(1)."""


solution = Solution()

nums1 = [1,2,3,0,0,0,0,0]
m = 3
nums2 = [2,3,4,5,6]
n = 5

solution.merge_v0(nums1, m, nums2, n)

print(nums1)
