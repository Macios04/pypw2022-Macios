def fib(n):
    cache = {
        0: 0,
        1: 1,
    }
    def _fib(n):
        if n not in cache:
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]
    
    return _fib(n)

if __name__ == "__main__":
    print(fib(34))
