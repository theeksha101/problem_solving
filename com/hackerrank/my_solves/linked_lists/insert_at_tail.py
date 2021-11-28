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


def print_singly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next


# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insert_node_at_tail(head, data):
    temp = head
    if head is None:
        return SinglyLinkedListNode(data)  # return new node with data = int, next = None
    else:
        while temp.next is not None:
            temp = temp.next
        temp.next = SinglyLinkedListNode(data)
    return head  # return new node with data = int, next = None


if __name__ == '__main__':

    llist_count = int(input())

    linked_list = SinglyLinkedList()  # initiated singly linked list with head = None

    for i in range(llist_count):
        item = int(input())
        inserted_node = insert_node_at_tail(linked_list.head, item)
        linked_list.head = inserted_node

    print_singly_linked_list(linked_list.head)
    print(linked_list.head.data)
