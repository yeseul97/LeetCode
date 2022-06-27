class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ss = [word for word in re.sub(r'[^\w\s]',' ',paragraph).lower().split() if word not in banned]
        cc = collections.Counter(ss) 
        result = cc.most_common(1)[0][0] 
        return result
