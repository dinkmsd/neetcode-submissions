class MinStack:

    def __init__(self):
        self.main_stack = []
        self.extra_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if len(self.extra_stack) > 0:
            if val < self.extra_stack[-1]:
                self.extra_stack.append(val)
            else:
                self.extra_stack.append(self.extra_stack[-1])
        else:
            self.extra_stack.append(val)

    def pop(self) -> None:
        self.main_stack.pop()
        self.extra_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.extra_stack[-1]

