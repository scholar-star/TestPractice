#iteration
def factorial_iterate(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#recursive
def factorial_recursive(n):
    if(n<=1):
        return 1
    return n*factorial_recursive(n-1)

print("iteration :", factorial_iterate(5))
print("recursive :", factorial_recursive(5))
