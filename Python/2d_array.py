"""
Author: Abhiram Ravi Bharadwaj
Source: HackerRank
Problem: https://www.hackerrank.com/challenges/2d-array/problem
"""

arr = [[1,1,1,0,0,0],
[0,1,0,0,0,0],
[1,1,1,0,0,0],
[0,0,2,4,4,0],
[0,0,0,2,0,0],
[0,0,1,2,4,0]]

size = len(arr[0])-2
print(len(arr))
max = 0
for i in range(size):
    for j in range(size):
        sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        sum += arr[i+1][j+1]
        sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        max=sum if (sum > max or (i == 0 and j == 0)) else max

print(max)