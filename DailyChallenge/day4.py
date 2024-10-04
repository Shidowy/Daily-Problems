# Problem: Sum of Unique Elements

# Given an array of integers, return the sum of all the unique elements (elements that appear exactly once).

# Example:

class UniqueElementsSum:
    def __init__(self, nums):
        self.nums = nums

    def sum_of_unique(self):
        k = 0
        n = len(self.nums)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if self.nums[j] > self.nums[j+1]:  
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
                    swapped = True
            if not swapped:  
                break
        while i < len(self.nums) - 1:
            if self.nums[i] == self.nums[i + 1]:
                del self.nums[i + 1]
            else:
                i += 1
        for j in range(len(self.nums)):
            k += self.nums[j]
        return k

    
test = UniqueElementsSum([1, 2, 3, 2])
print(test.sum_of_unique())  

