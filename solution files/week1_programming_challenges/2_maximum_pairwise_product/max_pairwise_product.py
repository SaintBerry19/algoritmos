def max_pairwise_product(numbers):
    n = len(numbers)
    index = 0
    for i in range(1, n):
        if numbers[i] > numbers[index]:
            index = i
    numbers[n-1] , numbers[index] = numbers[index], numbers[n-1]
    index = 0
    for i in range(1, n-1):
        if numbers[i] > numbers[index]:
            index = i
    numbers[n-2], numbers[index] = numbers[index], numbers[n-2]
    return numbers[n-1]*numbers[n-2]

if __name__ == "__main__":
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
