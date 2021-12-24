class Stack():
    def __init__(self):
        self.s = []
    def add(self,i):
        self.s.append(int(i))
    def toxic(self):
        for i in range(0,len(self.s)):
            if self.s[i] % 2 == 1:
                self.s[i] += 2
            elif self.s[i] % 2 == 0:
                self.s[i] -= 1
    def look(self):
        num = []
        if len(self.s) == 0:
            print(0)
        elif len(self.s) == 1:
            print(1)
        else :
            for j in range(0,len(self.s)):
                if len(num) != 0:
                    while self.s[j] > num[-1]:
                        num.pop()
                        if len(num) == 0:
                            num.append(self.s[j])
                            break
                    if self.s[j] < num[-1]:
                        num.append(self.s[j])
                else:
                    num.append(self.s[j])
            print(len(num))
inp = [k for k in input("Enter Input : ").split(",")]
s = Stack()
for l in range(0,len(inp)):
    print(inp[l])
    if inp[l] == 'B':
        s.look()
    elif inp[l] == 'S':
        s.toxic()
    else:
        A, value = inp[l].split()
        if A == 'A':
            s.add(value)