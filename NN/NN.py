import numpy as np
# Input data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Output labels
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Random weights for layer 1 (2 inputs -> 2 hidden neurons)
w1 = np.random.randn(2, 2)
b1 = np.zeros((1, 2))

# Random weights for layer 2 (2 hidden -> 1 output)
w2 = np.random.randn(2, 1)
b2 = np.zeros((1, 1))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return sigmoid(x) * (1 - sigmoid(x))

learning_rate = 0.1
for epoch in range(10000):
    # Forward pass
    z1 = np.dot(X, w1) + b1
    a1 = sigmoid(z1)
    
    z2 = np.dot(a1, w2) + b2
    a2 = sigmoid(z2)

    # Backward pass
    error = y - a2
    d_z2 = error * sigmoid_deriv(z2)
    d_w2 = np.dot(a1.T, d_z2)
    d_b2 = np.sum(d_z2, axis=0, keepdims=True)

    d_a1 = np.dot(d_z2, w2.T)
    d_z1 = d_a1 * sigmoid_deriv(z1)
    d_w1 = np.dot(X.T, d_z1)
    d_b1 = np.sum(d_z1, axis=0, keepdims=True)

    # Update weights and biases
    w1 += learning_rate * d_w1
    b1 += learning_rate * d_b1
    w2 += learning_rate * d_w2
    b2 += learning_rate * d_b2

    if epoch % 1000 == 0:
        loss = np.mean(error ** 2)
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

print("Final predictions:")
z1 = np.dot(X, w1) + b1
a1 = sigmoid(z1)
z2 = np.dot(a1, w2) + b2
a2 = sigmoid(z2)
print(np.round(a2))