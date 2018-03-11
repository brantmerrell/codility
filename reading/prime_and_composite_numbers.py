"""https://codility.com/media/train/8-PrimeNumbers.pdf"""
def divisors(int_n):
    """Counting the number of divisors - O(n^.5)"""
    itr_i = 0
    result = 0
    while itr_i * itr_i < int_n:
        if int_n % itr_i == 0:
            result += 2
        itr_i += 1
    if itr_i * itr_i == int_n:
        result += 1
    return result
def primality(int_n):
    """Primality test - O(n^.5)"""
    itr_i = 2
    while itr_i * itr_i <= int_n:
        if int_n % itr_i == 0:
            return False
        itr_i += 1
    return True
def coins(int_n):
    """Reversing coins - O(n * log (n))"""
    result = 0
    coin = [0] * (int_n + 1)
    for ndx_i in range(1, int_n + 1):
        ndx_k = ndx_i
        while ndx_k <= ndx_i:
            coin[ndx_k] = (coin[ndx_k] + 1) % 2
            ndx_k += 1
        result += coin[ndx_i]
    return result
# debugging:
divisors(12)
