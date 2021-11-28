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


def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next


def insert_node_at_head(link_list, data):
    node = SinglyLinkedListNode(data)
    if link_list:
        node.next = link_list
    return node


if __name__ == '__main__':

    llist_count = int(input())

    linked_list = SinglyLinkedList()  # initiated singly linked list with head = None

    for i in range(llist_count):
        item = int(input())
        inserted_node = insert_node_at_head(linked_list.head, item)
        linked_list.head = inserted_node

    print_singly_linked_list(linked_list.head)
