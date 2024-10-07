# Input:

# n: A positive integer (1 <= n <= 10^6).
# Output:

# Return a string representing the prime factorization in the format: "factor^exponent".


def prime_factorization(n):
    factors_str = ""
    divisor = 2

    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            if factors_str:  # Append " * " if there are already factors
                factors_str += " * "
            factors_str += "{}^{}".format(divisor, count)
        divisor += 1

    return factors_str

# Example usage
print(prime_factorization(28))  # "2^2 * 7^1"
print(prime_factorization(100)) # "2^2 * 5^2"
print(prime_factorization(37))  # "37^1"
