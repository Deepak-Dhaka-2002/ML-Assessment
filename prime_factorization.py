def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        count = 0
        while (n % i) == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append((i, count))
        i += 1
    if n > 1:
        factors.append((n, 1))
    return factors

if __name__ == "__main__":
    number = int(input("Enter an integer to perform prime factorization: "))
    factors = prime_factors(number)
    print(f"Prime factors of {number}: {factors}")
