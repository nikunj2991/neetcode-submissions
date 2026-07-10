class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        val_count = count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
            else:
                val_count += 1

        for i in range(len(nums) - val_count, len(nums)):
            nums[i] = "_"

        return count
                 