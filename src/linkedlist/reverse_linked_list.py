class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

    def insert(self, node=None):
        temp = self
        while temp.next:
            temp = temp.next
        temp.next = node

    def traversal(self):
        temp = self
        print("traversal", temp.data)
        while temp is not None:
            print(temp.data, " ->")
            temp = temp.next


def reverseLinkedList(head):
    current = head
    nextNode = current.next
    current.next = None
    while nextNode is not None:
        nextToNext = nextNode.next
        nextNode.next = current
        current = nextNode
        nextNode = nextToNext
    current.traversal()

def reverseLinkedListPractice(headNode):
    current = headNode
    nextNode = current.next

    # This is only for the first node case
    current.next = None

    while nextNode is not None:
        nextToNext = nextNode.next
        nextNode.next = current
        current = nextNode
        nextNode = nextToNext
    current.traversal()


if __name__ == "__main__":
    head = Node(1)
    head.insert(Node(2))
    head.insert(Node(3))
    head.insert(Node(4))
    head.insert(Node(5))
    head.traversal()
    reverseLinkedListPractice(head)

