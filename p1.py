# Implement search(nums: List[int], target: int) -> int and myPow(x: float, n: int) -float functions taking an integer array/target and base/exponent pairs, returning index and computed value respectively.
from typing import List


# Binary Search
def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Power function using Binary Exponentiation
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0

    while n > 0:
        if n % 2 == 1:
            result = result * x

        x = x * x
        n = n // 2

    return result


# Main program
print("----- Binary Search -----")

nums = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target element: "))

index = search(nums, target)

if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found")


print("\n----- Power Function -----")

x = float(input("Enter base (x): "))
n = int(input("Enter exponent (n): "))

answer = myPow(x, n)

print("Result:", answer)