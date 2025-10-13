from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        doce = 0
        for i in range(len(ratings)):
            # esq
            if ratings[i] < ratings[i+1]:
                doce += 1
            # dir
            else:
                doce += 2
        return doce