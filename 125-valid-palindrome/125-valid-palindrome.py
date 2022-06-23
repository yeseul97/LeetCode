class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # 문자열이 영어,한글,숫자로 되어있으면 참 리턴,아니면 거짓 리턴
                strs.append(char.lower()) # True이면 소문자로 바꿔서 추가
                
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
            
        return True