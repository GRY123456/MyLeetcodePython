import heapq
from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        dict_count = dict(count)
        ans = heapq.nlargest(k, dict_count.items(), key=lambda s: s[1])
        ans_list = []
        for num in ans:
            ans_list.append(num[0])
        return ans_list


if __name__ == "__main__":
    solution = Solution()
    ans = solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3, 4, 4, 4, 4], k=3)
    print(ans)
