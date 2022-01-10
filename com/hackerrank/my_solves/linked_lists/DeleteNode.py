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
        print(node.data)
        node = node.next


def deleteNode(llist, position):
    # Write your code here
    if llist is None:
        return
    if position == 0:
        return llist.next
    temp = llist
    while position != 1:
        temp = temp.next
        position -= 1
    delete_node = temp.next
    temp.next = delete_node.next
    del delete_node

    return llist

# Write your code here

if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input("Enter position: "))

    llist_head = deleteNode(llist.head, position)

    print_singly_linked_list(llist_head)

