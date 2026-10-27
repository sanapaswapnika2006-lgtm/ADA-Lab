from typing import List

def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort by value-to-weight ratio in descending order
    items.sort(reverse=True)

    total_value = 0.0

    for ratio, weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            capacity = 0

    return total_value


# Example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print(fractional_knapsack(weights, values, capacity))

from typing import List
from dataclasses import dataclass

@dataclass
class Job:
    id: int
    deadline: int
    profit: int


def job_scheduling(jobs: List[Job]) -> List[int]:
    # Sort jobs by profit in descending order
    jobs = sorted(jobs, key=lambda job: job.profit, reverse=True)

    max_deadline = max((job.deadline for job in jobs), default=0)
    slots = [None] * (max_deadline + 1)

    for job in jobs:
        # Find the latest free slot before the deadline
        for t in range(min(job.deadline, max_deadline), 0, -1):
            if slots[t] is None:
                slots[t] = job.id
                break

    # Return the scheduled job IDs in execution order
    return [job_id for job_id in slots[1:] if job_id is not None]


# Example
jobs = [
    Job(1, 2, 100),
    Job(2, 1, 19),
    Job(3, 2, 27),
    Job(4, 1, 25),
    Job(5, 3, 15)
]

sequence = job_scheduling(jobs)
print(sequence)