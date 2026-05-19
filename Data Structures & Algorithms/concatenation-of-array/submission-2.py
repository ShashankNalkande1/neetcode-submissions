class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        data = []
        for i in range(2):
            for x in nums:
                data.append(x)
        return data