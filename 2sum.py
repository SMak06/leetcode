class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        our_map = dict()
        for i, elem in enumerate(nums):
            compliment = target - elem
            if compliment in our_map:
                return [our_map[compliment],i]
            our_map[elem] = i
        return []
       
        