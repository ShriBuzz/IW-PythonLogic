# Write a Python function that takes a number as a parameter and check the
# number is prime or not.

n = int(input("Enter a number: "))


def check_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")

    else:
        print(n, "is not a prime number")


check_prime(n)
