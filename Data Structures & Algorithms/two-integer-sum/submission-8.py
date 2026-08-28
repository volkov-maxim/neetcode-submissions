class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is not None and target is not None:
            nums_indexes = {}
            for idx, num in enumerate(nums):
                if num not in nums_indexes:
                    nums_indexes[num] = [idx]
                else:
                    nums_indexes[num].append(idx)

            for idx, num in enumerate(nums):
                if target - num in nums[idx+1:]:
                    if len(nums_indexes[target - num]) > 1:
                        return nums_indexes[target - num]
                    return [idx, *nums_indexes[target - num]]
        else:
            return []