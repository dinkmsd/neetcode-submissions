class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles) # 25
        total = sum(piles) # 62
        if total <= h:
            return 1
        
        if len(piles) > h:
            return 0
        
        l, r = 2, max_k
        res = max_k
        while l < r:# 2...3
            avg = int((l + r)/2) # 2
            count = 0
            for pile in piles:
                count += math.ceil(pile/avg)
            if count > h:
                if l == avg:
                    break
                l = avg
            else:
                if r == avg:
                    break
                r = avg # 2
                res = r # 2
        
        return res