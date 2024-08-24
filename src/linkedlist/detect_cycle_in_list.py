class Node:
    def __init__(self, data, node=None):
        self.data = data
        self.next = node

    def insert(self, node=None):
        temp = self
        while temp.next is not None:
            temp = temp.next
        temp.next = node


# 1-2-3-4-5
#   |     |
#   - - - -
def find_cycle(head) -> bool:
    slow = head
    fast = head.next
    while slow != fast:
        print(slow.data, " ", fast.data)
        if fast is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

def solution():
    head = Node(1)
    loopNode = Node(2)
    head.insert(loopNode)
    head.insert(Node(3))
    head.insert(Node(4))
    loopNode2 = Node(5)
    head.insert(loopNode2)
    loopNode2.insert(loopNode)
    print(find_cycle(head))

if __name__ == "__main__":
    solution()