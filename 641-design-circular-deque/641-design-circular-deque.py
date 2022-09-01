class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        
    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node:ListNode, new:ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node,n
        n.left = new
    
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node
        

    def insertFront(self, value: int) -> bool:
        '앞쪽에 노드를 추가하는 연산'
        if self.len == self.k:
            return False  # 새로운 노드 삽입시 최대 길이에 도달하면 False 리턴
        self.len += 1
        self._add(self.head, ListNode(value)) 
        return True # 이외에는 _add() 메소드를 이용해 head 위치에 노드 삽입
        
        
    def insertLast(self, value: int) -> bool:
        '뒤쪽에 노드를 추가하는 연산'
        if self.len == self.k:
            return False 
        self.len += 1
        self._add(self.tail.left, ListNode(value)) # head가 아닌 tail.left에 삽입함
        return True

    def deleteFront(self) -> bool:
        '데크 처음에 아이템을 삭제'
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        '데크 마지막에 아이템을 삭제'
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left) #??
        return True
        

    def getFront(self) -> int:
        '데크의 첫 번째 아이템을 가져옴'
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        '데크의 마지막 아이템을 가져옴'
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        '데크가 비어 있는지 여부 판별'
        return self.len == 0

    def isFull(self) -> bool:
        '데크가 가득 차 있는지 여부 판별'
        return self.len == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()