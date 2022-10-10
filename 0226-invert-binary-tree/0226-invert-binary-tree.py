# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root: # 루트마다
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left) # 스왑 이용
            return root
        return None # 파이썬은 자연스럽게 None을 할당하기 때문에 생략 가능
        