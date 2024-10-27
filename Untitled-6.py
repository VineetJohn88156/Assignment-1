def cube_sum(n):
    return sum(i**3 for i in range(1, n + 1))

# Example usage
n = 3
print(f"Cube sum of first {n} natural numbers is {cube_sum(n)}")