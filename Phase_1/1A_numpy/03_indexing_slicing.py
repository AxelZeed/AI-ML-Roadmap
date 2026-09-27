import numpy as np

rewards = np.array([10, 20, -5, 30, 15])

print("--- 1D Indexing ---")
print("Array:", rewards)

print("First element:", rewards[0])
print("Second element:", rewards[1])
print("Last element:", rewards[-1])
print("Second-last element:", rewards[-2])

print("\n--- 1D Slicing ---")

print("First three:")
print(rewards[0:3])

print("From index 2 onward:")
print(rewards[2:])

print("Everything before index 4:")
print(rewards[:4])

print("Every second element:")
print(rewards[::2])

print("Reverse array:")
print(rewards[::-1])

episode_data = np.array([
    [10, 25, 1],
    [20, 18, 1],
    [-5, 100, 0],
    [35, 15, 1],
])

print("\n--- 2D Indexing ---")
print(episode_data)

print("\nFirst row:")
print(episode_data[0])

print("\nThird row:")
print(episode_data[2])

print("\nFirst row, second column:")
print(episode_data[0, 1])

print("\nThird row, third column:")
print(episode_data[2, 2])

print("\n--- Selecting Columns ---")

rewards_column = episode_data[:, 0]
steps_column = episode_data[:, 1]
success_column = episode_data[:, 2]

print("Rewards:")
print(rewards_column)

print("Steps:")
print(steps_column)

print("Success:")
print(success_column)

print("\n--- Row Slicing ---")

print("First two rows:")
print(episode_data[0:2])

print("\nRows 1 to 3:")
print(episode_data[1:4])

print("\n--- 2D Slicing ---")

subset = episode_data[0:3, 0:2]

print(subset)


print("\n--- Boolean Indexing ---")

rewards = np.array([10, 20, -5, 30, 15])

positive_mask = rewards > 0

print("Rewards:")
print(rewards)

print("\nMask:")
print(positive_mask)

print("\nPositive rewards:")
print(rewards[positive_mask])

print("\n--- Filter Successful Episodes ---")

successful_episodes = episode_data[episode_data[:, 2] == 1]

print(successful_episodes)

print("\n--- Multiple Conditions ---")

fast_success = episode_data[
    (episode_data[:, 2] == 1) &
    (episode_data[:, 1] < 20)
]

print(fast_success)

print("\n--- Fancy Indexing ---")

selected_rewards = rewards[[0, 2, 4]]

print(selected_rewards)

selected_rows = episode_data[[0, 3]]

print("\nSelected rows:")
print(selected_rows)


print("\n--- Slice View Behavior ---")

original = np.array([10, 20, 30, 40, 50])

slice_view = original[1:4]

print("Original:")
print(original)

print("Slice:")
print(slice_view)

slice_view[0] = 999

print("\nAfter changing slice:")
print("Original:")
print(original)

print("Slice:")
print(slice_view)

print("\n--- RL Telemetry Exercise ---")

telemetry = np.array([
    [1, 80, 30, 1],
    [2, 95, 20, 1],
    [3, -10, 100, 0],
    [4, 70, 40, 1],
    [5, 85, 25, 1],
], dtype=np.float32)

print("Telemetry:")
print(telemetry)

rewards = telemetry[:, 1]
steps = telemetry[:, 2]
success = telemetry[:, 3]

print("\nRewards:")
print(rewards)

print("\nSuccessful episodes:")
print(telemetry[success == 1])

print("\nEpisodes with reward >= 80:")
print(telemetry[rewards >= 80])

print("\nSuccessful episodes with <= 30 steps:")
efficient_successes = telemetry[
    (success == 1) &
    (steps <= 30)
]

print(efficient_successes)




