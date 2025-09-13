num = 600851475143
prime_factors = []

i = 2
while i * i <= num:
  while num % i == 0:
    prime_factors.append(i)
    num //= i
  i += 1

if num > 1:
  prime_factors.append(num)

print(f"Largest prime factor of number: {max(prime_factors)}")
