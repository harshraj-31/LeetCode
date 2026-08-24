class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                
                # Check left side
                if i == 0 or flowerbed[i - 1] == 0:
                    
                    # Check right side
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1

        return count >= n