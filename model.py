from tensor import Tensor

class Linear:
    def __init__(self, input_size, output_size):
        import random
        self.weights = Tensor([random.uniform(-1, 1) for _ in range(input_size * output_size)])
        self.bias = Tensor([0] * output_size)

    def forward(self, x):
        return x * self.weights + self.bias

class NeuralNet:
    def __init__(self):
        self.layer = Linear(2, 1)

    def forward(self, x):
        return self.layer.forward(x).relu()

    def train(self, x, y, epochs=100, lr=0.01):
        for _ in range(epochs):
            pred = self.forward(x)
            loss = (pred - y).mean()
            self.layer.weights.backward(loss.grad)
            self.layer.bias.backward(loss.grad)
            self.layer.weights.data = [w - lr * w.grad for w in self.layer.weights.data]
            self.layer.bias.data = [b - lr * b.grad for b in self.layer.bias.data]
