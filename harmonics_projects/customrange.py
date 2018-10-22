class CustomRange:
    def __init__(self, min=0, max=0):
        self.min = min
        self.max = max

    def __iter__(self):
        self.curr = self.min
        return self

    def __next__(self):
        numb = self.curr
        if self.curr >= self.max:
            raise StopIteration
        self.curr += 1
        return numb

for i in CustomRange(-1, 15):
    print(i)

print()

for i in CustomRange(20, 25):
    print(i)