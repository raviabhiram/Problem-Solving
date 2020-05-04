//  https://leetcode.com/problems/two-sum/
//  twoSum.cpp
//  C++
//
//  Created by Abhiram Bharadwaj on 5/4/20.
//  Copyright © 2020 Abhiram Bharadwaj. All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <map>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> result(2);
    map<int,int> sumMap;
    
    for (vector<int>::iterator it = nums.begin() ; it != nums.end(); ++it){
        if(sumMap.find(*it) != sumMap.end()){
            result[0] = sumMap[*it];
            result[1] = it - nums.begin();
            break;
        } else{
            sumMap[target - *it] = it - nums.begin();
        }
    }
    return result;
}
