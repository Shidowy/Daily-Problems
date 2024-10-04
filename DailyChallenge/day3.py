# Problem: Kth Largest Element in an Array
# Description: Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in sorted order, not the kth distinct element.

# You should aim to solve this in better than O(n log n) time complexity (so no full sorting of the array).

# Example:
# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
# Output: 4
# Explanation: The sorted array is [6, 5, 5, 4, 3, 3, 2, 2, 1]. The 4th largest element is 4.
# Constraints:
# You must solve this in O(n) average time complexity using algorithms like Quickselect or a heap-based approach.


#2^N solution
class KthLargest:
    def __init__(self, nums, k):
        """Initialize with the array of numbers and the value of k."""
        self.nums = nums
        self.k = k

    def find_kth_largest(self):
        """Method to find the kth largest element."""
        n = len(self.nums)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if self.nums[j] > self.nums[j+1]:  
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
                    swapped = True
            if not swapped:  
                break
        return self.nums[self.k-1]   


nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2

kth_largest = KthLargest(nums1, k1)
result = kth_largest.find_kth_largest()
print(f"Kth largest element: {result}")
