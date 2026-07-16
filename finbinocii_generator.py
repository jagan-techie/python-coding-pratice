def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Infinite generator initialized
fib = fibonacci_generator()

# Print the first 10 Fibonacci numbers dynamically
for _ in range(10):
    print(next(fib), end=" ")
