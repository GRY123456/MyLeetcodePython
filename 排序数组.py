from typing import List


# 快速排序

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.q_sort(nums, 0, len(nums)-1)

    def q_sort(self, nums, left, right):
        if left < right:
            pivot = self.Partition(nums, left, right)
            self.q_sort(nums, left, pivot-1)
            self.q_sort(nums, pivot+1, right)
        return nums

    def Partition(self, nums, left, right):
        pivotkey = nums[left]

        while left < right:
            while left < right and nums[right] >= pivotkey:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivotkey:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivotkey
        return left


if __name__ == "__main__":
    solution = Solution()
    ans = solution.sortArray([5, 1, 1, 2, 0, 0])
    print(ans)
