class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        result = [0] * arr_len
        right_max = -1

        for i in range(arr_len - 1, -1, -1):
            result[i] = right_max
            right_max = max(right_max, arr[i])
        
        return result
