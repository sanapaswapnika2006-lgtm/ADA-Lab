
from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Accept input from the user
nums = list(map(int, input("Enter integers separated by spaces: ").split()))

print("Length of LIS:", lengthOfLIS(nums))
