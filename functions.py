import random
import time
from sympy import isprime, primerange, gcd
from math import isqrt

# Функція для генерації великого простого числа
def generate_large_prime(bits, t):
    start_time = time.perf_counter() 
    iterations = 0 
    while True:
        iterations += 1
        # Генеруємо випадкове n-бітове непарне число з встановленим старшим бітом
        candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        # Перевіряємо, чи є число простим за допомогою тесту Рабіна-Міллера
        if rabin_miller_test(candidate, t):
            elapsed_time = time.perf_counter() - start_time
            print(f"A prime number generated by {iterations} iterations and {elapsed_time} seconds")
            return candidate

# Функція для перевірки простоти числа за тестом Рабіна-Міллера
def rabin_miller_test(n, t):
    # Перевіряємо, чи є число меншим за 2 або парним
    if n < 2 or n % 2 == 0:
        return False
    # Розкладаємо n-1 у вигляді 2^r * s
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(t):
        # Вибираємо випадкове число a з діапазону [2, n-2]
        a = random.randint(2, n - 2)
        # Вираховуємо a^s mod n
        x = pow(a, s, n)
        # Якщо x == 1 або x == n-1, число може бути простим
        if x == 1 or x == n - 1:
            continue
        # Повторно підносимо x до квадрату r-1 разів
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:  # Якщо x == n-1, переходимо до наступної ітерації
                break
        else:
            return False 
    return True 

# Функція для пошуку простих чисел у заданому діапазоні
def primes_in_range(start, end):
    start_time = time.perf_counter() 
    primes = list(primerange(start, end + 1))
    elapsed_time = time.perf_counter() - start_time 
    print(f"Prime numbers in the range [{start}, {end}] are found in {elapsed_time} seconds.")
    return primes

# Функція для знаходження примітивних коренів за модулем p
def find_primitive_roots(p, count=100):
    if not isprime(p):
        raise ValueError("The number must be prime.")
    
    start_time = time.perf_counter() 
    phi = p - 1  # Значення функції Ейлера
    factors = factorize(phi)  # Факторизація phi для пошуку примітивних коренів
    roots = []  

    for candidate in range(2, p):
        # Перевіряємо, чи кандидат задовольняє умови примітивного кореня
        if all(pow(candidate, phi // factor, p) != 1 for factor in factors):
            roots.append(candidate) 
        if len(roots) == count:  # Якщо знайдено потрібну кількість коренів, припиняємо пошук
            break

    elapsed_time = time.perf_counter() - start_time 
    print(f"Found {len(roots)} primitive roots for {p} in {elapsed_time} seconds.")
    return roots

# Допоміжна функція для факторизації числа
def factorize(n):
    factors = set()
    # Перебираємо всі можливі дільники до sqrt(n)
    for i in range(2, isqrt(n) + 1):
        while n % i == 0:  # Якщо i є дільником, додаємо його до множини
            factors.add(i)
            n //= i
    if n > 1:  # Якщо залишок n > 1, додаємо його до множини
        factors.add(n)
    return factors
