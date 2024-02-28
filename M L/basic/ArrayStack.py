class ArrayStack:
    def __init__(self):
        self._stack: list[int] = []

    def size(self) -> int:
        return len(self._stack)
    
    def is_empty(self) -> bool:
        return self._stack == []
    
    def push(self, item:int):
        self._stack.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._stack.pop()
    
    # def peek(self) -> int:

    
if __name__ == "__main__":
    stack = ArrayStack()
    stack.push(1)
    stack.push(1)
    print(stack.pop())
