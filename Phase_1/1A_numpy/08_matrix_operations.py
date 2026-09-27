import numpy as np

print("--- Vector Basics ---")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a:", a)
print("b:", b)

print("a shape:", a.shape)
print("b shape:", b.shape)

print("\na + b:")
print(a + b)

print("\na - b:")
print(a - b)

print("\na * b:")
print(a * b)

print("\n--- Dot Product ---")

dot_result = np.dot(a, b)

print("np.dot(a, b):")
print(dot_result)

dot_result_alt = a @ b

print("\na @ b:")
print(dot_result_alt)

print("\n--- Matrix Basics ---")

A = np.array([
    [1, 2],
    [3, 4],
])

B = np.array([
    [5, 6],
    [7, 8],
])

print("A:")
print(A)
print("Shape:", A.shape)

print("\nB:")
print(B)
print("Shape:", B.shape)

print("\n--- Matrix Addition ---")

print(A + B)

print("\n--- Element-Wise Matrix Multiplication ---")

print(A * B)


print("\n--- Matrix Multiplication ---")

matrix_product = A @ B

print(matrix_product)


print("\n--- Matrix Shape Example ---")

X = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

W = np.array([
    [1, 0],
    [0, 1],
    [1, 1],
])

print("X shape:", X.shape)
print("W shape:", W.shape)

output = X @ W

print("\nOutput:")
print(output)

print("Output shape:", output.shape)

print("\n--- Tiny Neural Layer ---")

X = np.array([
    [0.2, 0.5, 0.7],
    [0.9, 0.1, 0.4],
])

W = np.array([
    [0.5, -0.2],
    [0.3, 0.8],
    [0.7, 0.1],
])

layer_output = X @ W

print("X shape:", X.shape)
print("W shape:", W.shape)

print("\nLayer output:")
print(layer_output)

print("Output shape:", layer_output.shape)

bias = np.array([0.1, -0.1])

layer_output_with_bias = X @ W + bias

print("\nLayer output with bias:")
print(layer_output_with_bias)



print("\n--- Transpose ---")

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print("Original:")
print(matrix)
print("Shape:", matrix.shape)

transposed = matrix.T

print("\nTransposed:")
print(transposed)
print("Shape:", transposed.shape)

print("\n--- 1D Transpose Surprise ---")

v = np.array([1, 2, 3])

print("Original shape:", v.shape)
print("Transposed shape:", v.T.shape)

print(v.T)

print("\n--- Identity Matrix ---")

I = np.eye(3)

print(I)


M = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9],
])

print("\nM @ I:")
print(M @ I)

print("\n--- Matrix Inverse Preview ---")

A = np.array([
    [2.0, 1.0],
    [1.0, 2.0],
])

A_inverse = np.linalg.inv(A)

print("A:")
print(A)

print("\nInverse:")
print(A_inverse)

print("\nA @ inverse:")
print(A @ A_inverse)


print("\n--- Vector Magnitude ---")

vector = np.array([3, 4])

magnitude = np.linalg.norm(vector)

print("Vector:", vector)
print("Magnitude:", magnitude)


print("\n--- Distance Between Vectors ---")

position_a = np.array([2, 3])
position_b = np.array([8, 7])

difference = position_b - position_a
distance = np.linalg.norm(difference)

print("Position A:", position_a)
print("Position B:", position_b)

print("Difference:", difference)
print("Distance:", distance)

print("\n--- RL Observation Matrix ---")

observations = np.array([
    [0.2, 0.4, 0.8],
    [0.5, 0.1, 0.3],
    [0.9, 0.7, 0.2],
], dtype=np.float32)

weights = np.array([
    [0.5, 0.2],
    [0.1, 0.8],
    [0.6, -0.3],
], dtype=np.float32)

bias = np.array([0.1, -0.2], dtype=np.float32)

scores = observations @ weights + bias

print("Observations shape:")
print(observations.shape)

print("Weights shape:")
print(weights.shape)

print("Bias shape:")
print(bias.shape)

print("\nScores:")
print(scores)

print("Scores shape:")
print(scores.shape)