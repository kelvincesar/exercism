lookup_table = {0: 1}
def factorial(n):
    if n in lookup_table:
        return lookup_table[n]
    
    x = factorial(n - 1) * n
    lookup_table[n] = x
    return x


print(factorial(3))