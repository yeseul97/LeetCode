class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        '''요소 x를 큐 마지막에 삽입'''
        self.input.append(x)
        

    def pop(self) -> int:
        '''큐 처음에 있는 요소를 제거'''
        self.peek()
        return self.output.pop()
        

    def peek(self) -> int:
        '''큐 처음에 있는 요소를 조회'''
        # output이 업으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        '''큐가 비어 있는지 여부를 리턴'''
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()