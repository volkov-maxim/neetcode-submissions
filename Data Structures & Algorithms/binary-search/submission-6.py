import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_right(nums, target)
        return index-1 if nums[index-1] == target else -1