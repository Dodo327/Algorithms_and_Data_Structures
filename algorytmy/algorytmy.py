import math

def max_min(S):
    #S - zbiór elementów
    #Funkcja zwraca minimalny i maksymalny element zbioru
    #T(n) = 2(n−1)= O(n)
    
    s = len(S)
    if s == 1:
        return (S[0], S[0])
    else:
        z = math.ceil(s/2)
        S1 = S[0:z]
        S2 = S[z:]
        (min1, max1) = max_min(S1)
        (min2, max2) = max_min(S2)
        return (min(min1, min2), max(max1,max2))
    
def Hanoi(n, froM = "a", to = "b", using = "c"):
    #rozwiązanie problemu wież Hanoi
    #n - liczba krążków
    #T(n) = 2·T(n-1)+1 = 2·(2·T(n-2)+1)+1 = 2^(n-1)·T(1)+(2^(n-2)+2^(n-3)+...+1) = 2^(n-1)= O(2^n)
    
    if n == 1:
        print(froM + "-->" + to)
    
    else:
        Hanoi(n-1, froM, using, to)
        print(froM + "-->" + to)
        Hanoi(n-1, using, to, froM)


#ciąg fibbonacciego
def fib1(n):
    # O(2^n)
    
    if (n<=2): return 1
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    #O(n)
    f = [None] * (n)
    f[0] = f[1] = 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    
    return f[n-1]

S = [1, 23, 5, 5]
print(max_min(list(S)))
Hanoi(3)
print(fib1(10))
print(fib2(10))