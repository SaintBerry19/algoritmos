def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous_digit = 0
    current_digit = 1

    for _ in range(n - 1):
        previous_digit, current_digit = (
            current_digit,
            (previous_digit + current_digit) % 10,
        )

    return current_digit


n = int(input())
print(fibonacci_last_digit(n))
