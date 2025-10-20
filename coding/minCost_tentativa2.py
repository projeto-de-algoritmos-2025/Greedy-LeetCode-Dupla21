import math


class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        total_cost = 0
        stack = [math.inf]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                total_cost += min(stack[-1], a) * mid
            stack.append(a)
        while len(stack) > 2:
            right = stack.pop()
            left = stack.pop()

            total_cost += left * right
            stack.append(left)
        return total_cost

if __name__ == "__main__":
    arr = [4, 11]
    r = Solution()
    print(r.mctFromLeafValues(arr))