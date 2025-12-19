
# Take input from the user
num = int(input("Enter a number: "))

# 0 and 1 are not prime numbers
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    # Assume the number is prime
    is_prime = True

    # Check for factors from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Use if-else to print the result
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
