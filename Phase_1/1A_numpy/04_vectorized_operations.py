import numpy as np
import time

rewards = np.array([10, 20, -5, 30, 15], dtype=np.float32)

print("--- Basic Vectorized Arithmetic ---")
print("Original rewards:")
print(rewards)

print("\nAdd 10:")
print(rewards + 10)

print("\nSubtract 5:")
print(rewards - 5)

print("\nMultiply by 2:")
print(rewards * 2)

print("\nDivide by 2:")
print(rewards / 2)


print("\n--- Array-to-Array Operations ---")

actual_rewards = np.array([10, 20, 30, 40], dtype=np.float32)
expected_rewards = np.array([12, 18, 35, 38], dtype=np.float32)

print("Actual:")
print(actual_rewards)

print("Expected:")
print(expected_rewards)

print("\nDifference:")
print(actual_rewards - expected_rewards)

print("\n--- Element-Wise Multiplication ---")

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a * b)

print("\n--- Vectorized Comparisons ---")

rewards = np.array([10, 20, -5, 30, 15])

print("Rewards:")
print(rewards)

print("\nRewards > 10:")
print(rewards > 10)

print("\nRewards <= 15:")
print(rewards <= 15)

print("\nRewards == 20:")
print(rewards == 20)

print("\n--- Combined Conditions ---")

good_rewards = (rewards >= 10) & (rewards <= 20)

print(good_rewards)
print(rewards[good_rewards])

negative_mask = rewards < 0

print("\nNot negative:")
print(rewards[~negative_mask])

print("\n--- Replace Values ---")

clean_rewards = rewards.copy()

clean_rewards[clean_rewards < 0] = 0

print("Original:")
print(rewards)

print("Cleaned:")
print(clean_rewards)

print("\n--- np.where() ---")

adjusted_rewards = np.where(
    rewards < 0,
    0,
    rewards,
)

print(adjusted_rewards)

print("\n--- Mathematical Functions ---")

values = np.array([1, 4, 9, 16], dtype=np.float32)

print("Square root:")
print(np.sqrt(values))

print("\nSquared:")
print(np.square(values))

print("\nExponential:")
print(np.exp(np.array([1, 2, 3], dtype=np.float32)))

print("\nAbsolute value:")
print(np.abs(np.array([-5, -2, 3, 8])))

print("\n--- Clipping ---")

raw_rewards = np.array([-100, -10, 0, 25, 50, 200])

clipped_rewards = np.clip(raw_rewards, -20, 100)

print("Raw:")
print(raw_rewards)

print("Clipped:")
print(clipped_rewards)


print("\n--- Python Loop vs NumPy ---")

python_values = [1, 2, 3, 4, 5]

python_result = []

for value in python_values:
    python_result.append(value * 2 + 5)

print("Python result:")
print(python_result)

numpy_values = np.array([1, 2, 3, 4, 5])

numpy_result = numpy_values * 2 + 5

print("NumPy result:")
print(numpy_result)



print("\n--- Performance Comparison ---")

size = 1_000

python_values = list(range(size))
numpy_values = np.arange(size)

start = time.perf_counter()

python_result = []

for value in python_values:
    python_result.append(value * 2)

python_time = time.perf_counter() - start


start = time.perf_counter()

numpy_result = numpy_values * 2

numpy_time = time.perf_counter() - start


print(f"Python loop: {python_time:.6f} seconds")
print(f"NumPy:       {numpy_time:.6f} seconds")

print("\n--- RL Telemetry Vectorization ---")

telemetry = np.array([
    [1, 80, 30, 1],
    [2, 95, 20, 1],
    [3, -10, 100, 0],
    [4, 70, 40, 1],
    [5, 85, 25, 1],
], dtype=np.float32)

rewards = telemetry[:, 1]
steps = telemetry[:, 2]
success = telemetry[:, 3]

print("Rewards:")
print(rewards)

print("\nReward per step:")
reward_per_step = rewards / steps
print(reward_per_step)


print("\n--- Simple Scaling Preview ---")

max_reward = rewards.max()

scaled_rewards = rewards / max_reward

print("Original rewards:")
print(rewards)

print("Scaled rewards:")
print(scaled_rewards)

print("\n--- Derived Telemetry Features ---")

efficient = (success == 1) & (steps <= 30)
high_reward = rewards >= 80

print("Efficient:")
print(efficient)

print("High reward:")
print(high_reward)

print("\nEfficient AND high reward:")
elite_episodes = telemetry[efficient & high_reward]

print(elite_episodes)

