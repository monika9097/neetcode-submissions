class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch not in {"+","-","*","/"}:
                stack.append(int(ch))
            else:
                x = stack.pop()
                y = stack.pop()

                if ch =="+":
                    stack.append(y+x)
                elif ch == "-":
                    stack.append(y-x)
                elif ch == "*":
                    stack.append(y*x)
                else:
                    stack.append(int(y/x))
        return stack[-1]

           

        