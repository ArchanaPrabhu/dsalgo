from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

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