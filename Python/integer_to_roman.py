"""
Author: Abhiram Ravi Bharadwaj
Source: Leetcode
Problem: https://leetcode.com/problems/integer-to-roman/
"""

num = 49
roman_map = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}
checkpoints=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
ans = ''
while num >= 1000:
    num-=1000
    ans+=roman_map[1000]
while num > 0:
    for i in range(len(checkpoints)):
        if checkpoints[i] > num:
            break
    i-=1
    num-=checkpoints[i]
    ans+=roman_map[checkpoints[i]]
return ans
