# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        res = []
        self.inorder(root, res)

        for i in range(1, len(res)):
            if res[i - 1] >= res[i]:
                return False
        return True

    def inorder(self, root, res):
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)


s = Solution()
print(s.isValidBST(root=[2, 1, 3]))
print(s.isValidBST(root=[5, 1, 4, null, null, 3, 6]))
