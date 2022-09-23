class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                
            # 자신 이전의 모든 값을 고정하여 재귀 호출 - (순열에서는 자기 자신만 제외했음)
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
                
        dfs([],1,k) # 1씩 줄여나가며 재귀 호출
        return results