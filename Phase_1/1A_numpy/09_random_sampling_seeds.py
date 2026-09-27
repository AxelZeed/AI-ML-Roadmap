import numpy as np

print("--- Random Generator ---")

rng = np.random.default_rng()

print(rng)


print("\n--- Random Integers ---")

random_number = rng.integers(1, 11)

print("Random integer:")
print(random_number)

random_numbers = rng.integers(
    low=1,
    high=11,
    size=5,
)

print("\nFive random integers:")
print(random_numbers)


print("\n--- Random Floats ---")

random_floats = rng.random(5)

print(random_floats)

print("\n--- Random Array Shapes ---")

random_matrix = rng.random((3, 4))

print(random_matrix)
print("Shape:", random_matrix.shape)


print("\n--- Random Choice ---")

actions = np.array([
    "UP",
    "DOWN",
    "LEFT",
    "RIGHT",
])

action = rng.choice(actions)

print("Chosen action:")
print(action)

random_actions = rng.choice(
    actions,
    size=10,
)

print("\nTen random actions:")
print(random_actions)



