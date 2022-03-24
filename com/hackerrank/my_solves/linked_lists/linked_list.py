class ListNode:
    def __init__(self, data=0):
        self.val = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = ListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def printLinkedList(self, head):
        while head:
            print(head.val)
            head = head.next


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    llist.printLinkedList(llist.head)
    print(llist.head.val)
