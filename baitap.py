from math import *
def per(n):
    tong = 1
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong == n
def snt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True
def per2(n):
    for b in range(2, 35 ):
         if snt(b):
             if snt(2 ** b - 1):
                 if (2 ** b - 1) * (2 **(b - 1)) == n:
                     return True
    return False
if __name__ == '__main__':
    print(per2(6))