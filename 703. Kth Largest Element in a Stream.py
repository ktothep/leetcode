class KthLargest:

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]
obj=KthLargest(3, [4, 5, 8, 2])
obj.add(3)