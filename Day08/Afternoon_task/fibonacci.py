# A2: Generator for Fibonacci numbers

def fibonacci(n):
    """Yield the first n Fibonacci numbers."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# --- Test ---
print("First 10 Fibonacci numbers:")
for num in fibonacci(10):
    print(num, end=" ")
print()

# Infinite generator version
def fibonacci_infinite():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci_infinite()
print("\nFirst 15 (infinite generator):")
print([next(gen) for _ in range(15)])

