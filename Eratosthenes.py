def sieve_of_eratosthenes(limit):
    # Create a boolean array "prime[0..limit]" and initialize all entries as True
    prime = [True for _ in range(limit + 1)]
    prime[0] = prime[1] = False  # 0 and 1 are not primes

    p = 2
    while p * p <= limit:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1

    # Compile the list of prime numbers
    primes = [num for num in range(limit + 1) if prime[num]]
    return primes

# Example usage:
limit = int(input("Enter a number"))
primes = sieve_of_eratosthenes(limit)
print("Prime numbers up to", limit, "are:", primes)
