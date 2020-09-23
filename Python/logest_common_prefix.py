"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/longest-common-prefix/
"""
strs=["flower","flow","flag"]
if len(strs)<1:
    return ''
ans, smallest, index = '', len(strs[0]), 0
for i in range(len(strs)):
    if len(strs[i]) < smallest:
        index = i
        smallest = len(strs[i])
word = strs[index]
for i in range(len(word)):
    for words in strs:
        if words[i] != word[i]:
            return ans
    ans+=word[i]
return ans
