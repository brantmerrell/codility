"""https://codility.com/media/train/9-Sieve.pdf"""
def sieve(int_n):
    """Sieve of Eratosthenes"""
    sieve = [True] * (int_n + 1)
    sieve[0] = sieve[1] = False
        # equivalent to Rscript -e "sieve[1:2] <- F"
    itr_i = 2
    while itr_i * itr_i <= int_n:
        if sieve[itr_i]:
            unk_k = itr_i * itr_i
            while unk_k <= int_n:
                sieve[unk_k] = False
                unk_k += 1
        itr_i += 1
    return sieve
def array_f(int_n):
    """Preparing the array F for factorization"""
    arr_f = [0] * (int_n + 1)
    itr_i = 2
    while itr_i * itr_i <= int_n:
        if arr_f[itr_i] == 0:
            unk_k = itr_i * itr_i
            while unk_k <= int_n:
                if arr_f[unk_k] == 0:
                    arr_f[unk_k] = itr_i
                unk_k += itr_i
        itr_i += 1
    return arr_f
def factorization(unk_x, arr_f):
    """Factorization of x - O(log x)"""
    prime_factors = []
    while arr_f[unk_x] > 0:
        prime_factors += arr_f[unk_x]
        unk_x /= arr_f[unk_x]
    prime_factors += unk_x
    return prime_factors
