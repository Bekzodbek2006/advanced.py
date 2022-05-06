class Num:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, value):
        return Num(self.x + value.x, self.y - value.y )

    def __repr__(self):
        return f'X {self.x}ga teng Y {self.y}ga teng'


num = Num(10,25)
num1  = Num(25,14)

result = num + num1
print(result)

#result X 35ga teng Y 11ga teng

