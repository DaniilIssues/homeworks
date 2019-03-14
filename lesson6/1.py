class Triangle():
    def __init__(self, a, b, c):
        if a<b+c and b<a+c and c<a+b:
            self.a = a
            self.b = b
            self.c = c
        else:
            print("Такой треугольник нельзя создать!")
            exit()

    def square(self):
        p = (self.a+self.b+self.c)/2
        s = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return s
    def perimetr(self):
        perim = self.a+self.b+self.c
        return perim
    def print_abc(self):
        return self.a, self.b, self.c

perv = Triangle(2, 2, 3)
print(perv.square())