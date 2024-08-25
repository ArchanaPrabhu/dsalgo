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


def solution(head):
    print(dfs(head))

def dfs(node: Node):
    if node is None:
        return 0
    return node.data + max(dfs(node.left), dfs(node.right))

if __name__ == "__main__":
    #      2
    # 6        4
    #   8    7
    #         2
    head = Node(2)
    head.insertRight(4).insertRight(17).insertRight(2).insertRight(6).insertRight(8)
    head.traversal()
    solution(head)
