class Solution:

    def __init__(self):
        self.stack = [] # 
        
        self.operator = {
            "+" : lambda a, b :  a + b,
            "-" : lambda a, b :  a - b,
            "*" : lambda a, b :  a * b,
            "/" : lambda a, b :  int(a/b)
        }

    def evalRPN(self, tokens: List[str]) -> int:
        for char in tokens: 
            if char in self.operator:
                under = self.stack.pop()
                above = self.stack.pop()

                self.stack.append(self.operator[char](above, under))

            else :
                self.stack.append(int(char))

        return self.stack.pop()