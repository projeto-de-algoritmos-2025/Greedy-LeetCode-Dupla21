from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        
        # verificar o vetor da esq pra dir 
        doces = [1] * n
        for i in range(1, n, 1):
            # vê se a nota verificada agora é maior que a anterior
            if ratings[i] > ratings[i-1]:
                # se sim,dá um doce a mais que o anterior
                doces[i] = doces[i-1] + 1
        
        # verificar o vetor da dir pra esq, começando no penúltimo
        for i in range(n - 2, -1, -1):
            # vê se a nota verificada agora é maior que a próxima
            if ratings[i] > ratings[i+1]:
                # max para garantir que a regra da esq nao seja quebrada e garanta também a regra da dir
                doces[i] = max(doces[i], doces[i+1] + 1)
        
        # soma dos doces
        return sum(doces)