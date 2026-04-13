class Solution:
    def isValid(self, s: str) -> bool:
        close = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for p in s:
            if p in close:
                if stack and stack[-1] == close[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        if not stack:
            return True 
        else:
            return False 
        