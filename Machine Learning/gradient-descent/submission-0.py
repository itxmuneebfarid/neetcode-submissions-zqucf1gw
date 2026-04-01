class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for _ in range(iterations):
            grad = 2 * x           
            x = x - learning_rate * grad 
        return round(x, 5)
sol = Solution()
print(sol.get_minimizer(iterations=100, learning_rate=0.1, init=10))
