import matplotlib.pyplot as plt
from collections import Counter

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

number = int(input("Введіть тризначне число: "))

if 100 <= number <= 999:
    factors = prime_factors(number)
    factor_counts = Counter(factors)

    plt.figure(figsize=(8, 6))
    plt.bar(factor_counts.keys(), factor_counts.values(), color='skyblue')

    plt.xlabel('Прості множники')
    plt.ylabel('Частота появи')
    plt.title(f'Частота появи простих множників для числа {number}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    print("Будь ласка, введіть тризначне число.")
