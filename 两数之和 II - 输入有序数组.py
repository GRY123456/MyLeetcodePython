from typing import List


# 方法：双指针
#
# 我们使用两个指针，初始分别位于第一个元素和最后一个元素位置，比较这两个元素之和与目标值的大小。
# 如果和等于目标值，我们发现了这个唯一解。如果比目标值小，我们将较小元素指针增加一。
# 如果比目标值大，我们将较大指针减小一。移动指针后重复上述比较知道找到答案。
#
# 假设 [... , a, b, c, ... , d, e, f, ...]是已经升序排列的输入数组，并且元素 b,e 是唯一解。
# 因为我们从左到右移动较小指针，从右到左移动较大指针，总有某个时刻存在一个指针移动到 b 或 e 的位置。
# 不妨假设小指针县移动到了元素 b ，这是两个元素的和一定比目标值大，根据我们的算法，我们会向左移动较大指针直至获得结果。
#
# 时间复杂度：O(n)。每个元素最多被访问一次，共有 n个元素。
# 空间复杂度：O(1)。只是用了两个指针。
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        letf_link = 0
        right_link = len(numbers) - 1
        while numbers[letf_link] + numbers[right_link] != target:
            if numbers[letf_link] + numbers[right_link] > target:
                right_link -= 1
            else:
                letf_link += 1
        return [letf_link, right_link]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.twoSum(numbers=[2, 7, 11, 15], target=9)
    print(ans)
