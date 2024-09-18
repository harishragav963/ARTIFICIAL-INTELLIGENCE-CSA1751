import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.weights2 = np.random.randn(hidden_size, output_size)

    def forward(self, X):
        self.hidden_layer = sigmoid(np.dot(X, self.weights1))
        self.output_layer = sigmoid(np.dot(self.hidden_layer, self.weights2))
        return self.output_layer

    def backward(self, X, y, learning_rate):
        output_error = y - self.output_layer
        output_delta = output_error * sigmoid_derivative(self.output_layer)

        hidden_error = output_delta.dot(self.weights2.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_layer)

        self.weights2 += self.hidden_layer.T.dot(output_delta) * learning_rate
        self.weights1 += X.T.dot(hidden_delta) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        for i in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)

# Example usage
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

nn = NeuralNetwork(2, 2, 1)
nn.train(X, y, 10000, 0.1)

print(nn.forward(X))