class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                item1, item2 = stack.pop(), stack.pop()
                stack.append(item1 + item2)
            elif token == '-':
                item1, item2 = stack.pop(), stack.pop()
                stack.append(item2 - item1)
            elif token == '*':
                item1, item2 = stack.pop(), stack.pop()
                stack.append(item1 * item2)
            elif token == '/':
                item1, item2 = stack.pop(), stack.pop()
                stack.append(math.trunc(item2 / item1))
            else:
                stack.append(int(token))
        return stack[0]