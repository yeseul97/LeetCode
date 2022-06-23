class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit(): # 띄어쓰기 기준으로 자르고 식별자 제외 부분부터
                digits.append(log)
            else:
                letters.append(log)
                
        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 1부터의 문자로 sort해야함
        return letters + digits
        