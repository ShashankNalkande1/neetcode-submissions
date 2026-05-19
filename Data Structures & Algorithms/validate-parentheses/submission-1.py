class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:

            # if closing bracket
            if char in pairs:

                # if stack empty OR mismatch
                if not stack or stack[-1] != pairs[char]:
                    return False

                stack.pop()

            else:
                # opening bracket
                stack.append(char)

        return len(stack) == 0