#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next


#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insert_node_at_position(llist, data, position):
    if position == 0:
        new_head = SinglyLinkedListNode(data)
        new_head.next = llist
        return new_head
    else:
        temp = llist
        while position > 1:
            temp = temp.next
            position -= 1
        new_node = SinglyLinkedListNode(data)
        next_node = temp.next
        temp.next = new_node
        new_node.next = next_node
        return llist


# Write your code here

if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input("Enter data to be inserted: "))

    position = int(input("Enter position: "))

    llist_head = insert_node_at_position(llist.head, data, position)

    print_singly_linked_list(llist_head)
    print(llist.head)
    print(llist.tail)