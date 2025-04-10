from tensor import Tensor
from model import NeuralNet

# Dummy data
X = Tensor([0.2, 0.7])
Y = Tensor([1])

net = NeuralNet()
net.train(X, Y, epochs=10)
print("Training complete!")
