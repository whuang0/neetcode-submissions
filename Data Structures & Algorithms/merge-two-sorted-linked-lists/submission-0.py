# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # so the idea here is we compare the nodes, taking the lower value
        # otherwise if equal we just append it to the merged LL
        # use a dummy node to hold the value of the first
        # LL nodes. we have a value then a pointer.
        # we want to use a dummy node to create a fake head.
        # then afterwards we use that fake head and make it hold our merged LL
        dummyNode = node = ListNode()

        # iterate while there is still nodes in list 1 or 2
        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next 
            else:
                node.next = list1
                list1 = list1.next
            node = node.next
        # basically here, we set our node to the next value
        # so either list1 or list2's value then 
        node.next = list1 or list2 
        return dummyNode.next