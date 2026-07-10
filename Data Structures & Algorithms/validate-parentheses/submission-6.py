class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            top = len(stack) - 1
            match char:
                case "(":
                    stack.append(")")
                case "[":
                    stack.append("]")
                case "{":
                    stack.append("}")
                case ")":
                    if (top == -1 or stack[top] != char):
                        return False
                    if (stack[top] == char):
                        stack.pop()
                case "]":
                    if (top == -1 or stack[top] != char):
                        return False
                    if (stack[top] == char):
                        stack.pop()
                case "}":
                    if (top == -1 or stack[top] != char):
                        return False
                    if (stack[top] == char):
                        stack.pop()

        return not len(stack)
        