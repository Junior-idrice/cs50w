from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR ON {n}, is expected to be {expected}")