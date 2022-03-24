from typing import Optional
from com.hackerrank.my_solves.linked_lists.linked_list import ListNode, SinglyLinkedList


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        newlist = ListNode()
        newlistptr = newlist

        while l1 and l2:
            if l1.val <= l2.val:
                newlistptr.next = l1
                l1 = l1.next
            else:
                newlistptr.next = l2
                l2 = l2.next
            newlistptr = newlistptr.next
        if l1 != None:
            newlistptr.next = l1
        else:
            newlistptr.next = l2
        return newlist.next


sol = Solution()
list1 = ListNode(1)
list1_next = ListNode(2)
list1_next_next = ListNode(4)
list1.next = list1_next
list1_next.next = list1_next_next
list2 = ListNode(1)
list2_next = ListNode(3)
list2_next_next = ListNode(4)
list2.next = list2_next
list2_next.next = list2_next_next
linklist = SinglyLinkedList()
linklist.printLinkedList(sol.mergeTwoLists(list1, list2))



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val < list2.val:
            nxthead = self.mergeTwoLists(list1.next, list2)
            list1.next = nxthead
            return list1
        else:
            nxthead = self.mergeTwoLists(list1, list2.next)
            list2.next = nxthead
            return list2
