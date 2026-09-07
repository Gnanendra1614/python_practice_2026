def square_numbers(n):

    for i in range(1, n + 1):
        yield i ** 2


squares = square_numbers(5)

for value in squares:
    print(value)