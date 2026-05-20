class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:

        n = len(nums)
        total_sum = sum(nums)

        dp = [set() for _ in range(n + 1)]

        dp[0].add(0)

        for num in nums:

            for size in range(n - 1, -1, -1):

                for prev_sum in dp[size]:

                    dp[size + 1].add(prev_sum + num)

        for size in range(1, n):

            if (total_sum * size) % n == 0:

                target_sum = (total_sum * size) // n

                if target_sum in dp[size]:
                    return True

        return False