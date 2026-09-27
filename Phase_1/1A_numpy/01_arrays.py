import numpy as np


rewards = np.array([10, 20, -5, 30, 15])

print("Rewards:")
print(rewards)

print("\nType:")
print(type(rewards))

print("\nData type:")
print(rewards.dtype)

print("\nShape:")
print(rewards.shape)

print("\nDimensions:")
print(rewards.ndim)

print("\nNumber of elements:")
print(rewards.size)

print("\n--- Python List vs NumPy Array ---")

python_rewards = [10, 20, -5, 30, 15]
numpy_rewards = np.array([10, 20, -5, 30, 15])

print("\nPython list:")
print(python_rewards)

print("\nNumPy array:")
print(numpy_rewards)

print("\nMultiply by 2:")

print("Python list:")
print(python_rewards * 2)

print("NumPy array:")
print(numpy_rewards * 2)

print("\nAdd 10:")
print(numpy_rewards + 10)

print("\nSubtract 5:")
print(numpy_rewards - 5)

print("\nDivide by 2:")
print(numpy_rewards / 2)

float_rewards = np.array([10.5, 20.2, -5.7, 30.1, 15.8])

print("\n--- Float Array ---")
print(float_rewards)
print("dtype:", float_rewards.dtype)

small_rewards = np.array(
    [10.5, 20.2, -5.7, 30.1, 15.8],
    dtype=np.float32,
)

print("\n--- Explicit dtype ---")
print(small_rewards)
print("dtype:", small_rewards.dtype)

print("\n--- Mixed Data Types ---")

mixed_numbers = np.array([10, 20.5, 30])

print(mixed_numbers)
print("dtype:", mixed_numbers.dtype)

print("\n--- Type Conversion ---")

original = np.array([10.7, 20.2, 30.9])

converted_to_int = original.astype(np.int32)
converted_to_float = converted_to_int.astype(np.float32)

print("Original:")
print(original)
print("dtype:", original.dtype)

print("\nConverted to int:")
print(converted_to_int)
print("dtype:", converted_to_int.dtype)

print("\nConverted back to float:")
print(converted_to_float)
print("dtype:", converted_to_float.dtype)

print("\n--- zeros() ---")

zero_array = np.zeros(100)

print(zero_array)
print("dtype:", zero_array.dtype)

print("\n--- ones() ---")

one_array = np.ones(5,dtype=np.int32)

print(one_array)

print("\n--- full() ---")

default_rewards = np.full(5, -1.0)

print(default_rewards)

print("\n--- arange() ---")

episodes = np.arange(1, 11)

print(episodes)

training_steps = np.arange(0, 10001, 1000)

print(training_steps)

print("\n--- linspace() ---")

learning_rates = np.linspace(0.0, 1.0, 5)

print(learning_rates)

print("\n--- Simple Telemetry Array ---")

episode_rewards = np.array(
    [15.2, 20.1, -5.0, 35.7, 42.3],
    dtype=np.float32,
)

episode_numbers = np.arange(1, len(episode_rewards) + 1)

print("Episodes:")
print(episode_numbers)

print("Rewards:")
print(episode_rewards)

print("Rewards dtype:")
print(episode_rewards.dtype)