from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        #array de "remendos" (patches) que precisamos adicionar
        
        # adições começa em 0
        patches = 0
        
        # numero que queremos alcançar, inicia com o 1
        alcance = 1
        
        # i pra percorrer o vetor
        i = 0
        
        
        while alcance <= n:
            #se o número atual em nums for menor ou igual ao alcance
            if i < len(nums) and nums[i] <= alcance:
                # alcançar mais numeros somando o valor atual presente em nums
                alcance += nums[i]
                i += 1
            # o numero já é maior que o alcance
            else:
                # como tem um "buraco" no remendo, soma o alcance a ele mesmo
                alcance += alcance
                # soma 1 no contador de remendos
                patches += 1
                
        return patches