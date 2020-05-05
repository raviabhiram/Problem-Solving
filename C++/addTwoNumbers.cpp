//  https://leetcode.com/problems/add-two-numbers/
//  addTwoNumbers.cpp
//  C++
//
//  Created by Abhiram Bharadwaj on 5/5/20.
//  Copyright © 2020 Abhiram Bharadwaj. All rights reserved.
//

#include <iostream>
class Solution {
    // Definition for singly-linked list.
    struct ListNode {
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };

public:
    // Recursive Approach - Also works, just uncomment.
//    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
//        ListNode *result = helper(l1,l2,0);
//        return result;
//    }
//
//    ListNode * helper(ListNode * l1, ListNode * l2, int carry){
//        int sum;
//        if (l1 == nullptr && l2 == nullptr)
//            return carry ? new ListNode(carry) : nullptr;
//        else if (l1 == nullptr){
//            sum = l2->val+carry;
//            l2 = l2->next;
//        }
//        else if (l2 == nullptr){
//            sum = l1->val+carry;
//            l1 = l1->next;
//        }
//        else{
//            sum = l1->val + l2->val + carry;
//            l1 = l1->next;
//            l2 = l2->next;
//        }
//        return new ListNode(sum%10, helper(l1, l2, sum/10));
//    }
    
    // Iterative Approach
    ListNode * addTwoNumbers(ListNode* l1, ListNode* l2){
        ListNode dummyHead(0), *p = & dummyHead;
        int carry = 0, sum = 0;
        while (l1 || l2 || carry){
            sum = (l1 ? l1->val :0) + (l2 ? l2->val :0) + carry;
            carry = sum / 10;
            p->next = new ListNode(sum % 10);
            p = p->next;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return dummyHead.next;
    }
};
