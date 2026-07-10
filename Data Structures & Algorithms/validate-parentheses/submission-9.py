class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "}": "{", "]": "["}
        stack = []

        if not s:
            return True
        
        if s[0] in map.keys():
            return False

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if char in map.keys():
                    top = len(stack) - 1
                    if (top != -1 and stack[top] == map[char]):
                        stack.pop()
                    else:
                        return False

        return not len(stack)

        