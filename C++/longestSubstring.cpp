//  https://leetcode.com/problems/longest-substring-without-repeating-characters/
//  longestSubstring.cpp
//  C++
//
//  Created by Abhiram Bharadwaj on 5/5/20.
//  Copyright © 2020 Abhiram Bharadwaj. All rights reserved.
//

#include <stdio.h>
#include <string>
#include <map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxTillNow[s.length()+1], count = 0, start = 0;
        maxTillNow[0]=0;
        map<char,int> charMap;
        for(int i = 0; i < s.length(); i++){
            if(charMap.find(s[i]) != charMap.end() && charMap[s[i]] > start){
                count = i - charMap[s[i]] - 1;
                start = charMap[s[i]] + 1;
            }
            charMap[s[i]] = i;
            count++;
            maxTillNow[i+1] = max(maxTillNow[i], count);
        }
        return maxTillNow[s.length()];
    }
};
