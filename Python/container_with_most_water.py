"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/container-with-most-water/
"""

height = [1,8,6,2,5,4,8,3,7]

ans, i, j = 0, 0, len(height) - 1
while i < j :
    area = min(height[i], height[j]) * (j-i)
    ans = max(ans, area)
    if height[i]<height[j]:
        i+=1
    else:
        j-=1
return ans
