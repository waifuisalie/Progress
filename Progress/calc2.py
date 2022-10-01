class Calculadora:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def add(self):
        return self.x + self.y
    def subtraction(self):
        return self.x - self.y    
    def multiply(self):
        return self.x * self.y
    def division(self):
        return self.x / self.y    
    def power(self):
        return self.x ** self.y
    def root(self):
        return self.x ** (1/self.y)

#programa principal

op1 = float(input('Give first value: '))
op2 = float(input('Give second value: '))

while op2 == 0:
    print('division by zero is incorrect!')
    op2 = float(input('give second value: '))

calc1 = Calculadora(op1,op2)

print('1 operando: ', calc1.x)
print('2 operando: ', calc1.y)
print('=======================')
print('sum is: ', calc1.add())
print('subtraction is: ', calc1.subtraction())
print('multiplication is: ', calc1.multiply())
print('division is: ', calc1.division())
print('power is: ', calc1.power())
print('root: ', calc1.root())
