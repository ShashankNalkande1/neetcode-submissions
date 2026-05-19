class Solution:

    def longestConsecutive(self, nums):

        # edge case
        if len(nums) == 0:
            return 0

        # convert list to set
        num_set = set(nums)

        longest = 0

        for num in num_set:

            # check start of sequence
            if (num - 1) not in num_set:

                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set:

                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest