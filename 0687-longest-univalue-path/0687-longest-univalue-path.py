# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result: int=0
        
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            
            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
                
            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            '''현재 노드는 양쪽 자식 노드를 모두 연결 할 수 있지만,
            현재 노드의 부모 노드에서는 지금의 양쪽 자식 노드를 동시에 연결할 수 없음'''
            '''단반향이기 때문에 양쪽 자식 노드 중 어느 한쪽 자식만 택할 수 있으며, 이는 트리의 특징임'''
            return max(left, right)
        
        dfs(root)
        return self.result