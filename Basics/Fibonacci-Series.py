# Fibonacci Series.

def fibonacci(n):
    series = []
    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


n = int(input("Enter number of terms: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    print("Fibonacci Series:", fibonacci(n))