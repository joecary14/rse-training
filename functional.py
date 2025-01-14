def factorial_recursive(n):
    if n<0:
        raise ValueError('n must be non-negative')
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
    
def factorial_procedural(n):
    if n<0:
        raise ValueError('n must be non-negative')
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

