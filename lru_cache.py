'''
We'll be building an lru cache using functools with some demo examples. (lru stands for least recently used, and it's a caching mechanism that discards the least recently used items first when the cache reaches its maximum size.)
'''

from functools import lru_cache
from time import time
from functools import wraps

def measure(func):
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper


#first basic example from the documentation
# constraint -> it only works with hashable types, so we can't use it with lists or dictionaries as arguments and the first runs the function each time we call it with a new argument, but if we call it with 2nd function it will return the cached result instead of recomputing it.
def count_vowels(sentence: str) -> int:
    """Counts the number of vowels in a given sentence."""
    print(f"Counting vowels in: '{sentence}'")
    return sum(1 for char in sentence if char.lower() in 'aeiou')

print(count_vowels("Hello World"))  # This will compute and print the count
print(count_vowels("Hello World"))  # This will compute again and print the count

# Apply LRU cache with a maximum size of 128
@lru_cache(maxsize=128)
def count_vowels_cached(sentence: str) -> int:
    """Counts the number of vowels in a given sentence (with LRU caching)."""
    print(f"Counting vowels in: '{sentence}'")
    return sum(1 for char in sentence if char.lower() in 'aeiou')

print(count_vowels_cached("Hello World"))  # This will compute and print the count
print(count_vowels_cached("Hello World"))  # This will return the cached result without printing

# Another example where we add a function shows us how many times execution occurs
@lru_cache(maxsize=128)
def count_vowels_cached(sentence: str) -> int:
    """Counts the number of vowels in a given sentence (with LRU caching)."""
    print(f"Counting vowels in: '{sentence}'") # This will only print the first time we call the function with a new sentence, subsequent calls with the same sentence will return the cached result without printing.
    return sum(1 for char in sentence if char.lower() in 'aeiou') # This will compute the count of vowels in the sentence and return it.

@measure
def main() -> None:
    sentences: list[str] = [
        "Hello World",
        "Python is great",
        "LRU Cache is useful",] # We have a list of sentences that we will use to test our cached function. Each sentence will be processed multiple times to demonstrate the caching mechanism.
    
    for sentence in sentences: # We iterate over each sentence in the list of sentences.
        for i in range(1_000_000): # We call the cached function 1 million times for each sentence to demonstrate the performance benefits of caching. The first call will compute the result and cache it, while subsequent calls will return the cached result, significantly reducing execution time.
            count_vowels_cached(sentence) # This calls the cached function to count the vowels in the current sentence. The first call for each unique sentence will compute the result and cache it, while subsequent calls will return the cached result, demonstrating the efficiency of the LRU cache.

if __name__ == "__main__":    main()
print(count_vowels_cached.cache_info()) # This will print the cache information, showing the number of hits, misses, current size, and maximum size of the cache.


# Another example with fibonacci sequence, which is a common example to demonstrate the benefits of caching due to its recursive nature.
@lru_cache(maxsize=None) # We set maxsize to None to allow unlimited caching, which is useful for the Fibonacci function as it can generate a large number of unique inputs.
def fibonacci(n: int) -> int:
    """Returns the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) # This is the recursive definition of the Fibonacci sequence. The LRU cache will store previously computed results, significantly improving performance for larger values of n.  

@measure
def main() -> None:
    result: int = fibonacci(10) # This will compute the 10th Fibonacci number. The first time this function is called, it will compute the result recursively, but subsequent calls with the same input will return the cached result, demonstrating the efficiency of the LRU cache.
    print(result)

if __name__ == "__main__":
    main()