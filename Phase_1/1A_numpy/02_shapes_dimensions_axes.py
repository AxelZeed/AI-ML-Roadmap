import numpy as np

rewards = np.array([10, 20, 30, 40, 50])

print("--- 1D Array ---")
print(rewards)

print("shape:", rewards.shape)
print("ndim:", rewards.ndim)
print("size:", rewards.size)

episode_data = np.array([
    [10, 25, 1],
    [20, 18, 1],
    [-5, 100, 0],
    [35, 15, 1],
])

print("\n--- 2D Array ---")
print(episode_data)

print("shape:", episode_data.shape)
print("ndim:", episode_data.ndim)
print("size:", episode_data.size)

batch_data = np.array([
    [
        [1, 2],
        [3, 4],
    ],
    [
        [5, 6],
        [7, 8],
    ],
])

print("\n--- 3D Array ---")
print(batch_data)

print("shape:", batch_data.shape)
print("ndim:", batch_data.ndim)
print("size:", batch_data.size)


scores = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

print("\n--- Axis Example ---")

print(scores)
print("shape:", scores.shape)

print("\nSum everything:")
print(scores.sum())

print("\nSum axis=0:")
print(scores.sum(axis=0))

print("\nSum axis=1:")
print(scores.sum(axis=1))

print("\n--- Mean Across Axes ---")

print("Overall mean:")
print(scores.mean())

print("\nMean axis=0:")
print(scores.mean(axis=0))

print("\nMean axis=1:")
print(scores.mean(axis=1))

print("\n--- RL Experiment Example ---")

experiment_results = np.array([
    [80, 30, 1],
    [95, 20, 1],
    [-10, 100, 0],
    [70, 40, 1],
    [85, 25, 1],
], dtype=np.float32)

print("Data:")
print(experiment_results)

print("\nShape:")
print(experiment_results.shape)

print("\nDimensions:")
print(experiment_results.ndim)

print("\nAverage of each column:")
print(experiment_results.mean(axis=0))

print("\nAverage of each row:")
print(experiment_results.mean(axis=1))











