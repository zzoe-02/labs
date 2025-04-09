import time

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)
@memoize
def memo_fibo(n):
    if n <= 1:
        return n
    else:
        return memo_fibo(n - 1) + memo_fibo(n - 2)

# testing
if __name__ == "__main__":
    n = 35
    start_ = time.time()
    result_ = recur_fibo(n)
    end_ = time.time()
    print(f"fibo with recursion (n={n}): {result_}")
    print(f"time with recursion: {end_ - start_:.5f} s")
    start_ = time.time()
    result_memo = memo_fibo(n)
    end_ = time.time()
    print(f"fibo with memoization (n={n}): {result_memo}")
    print(f"time with memoization: {end_ - start_:.5f} s")
