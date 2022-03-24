# Definition for singly-linked list.

from com.hackerrank.my_solves.linked_lists import linked_list


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = linked_list.ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = linked_list.ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


sol = Solution()
l1 = linked_list.SinglyLinkedList()
l1.insert_node(1)
l1.insert_node(1)
l1.insert_node(8)

l2 = linked_list.SinglyLinkedList()
l2.insert_node(3)
l2.insert_node(2)
l2.insert_node(7)

result = sol.addTwoNumbers(l1.head, l2.head)
result_head = linked_list.SinglyLinkedList()
result_head.printLinkedList(result)
