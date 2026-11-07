class Solution:
    def isValid(self, s: str) -> bool:
         
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for bracket in s:
            if bracket in pairs:
                if not stack or stack.pop() != pairs[bracket]:
                    return False
            else:
                stack.append(bracket)

        return len(stack) == 0
        