class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            # add the previous two on top of the stack
            if i == "+":
                stack.append(stack[-1] + stack[-2])
                print(stack)

            elif i == "D":
                stack.append(stack[-1] * 2)
                print(stack)
            
            elif i == "C":
                stack.pop()
                print(stack)
                
            else:
                stack.append(int(i))
            
        return sum(stack)