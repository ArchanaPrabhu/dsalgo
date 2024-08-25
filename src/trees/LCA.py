from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

    def insertLeft(self, left=None):
        self.left = Node(left)
        return self.left

    def insertRight(self, right=None):
        self.right = Node(right)
        return self.right

    def traversal(self):
        nodeq = deque()
        nodeq.append(self)
        print("traversing tree level order")
        while len(nodeq) > 0:
            popped_node = nodeq.popleft()
            print(popped_node.data)
            if popped_node.left is not None:
                nodeq.append(popped_node.left)
            if popped_node.right is not None:
                nodeq.append(popped_node.right)


def solution(x, y, head):
    queue = deque()
    queue.append(head)
    small = x
    big = y
    if x > y:
        small = y
        big = x
    ans = head.data
    while len(queue) > 0:
        popped_node = queue.popleft()
        if small < popped_node.data < big:
            ans = popped_node.data
        if popped_node.left is not None:
            queue.append(popped_node.left)
        if popped_node.right is not None:
            queue.append(popped_node.right)
    return ans

if __name__ == "__main__":
    #      20
    # 6        24
    #   8    7
    #      5  12
    head = Node(20)
    intermediate = head.insertRight(24).insertLeft(7)
    intermediate.insertLeft(5)
    intermediate.insertRight(12)
    head.insertLeft(6).insertRight(8)
    head.traversal()
    print("ans", solution(5, 12, head))
