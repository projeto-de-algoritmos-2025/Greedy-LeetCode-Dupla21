from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        patches = 0
        
        alcance = 1
        
        for num in nums:

            while num > alcance and alcance <= n:
                # adicionar patch e alcancar mais
                alcance += alcance
                patches += 1
            
            # depois dos buracos, somo ao atual
            alcance += num
            
            # verifica se ja chegou em n
            if alcance > n:
                break
            
        
        return patches