import numpy as np

print("--- reshape() ---")

values = np.arange(1, 13)

print("Original:")
print(values)

print("Shape:")
print(values.shape)

matrix = values.reshape(3, 4)

print("\nReshaped to (3, 4):")
print(matrix)
print("Shape:", matrix.shape)

print("\n--- Automatic Dimension with -1 ---")

automatic = values.reshape(3, -1)

print(automatic)
print("Shape:", automatic.shape)


automatic = values.reshape(-1, 2)

print(automatic)
print(automatic.shape)

print("\n--- Vector Shapes ---")

vector = np.array([10, 20, 30])

row_vector = vector.reshape(1, 3)
column_vector = vector.reshape(3, 1)

print("Original:")
print(vector)
print("Shape:", vector.shape)

print("\nRow vector:")
print(row_vector)
print("Shape:", row_vector.shape)

print("\nColumn vector:")
print(column_vector)
print("Shape:", column_vector.shape)


print("\n--- Flattening ---")

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

flattened = matrix.flatten()

print("Matrix:")
print(matrix)

print("\nFlattened:")
print(flattened)

print("Shape:", flattened.shape)

print("\n--- ravel() ---")

raveled = matrix.ravel()

print(raveled)

print("\n--- Adding Dimensions ---")

values = np.array([10, 20, 30])

column = values[:, np.newaxis]

print("Original:")
print(values)
print("Shape:", values.shape)

print("\nWith new axis:")
print(column)
print("Shape:", column.shape)

row = values[np.newaxis, :]

print("\nRow version:")
print(row)
print("Shape:", row.shape)

print("\n--- expand_dims() ---")

values = np.array([10, 20, 30])

expanded_axis_0 = np.expand_dims(values, axis=0)
expanded_axis_1 = np.expand_dims(values, axis=1)

print("Axis 0:")
print(expanded_axis_0)
print(expanded_axis_0.shape)

print("\nAxis 1:")
print(expanded_axis_1)
print(expanded_axis_1.shape)


print("\n--- squeeze() ---")

weird = np.array([[[10, 20, 30]]])

print("Before:")
print(weird)
print("Shape:", weird.shape)

squeezed = np.squeeze(weird)

print("\nAfter:")
print(squeezed)
print("Shape:", squeezed.shape)

print("\n--- Vertical Stacking ---")

run_1 = np.array([
    [1, 80],
    [2, 85],
])

run_2 = np.array([
    [3, 90],
    [4, 95],
])

combined = np.vstack((run_1, run_2))

print("Run 1:")
print(run_1)

print("\nRun 2:")
print(run_2)

print("\nCombined:")
print(combined)

print("Shape:", combined.shape)

print("\n--- Horizontal Stacking ---")

rewards = np.array([
    [80],
    [95],
    [70],
])

steps = np.array([
    [30],
    [20],
    [40],
])

combined_features = np.hstack((rewards, steps))

print(combined_features)
print("Shape:", combined_features.shape)

print("\n--- concatenate() ---")

a = np.array([
    [1, 2],
    [3, 4],
])

b = np.array([
    [5, 6],
    [7, 8],
])

rows_combined = np.concatenate((a, b), axis=0)
columns_combined = np.concatenate((a, b), axis=1)

print("Along axis 0:")
print(rows_combined)
print("Shape:", rows_combined.shape)

print("\nAlong axis 1:")
print(columns_combined)
print("Shape:", columns_combined.shape)


print("\n--- stack() ---")

episode_a = np.array([80, 30, 1])
episode_b = np.array([95, 20, 1])
episode_c = np.array([70, 40, 1])

episodes = np.stack(
    (episode_a, episode_b, episode_c),
    axis=0,
)

print(episodes)
print("Shape:", episodes.shape)


print("\n--- split() ---")

values = np.arange(1, 13)

parts = np.split(values, 3)

print("Original:")
print(values)

print("\nParts:")

for part in parts:
    print(part)


print("\n--- array_split() ---")

values = np.arange(1, 11)

parts = np.array_split(values, 3)

for part in parts:
    print(part)

print("\n--- Matrix Splitting ---")

data = np.array([
    [1, 80, 30, 1],
    [2, 95, 20, 1],
    [3, 70, 40, 1],
    [4, 85, 25, 1],
])

print("Data:")
print(data)

top, bottom = np.vsplit(data, 2)

print("\nTop:")
print(top)

print("\nBottom:")
print(bottom)

episode_column, measurements = np.hsplit(data, [1])

print("\nEpisode IDs:")
print(episode_column)

print("\nMeasurements:")
print(measurements)



dataset = np.array([
    [170, 65, 22, 0],
    [180, 80, 25, 1],
    [160, 55, 21, 0],
    [175, 72, 30, 1],
], dtype=np.float32)



print("\n--- Feature / Target Split ---")

X = dataset[:, :-1]
y = dataset[:, -1]

print("X:")
print(X)
print("Shape:", X.shape)

print("\ny:")
print(y)
print("Shape:", y.shape)

print("\n--- RL Telemetry Restructure ---")

telemetry = np.array([
    [1, 80, 30, 1],
    [2, 95, 20, 1],
    [3, -10, 100, 0],
    [4, 70, 40, 1],
    [5, 85, 25, 1],
], dtype=np.float32)

episode_ids = telemetry[:, 0]
metrics = telemetry[:, 1:]

print("Episode IDs:")
print(episode_ids)

print("\nMetrics:")
print(metrics)
print("Metrics shape:", metrics.shape)
rewards = metrics[:, 0]
steps = metrics[:, 1]
success = metrics[:, 2]

print("\nRewards:")
print(rewards)

print("\nSteps:")
print(steps)

print("\nSuccess:")
print(success)


rewards_column = rewards.reshape(-1, 1)
steps_column = steps.reshape(-1, 1)
success_column = success.reshape(-1, 1)

rebuilt = np.hstack(
    (
        rewards_column,
        steps_column,
        success_column,
    )
)

print("\nRebuilt metrics:")
print(rebuilt)

print("Shape:", rebuilt.shape)