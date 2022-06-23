class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언 - 데크=양방향 큐
        strs: Deque = collections.deque()
            
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True
                