import numpy as np

values = np.array([10, 20, 30, 40])

print("--- Scalar Broadcasting ---")
print("Original:")
print(values)

print("\nAdd scalar:")
print(values + 5)

print("\nMultiply scalar:")
print(values * 2)

print("\n--- 2D + 1D Broadcasting ---")

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])

offset = np.array([1, 2, 3])

print("Data:")
print(data)

print("\nOffset:")
print(offset)

print("\nResult:")
print(data + offset)

print("\n--- Feature Mean Subtraction ---")

features = np.array([
    [170, 65, 22],
    [180, 80, 25],
    [160, 55, 21],
], dtype=np.float32)

feature_means = features.mean(axis=0)

print("Features:")
print(features)

print("\nFeature means:")
print(feature_means)

centered = features - feature_means

print("\nCentered data:")
print(centered)


print("\n--- Row Broadcasting ---")

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

row_values = np.array([10, 20, 30])

print("Matrix shape:", matrix.shape)
print("Row values shape:", row_values.shape)

print(matrix + row_values)

print("\n--- Column Broadcasting ---")

column_values = np.array([
    [100],
    [200],
])

print("Matrix shape:", matrix.shape)
print("Column values shape:", column_values.shape)

print(matrix + column_values)

print("\n--- Incompatible Shapes ---")

a = np.zeros((4, 3))
b = np.array([1, 2, 3, 4])

print("a shape:", a.shape)
print("b shape:", b.shape)

# Uncomment this to see the broadcasting error:
#= print(a + b)

print("\n--- Fix With reshape() ---")

b_column = b.reshape(4, 1)

print("Original b shape:", b.shape)
print("Reshaped b shape:", b_column.shape)

print(a + b_column)

print("\n--- RL Telemetry Broadcasting ---")

telemetry = np.array([
    [80, 30, 1],
    [95, 20, 1],
    [-10, 100, 0],
    [70, 40, 1],
    [85, 25, 1],
], dtype=np.float32)

print("Telemetry:")
print(telemetry)
print("Shape:", telemetry.shape)

baseline = np.array([50, 30, 0], dtype=np.float32)

adjusted = telemetry - baseline

print("\nBaseline:")
print(baseline)

print("\nAdjusted telemetry:")
print(adjusted)

print("\n--- Feature Scaling Preview ---")

feature_max = telemetry.max(axis=0)

print("Feature maximums:")
print(feature_max)

scaled = telemetry / feature_max

print("\nScaled telemetry:")
print(scaled)

print("\n--- Standardization Structure Preview ---")

features = np.array([
    [10, 100],
    [20, 150],
    [30, 200],
    [40, 250],
], dtype=np.float32)

means = features.mean(axis=0)
stds = features.std(axis=0)

standardized = (features - means) / stds

print("Means:")
print(means)

print("\nStandard deviations:")
print(stds)

print("\nStandardized:")
print(standardized)

print("\n--- Shape Differences ---")

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3]])
c = np.array([
    [1],
    [2],
    [3],
])

print("a:")
print(a)
print("shape:", a.shape)

print("\nb:")
print(b)
print("shape:", b.shape)

print("\nc:")
print(c)
print("shape:", c.shape)

print("\n--- Row + Column Broadcast ---")

row = np.array([[10, 20, 30]])      # shape (1, 3)

column = np.array([
    [1],
    [2],
    [3],
    [4],
])                                  # shape (4, 1)

result = row + column

print("row shape:", row.shape)
print("column shape:", column.shape)
print("result shape:", result.shape)

print(result)