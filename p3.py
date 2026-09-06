from typing import List, Tuple

class solution:

    def findkthlargest(self, nums: List[int], k: int) -> int:
        # Sort the array in descending order
        nums.sort(reverse=True)

        # Since indexing starts from 0,
        # kth largest element is at index k-1
        return nums[k - 1]

        # Time Complexity: O(n log n)
        # Space Complexity: O(1) auxiliary space

    def findMinMax(self, nums: List[int]) -> Tuple[int, int]:
        # Start with the first element as minimum and maximum
        min_value = nums[0]
        max_value = nums[0]

        # Check every element in the array
        for num in nums:
            if num < min_value:
                min_value = num

            if num > max_value:
                max_value = num

        # Return minimum and maximum as a tuple
        return min_value, max_value

        # Time Complexity: O(n)
        # Space Complexity: O(1)


# -------- Testing the functions --------

nums = [7, 2, 9, 4, 1, 6]
k = 3

obj = solution()

print("Kth largest element:", obj.findkthlargest(nums, k))
print("Minimum and Maximum:", obj.findMinMax(nums))