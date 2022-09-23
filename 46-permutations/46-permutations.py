class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []
        
        def dfs(elements):
            # 리프 노드일 때 결과 추가 (= 그래프의 마지막 노드) (=결과값)
            if len(elements) == 0:
                results.append(prev_elements[:]) # 참조하는 값(prev_elements)로 하는 것이 아니라 반드시 값을 복사하는 형태여야 함. 
                # [:]와 copy()와 deepcopy()는 같은 형태
                
            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
                
        dfs(nums)
        return results