class Solution:
    def asteroidCollision(self, asteroids):
        result = []

        for asteroid in asteroids:
            while result and asteroid < 0 and result[-1] > 0:
                if result[-1] < -asteroid:
                    result.pop()
                elif result[-1] == -asteroid:
                    result.pop()
                    asteroid = 0
                    break
                else:
                    asteroid = 0
                    break

            if asteroid != 0:
                result.append(asteroid)

        return result