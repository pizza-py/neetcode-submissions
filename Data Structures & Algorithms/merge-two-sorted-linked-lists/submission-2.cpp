/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */


class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* ptr1 = list1;
        ListNode* ptr2 = list2;
        ListNode* res = new ListNode(); 
        ListNode* cur = res;

        while ((ptr1 != nullptr) && (ptr2 != nullptr)){
            if (ptr1->val <= ptr2->val){
                cur->next = new ListNode(ptr1->val);
                ptr1 = ptr1->next;
                cur = cur->next;
            } else {
                cur->next = new ListNode(ptr2->val);
                ptr2 = ptr2->next;
                cur = cur->next;
            }
        }

        while ((ptr1 != nullptr)){
            cur->next = new ListNode(ptr1->val);
            ptr1 = ptr1->next;
            cur = cur->next;
        }

        while ((ptr2!= nullptr)){
            cur->next = new ListNode(ptr2->val);
            ptr2 = ptr2->next;
            cur = cur->next;
        }

        return res->next;
    }
};
