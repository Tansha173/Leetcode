# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # declaring the head and pointer
        d = c = ListNode(0)
        # check condition for empty list
        while list1 and list2:
            if list1.val < list2.val:
                c.next = list1
                list1 = list1.next
            else:
                c.next = list2
                list2 = list2.next
            # incrementing the pointer
            c = c.next
        # if any of the lists is empty, apppend the remaining elements as it is
        c.next = list1 or list2
        
        return d.next
        
