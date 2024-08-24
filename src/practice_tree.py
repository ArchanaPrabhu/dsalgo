class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, node):
        temp = self

        while temp is not None:
            print("temp : ", temp.val, node.val)
            if node.val > temp.val:
                if temp.right is not None:
                    temp=temp.right
                else:
                    temp.right = node
                    print("insert to right : ", node.val)
                    break
            elif node.val < temp.val:
                if temp.left is not None:
                    temp=temp.left
                else:
                    temp.left = node
                    print("insert to left : ", node.val)
                    break

    # inorder traversal
    def traverse(self, node):
        if node is None:
            return
        self.traverse(node.left)
        print (node.val)
        self.traverse(node.right)

def isBalanced(node: TreeNode):
    ans = True
    print(findHeight(node, ans))

def findHeight(node: TreeNode, ans):
    if node is None:
        return True, 0
    currAnsL, leftHeight = findHeight(node.left, ans)
    currAnsR, rightHeight = findHeight(node.right, ans)
    print("findHeight : ", node.val, "left", node.left, leftHeight, currAnsL, "right", node.right, rightHeight, currAnsR)
    if abs(leftHeight - rightHeight) > 1:
        print("check height", abs(leftHeight - rightHeight))
        return False, 1 + max(leftHeight, rightHeight)
    return currAnsR or currAnsL, 1 + max(leftHeight, rightHeight)

if __name__ == "__main__":
    headNode = TreeNode(2)
    headNode.insert(TreeNode(1))
    headNode.insert(TreeNode(3))
    headNode.insert(TreeNode(4))
    headNode.insert(TreeNode(5))
    print("insert over")
    headNode.traverse(headNode)
    print("traverse over")
    isBalanced(headNode)

'''
    1
    |\
    2 3
   / \ 
  4   5
'''
