def fibonacci_number(n):
    array = [0, 1]
    for i in range(2, n + 1):
        array.append(array[i - 1] + array[i - 2])
    return array[n]


input_n = int(input())
print(fibonacci_number(input_n))
