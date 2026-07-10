class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        res = []

        for i, num in enumerate(nums):
            index = target - num
            map[index] = i

        for j in range(len(nums)-1, -1, -1):
            if nums[j] in map and map[nums[j]] != j:
                res.append(map[nums[j]])
                res.append(j)
                break
        
        return sorted(res);

        