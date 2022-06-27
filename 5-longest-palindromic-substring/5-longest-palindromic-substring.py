class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right): # 매칭이 되면 조건 만족하는 것까지 확장
            while left >=0 and right <=len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left + 1: right-1] # 슬라이싱은 n-1만큼 출력
    
        # 예외 처리 (풀이속도 향상시켜줌)  
        if len(s) < 2 or s == s[::-1]: # 전체 문자열일 경우 
            return s

        result = ''

        for i in range(len(s) - 1):
            result = max(result, 
                        expand(i,i+1), # 짝수 펠린드롬
                        expand(i,i+2), # 홀수 펠린드롬
                        key=len) # key는 어떤 기준으로 max를 찾을 것이냐

        return result