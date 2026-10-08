class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            st1, st2 = stones.pop(), stones.pop()
            if st1 != st2:
                stones.append(st1 - st2)

        return stones.pop() if len(stones) == 1 else 0
