
class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        n = len(arr)
        pilha = []
        i = 0
        sol = 0
        # [0,1, 2,3, 4,5, 6,7]
        while i < n:
            if i < n-1:
                pilha.append(arr[i]*arr[i+1])
            i = i + 2

        if len(arr)%2 != 0:
            pilha.append(arr[-1]*arr[-2])

        while len(pilha) > 0:
            sol += pilha.pop()

        return sol

if __name__ == "__main__":
    arr = [4,11]
    r = Solution()
    print(r.mctFromLeafValues(arr))