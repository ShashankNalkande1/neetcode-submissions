class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:

        n = len(nums)
        total_sum = sum(nums)

        # dp[k] = set of sums possible using k elements
        dp = [set() for _ in range(n + 1)]

        # 0 elements se sum 0 possible hai
        dp[0].add(0)

        # har number uthao
        for num in nums:

            # reverse me loop warna same number multiple baar use ho jayega
            for size in range(n - 1, -1, -1):

                # jo sums already possible hain
                for prev_sum in dp[size]:

                    # new size me new sum add karo
                    dp[size + 1].add(prev_sum + num)

        # ab check karenge
        # kya koi subset exist karta hai
        # jiska average same ho

        for size in range(1, n):

            # required sum hona chahiye integer
            if (total_sum * size) % n == 0:

                target_sum = (total_sum * size) // n

                # agar possible hai
                if target_sum in dp[size]:
                    return True

        return False