class StackMachine:
    def __init__(self):
        self.stack = Stack()
        self.mem = {}
        self.currentLine = 0

    def Execute(self, tokens):  # Takes Tokenized list (from prog4_1) and performs
        # arithmetic/stack operations based on this input
        func1 = {
            "pop": self.Pop,
            "add": self.Add,
            "sub": self.Sub,
            "mul": self.Mul,
            "div": self.Div,
            "mod": self.Mod,
            "skip": self.Skip,
        }
        func2 = {
            "push": self.Push,
            "save": self.Save,
            "get": self.Get
        }
        for i in range(0, len(tokens)):
            if (tokens[i] in func1):
                call = func1[tokens[i]]
                out = call()
            if (tokens[i] in func2):
                call = func2[tokens[i]]
                out = call(int(tokens[i + 1]))
        self.currentLine = self.currentLine + 1
        if out is not None:
            return out

    def Push(self, x):  # Add item to stack
        self.stack.Push(x)

    def Pop(self):  # Remove item from stack
        return self.stack.Pop()

    def Add(self):  # Take two items from stack, add together
        val1 = self.stack.Pop()
        val2 = self.stack.Pop()
        self.stack.Push(val1 + val2)

    def Sub(self):  # Take two items from stack, subtract one from other
        val1 = self.stack.Pop()
        val2 = self.stack.Pop()
        self.stack.Push(val1 - val2)

    def Mul(self):  # Take two items from stack, multiply together
        val1 = self.stack.Pop()
        val2 = self.stack.Pop()
        self.stack.Push(val1 * val2)

    def Div(self):  # Take two items from stack, divide one from other
        val1 = self.stack.Pop()
        val2 = self.stack.Pop()
        self.stack.Push(val1 / val2)

    def Mod(self):  # Take two items from stack, divide one from other, use remainder
        val1 = self.stack.Pop()
        val2 = self.stack.Pop()
        self.stack.Push(val1 % val2)

    def Skip(self):  # If first item on stack is 0, add value of
        val1 = self.stack.Pop()  # second item to loop incrementation
        val2 = self.stack.Pop()
        if (not val1):
            self.currentLine = self.currentLine + val2

    def Save(self, x):  # Take item from stack and place in memory
        self.mem[x] = self.Pop()

    def Get(self, x):  # Take item from memory and place on stack
        if (x not in self.mem):
            raise IndexError("Invalid Memory Access")
        self.stack.Push(self.mem[x])


class Stack:  # Data structure forming the basis for the StackMachine class
    def __init__(self):
        self.data = []

    def Push(self, val):
        self.data.append(val)

    def Pop(self):
        if (len(self.data) == 0):
            raise IndexError("Invalid Memory Access")
        return self.data.pop()

    def Peek(self):
        if (len(self.data) == 0):
            raise IndexError("Invalid Memory Access")
        return self.data[len(self.data) - 1]

    def giveMe(self, yourPhone):  # Give Me Your
        self.Push(yourPhone)
