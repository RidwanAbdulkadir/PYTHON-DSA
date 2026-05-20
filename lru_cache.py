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
    print(f"Counting vowels in: '{sentence}'") #
    return sum(1 for char in sentence if char.lower() in 'aeiou')

@measure
def main() -> None:
    sentences: list[str] = [
        "Hello World",
        "Python is great",
        "LRU Cache is useful",]
    
    for sentence in sentences:
        for i in range(1_000_000):
            count_vowels_cached(sentence)

if __name__ == "__main__":    main()