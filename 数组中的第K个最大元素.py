import heapq
from typing import List


# 大顶堆
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        big_heap = []
        for num in nums:
            if len(big_heap) != k:
                big_heap.append(num)
                now_index = len(big_heap) - 1
                father_index = int((now_index-1)/2)
                while big_heap[father_index] > big_heap[now_index]:
                    tmp = big_heap[father_index]
                    big_heap[father_index] = big_heap[now_index]
                    big_heap[now_index] = tmp
                    now_index = father_index
                    father_index = int((now_index-1)/2)
            else:
                if num > big_heap[0]:
                    big_heap[0] = num
                    more_small = num
                    more_small_flag = 0
                    now_index = 0
                    while True:
                        if now_index * 2 + 1 < k:
                            if big_heap[now_index * 2 + 1] < more_small:
                                more_small = big_heap[now_index * 2 + 1]
                                more_small_flag = 1
                        if now_index * 2 + 2 < k:
                            if big_heap[now_index * 2 + 2] < more_small:
                                more_small = big_heap[now_index * 2 + 2]
                                more_small_flag = 2
                        if more_small_flag == 1:
                            tmp = big_heap[now_index]
                            big_heap[now_index] = more_small
                            big_heap[now_index * 2 + 1] = tmp
                            now_index = now_index * 2 + 1
                            more_small_flag = 0
                            more_small = tmp
                        elif more_small_flag == 2:
                            tmp = big_heap[now_index]
                            big_heap[now_index] = more_small
                            big_heap[now_index * 2 + 2] = tmp
                            now_index = now_index * 2 + 2
                            more_small_flag = 0
                            more_small = tmp
                        else:
                            break
        return big_heap[0]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)
    print(ans)
