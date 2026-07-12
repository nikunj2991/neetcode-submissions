class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        res = max_k

        if (len(piles) == h):
            return max_k
        
        while min_k <= max_k:
            k = (min_k + max_k) // 2
            
            hours = 0
            for pile in piles:
                # ceil of pile/k
                hours += -(-pile // k)

            if hours > h:
                min_k = k + 1
            else:
                res = k
                max_k = k - 1

        return res

