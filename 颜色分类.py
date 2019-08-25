from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr] = nums[p0]
                nums[p0] = 0
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr] = nums[p2]
                nums[p2] = 2
                p2 -= 1
            else:
                curr += 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    solution = Solution()
    solution.sortColors(nums)
    print(nums)
