class Solution:
    def threeSum(self, nums):
        nums.sort()  # Step 1: sort the array
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers
            left = i + 1
            right = n - 1
            target = -nums[i]  # we need nums[left] + nums[right] == target

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1  # need a bigger sum
                else:
                    right -= 1  # need a smaller sum

        return result