class MinStack:

    def __init__(self):
        self._min_stack = Stack[int]()
        self._stack = Stack[int]()

    def push(self, val: int) -> None:
        self._stack.push(val)
        if self._min_stack.is_empty() or self._min_stack.top() >= val:
            self._min_stack.push(val)

    def pop(self) -> None:
        val = self._stack.pop()
        if val == self._min_stack.top():
            self._min_stack.pop()
        return val

    def top(self) -> int:
        return self._stack.top()
        

    def getMin(self) -> int:
        return self._min_stack.top()

class Stack[T = int]:
    def __init__(self):
        self._elements: list[T] = []

    def size(self):
        return len(self._elements)
    
    def top(self) -> T | None:
        if self.size() > 0:
            return self._elements[-1]
        return None
    
    def push(self, item: T) -> None:
        self._elements.append(item)
    
    def pop(self) -> T | None:
        if self.size() > 0:
            return self._elements.pop()
        return None
    
    def is_empty(self) -> bool:
        return self.size() == 0
