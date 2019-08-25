from typing import List


class Solution:
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

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child_len = len(g)
        g = self.q_sort(g, 0, child_len-1)
        s = self.q_sort(s, 0, len(s)-1)
        ans_sum = 0
        child_left = 0
        for biscuit in s:
            if biscuit >= g[child_left]:
                ans_sum += 1
                child_left += 1
            if child_left == child_len:
                break
        return ans_sum


if __name__ == "__main__":
    solution = Solution()
    ans = solution.findContentChildren([1, 2], [1, 2, 3])
    print(ans)

