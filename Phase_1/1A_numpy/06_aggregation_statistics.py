import numpy as np

rewards = np.array([80, 95, -10, 70, 85], dtype=np.float32)

print("--- Basic Aggregation ---")
print("Rewards:")
print(rewards)

print("\nSum:")
print(rewards.sum())

print("\nMean:")
print(rewards.mean())

print("\nMinimum:")
print(rewards.min())

print("\nMaximum:")
print(rewards.max())

print("\n--- Median ---")

print("Mean:")
print(np.mean(rewards))

print("Median:")
print(np.median(rewards))


example = np.array([10, 11, 12, 13, 1000])

print("\nOutlier example:")
print(example)

print("Mean:")
print(np.mean(example))

print("Median:")
print(np.median(example))


print("\n--- Standard Deviation ---")

print("Mean reward:")
print(np.mean(rewards))

print("Standard deviation:")
print(np.std(rewards))


stable = np.array([80, 81, 79, 80, 80], dtype=np.float32)

unstable = np.array([20, 140, 5, 170, 65], dtype=np.float32)

print("\nStable results:")
print(stable)
print("Mean:", stable.mean())
print("Std:", stable.std())

print("\nUnstable results:")
print(unstable)
print("Mean:", unstable.mean())
print("Std:", unstable.std())

print("\n--- Variance ---")

print("Variance:")
print(np.var(rewards))

print("Standard deviation:")
print(np.std(rewards))

variance = np.var(rewards)
std_from_variance = np.sqrt(variance)

print("\nStd from variance:")
print(std_from_variance)


print("\n--- Percentiles ---")

values = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("25th percentile:")
print(np.percentile(values, 25))

print("50th percentile:")
print(np.percentile(values, 50))

print("75th percentile:")
print(np.percentile(values, 75))

print("\n--- argmin() and argmax() ---")

rewards = np.array([80, 95, -10, 70, 85])

print("Rewards:")
print(rewards)

print("Maximum reward:")
print(rewards.max())

print("Index of maximum reward:")
print(rewards.argmax())

print("Minimum reward:")
print(rewards.min())

print("Index of minimum reward:")
print(rewards.argmin())

print("\n--- Aggregation Across Axes ---")

telemetry = np.array([
    [80, 30, 1],
    [95, 20, 1],
    [-10, 100, 0],
    [70, 40, 1],
    [85, 25, 1],
], dtype=np.float32)

print("Telemetry:")
print(telemetry)

print("\nColumn means:")
print(telemetry.mean(axis=0))

print("\nRow means:")
print(telemetry.mean(axis=1))

rewards = telemetry[:, 0]
steps = telemetry[:, 1]
success = telemetry[:, 2]

print("\n--- Named Feature Statistics ---")

print("Average reward:")
print(rewards.mean())

print("Median reward:")
print(np.median(rewards))

print("Reward std:")
print(rewards.std())

print("\nAverage steps:")
print(steps.mean())

print("Median steps:")
print(np.median(steps))

print("Step std:")
print(steps.std())

print("\nSuccess rate:")
print(success.mean())

print("\n--- Successful Episode Statistics ---")

successful_rewards = rewards[success == 1]
successful_steps = steps[success == 1]

print("Successful rewards:")
print(successful_rewards)

print("Average successful reward:")
print(successful_rewards.mean())

print("\nSuccessful steps:")
print(successful_steps)

print("Average successful steps:")
print(successful_steps.mean())


print("\n--- Counting Conditions ---")

success_mask = success == 1

print("Success mask:")
print(success_mask)

print("Number of successes:")
print(np.sum(success_mask))

print("Total episodes:")
print(success.size)

print("Success rate:")
print(np.mean(success_mask))

print("\n--- Failure Analysis ---")

failure_codes = np.array([
    0,
    0,
    2,
    1,
    0,
    2,
    0,
    1,
])

wall_failures = np.sum(failure_codes == 1)
trap_failures = np.sum(failure_codes == 2)

print("Wall failures:")
print(wall_failures)

print("Trap failures:")
print(trap_failures)

print("\n--- Unique Values ---")

unique_codes = np.unique(failure_codes)

print("Unique failure codes:")
print(unique_codes)


codes, counts = np.unique(
    failure_codes,
    return_counts=True,
)

print("\nCodes:")
print(codes)

print("Counts:")
print(counts)

print("\n--- Cumulative Operations ---")

episode_rewards = np.array([10, 20, -5, 30, 15])

print("Rewards:")
print(episode_rewards)

print("\nCumulative sum:")
print(np.cumsum(episode_rewards))


print("\n--- RL Experiment Summary ---")

telemetry = np.array([
    [1, 80, 30, 1],
    [2, 95, 20, 1],
    [3, -10, 100, 0],
    [4, 70, 40, 1],
    [5, 85, 25, 1],
    [6, 90, 22, 1],
    [7, 10, 100, 0],
    [8, 88, 24, 1],
], dtype=np.float32)

episode_ids = telemetry[:, 0]
rewards = telemetry[:, 1]
steps = telemetry[:, 2]
success = telemetry[:, 3]

print(telemetry)
print("Episodes:", len(telemetry))

print("\nReward statistics:")
print("Mean:", rewards.mean())
print("Median:", np.median(rewards))
print("Min:", rewards.min())
print("Max:", rewards.max())
print("Std:", rewards.std())

print("\nStep statistics:")
print("Mean:", steps.mean())
print("Median:", np.median(steps))
print("Min:", steps.min())
print("Max:", steps.max())

print("\nSuccess:")
print("Successes:", np.sum(success == 1))
print("Failures:", np.sum(success == 0))
print("Success rate:", success.mean())

best_index = rewards.argmax()
worst_index = rewards.argmin()

print("\nBest episode:")
print("Episode:", int(episode_ids[best_index]))
print("Reward:", rewards[best_index])

print("\nWorst episode:")
print("Episode:", int(episode_ids[worst_index]))
print("Reward:", rewards[worst_index])










