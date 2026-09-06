#Design a Sort class containing merge_sort(arr: List[int]) -> List[int] and quick_sort(arr:List[int]) -> List[int] methods that accept an unsorted integer array and return the sorted array

from typing import List

class Sort:

    # Merge two sorted lists
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    # Merge Sort
    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    # Quick Sort
    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        # Choose last element as pivot
        pivot = arr[-1]
        left = []
        right = []

        # Divide elements based on pivot
        for x in arr[:-1]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)


# Testing
obj = Sort()

arr = [8, 3, 5, 1, 7, 2]

print("Merge Sort:", obj.merge_sort(arr))
print("Quick Sort:", obj.quick_sort(arr))


# Time Complexity:
# Merge Sort:
# Best Case    : O(n log n)
# Average Case : O(n log n)
# Worst Case   : O(n log n)
#
# Quick Sort:
# Best Case    : O(n log n)
# Average Case : O(n log n)
# Worst Case   : O(n^2)
#
# Space Complexity:
# Merge Sort : O(n)
# Quick Sort : O(n)

