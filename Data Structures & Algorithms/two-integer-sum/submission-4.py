class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        res = []
        for i, num in enumerate(nums):
            diff = target - num
            if num not in map:
                map[diff] = i
                print(map)
            else:
                res.append(map[num])
                res.append(i)
                break

        return res

        