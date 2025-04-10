import math

class Tensor:
    def __init__(self, data):
        self.data = data
        self.grad = 0

    def __add__(self, other):
        return Tensor([x + y for x, y in zip(self.data, other.data)])

    def __mul__(self, other):
        return Tensor([x * y for x, y in zip(self.data, other.data)])

    def relu(self):
        return Tensor([max(0, x) for x in self.data])

    def mean(self):
        return sum(self.data) / len(self.data)

    def backward(self, grad):
        self.grad = grad
