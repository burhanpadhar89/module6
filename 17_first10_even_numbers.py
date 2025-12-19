def first_10_even_numbers():
    num = 0
    for _ in range(10):
        yield num
        num += 2
for n in first_10_even_numbers():
    print(n)
