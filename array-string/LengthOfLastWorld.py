class Solution:
    def lengthOfLastWord(self, s):

	#	return len(s.split()[-1])
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c
    

solution_instance = Solution()
s = "Hello World"
result = solution_instance.lengthOfLastWord(s)
print("Length of the last word:", result)


# The [::-1] syntax is used in Python to reverse a sequence, such as a string or a list. 
# When applied to a string, it reverses the order of its characters. 


# A simple Python solution to find the length of the last word in a given string.
# It iterates through the string in reverse order and calculates the length of the last word.
