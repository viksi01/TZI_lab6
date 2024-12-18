from sympy import isprime
from functions import find_primitive_roots, generate_large_prime, primes_in_range


def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate a large prime number")
        print("2. Search for prime numbers in a range")
        print("3. Find primitive roots for a number")
        print("4. Exit")
        
        choice = input("Your choice: ").strip()
        
        if choice == "1":
            while True:
                try:
                    bits = int(input("Enter the number of bits: "))
                    t = int(input("Enter the number of checks (t): "))
                    if t < 1:
                        raise ValueError("The number of checks must be positive.")
                    prime = generate_large_prime(bits, t)
                    print(f"Generated prime number: {prime}")
                    break
                except ValueError as e:
                    print(f"Input error: {e}. Please try again.")
        
        elif choice == "2":
            while True:
                try:
                    start = int(input("Enter the start of the range: "))
                    end = int(input("Enter the end of the range: "))
                    if start >= end:
                        raise ValueError("The start of the range must be less than the end.")
                    primes = primes_in_range(start, end)
                    print(f"Prime numbers in the range: {primes}")
                    break
                except ValueError as e:
                    print(f"Input error: {e}. Please try again.")
        
        elif choice == "3":
            while True:
                try:
                    p = int(input("Enter a prime number: "))
                    if not isprime(p):
                        raise ValueError("The number must be prime.")
                    roots = find_primitive_roots(p)
                    print(f"The first primitive roots of number {p}: {roots}")
                    break
                except ValueError as e:
                    print(f"Input error: {e}. Please try again.")
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
