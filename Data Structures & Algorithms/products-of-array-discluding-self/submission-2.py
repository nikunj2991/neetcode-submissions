class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0

        zeroCount = 0

        product = 1

        for num in nums:
            if num != 0:
                product *= num
            else:
                zeroCount += 1


        res = []

        if zeroCount > 1:
            return [0] * len(nums)

        for num in nums:
            if num == 0:
                res.append((product))
            else:
                val = product/num if not zeroCount else 0
                res.append(int(val))
        
        return res