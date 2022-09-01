# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # lists에는 입력값이 들어감
        # 전체적으로는 리스트 형태이지만 각 원소는 연결 리스트 형태임
        root = result = ListNode(None)
        # ListNode(None)은 data와 next를 None으로 둔 연결 리스트
        
        heap = []
        
        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
        # lists의 각 원소는 연결 리스트
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                # heappush를 이용해서 heap에 저장
                
        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
        # heap이 비어있을 때까지 while문 돌림
            node = heapq.heappop(heap)
            # 가장 작은 원소부터 오름차순으로 heap의 원소 추출하기 때문에 heap 구조로 변경한 것임
            # 추출된 원소는 heap에서 제거됨
            idx = node[1]
            result.next = node[2]
            result = result.next
            
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
                
        return root.next
        