import matplotlib.pyplot as plt

import time
import timeit

def powerIterative(a, n):
    r = 1   
    for i in range(n):
        r *= a
    return r

def powerDivideConquer(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        hp = powerDivideConquer(a, n // 2)
        return hp * hp
    else:
        hp = powerDivideConquer(a, (n - 1) // 2)
        return hp * hp * a


exponents = list(range(1, 106))  # You can adjust the range accordingly
resultsIterative = []
resultsDivideConquer = []

for exponent in exponents:
    base = 2  # Choose any base
    timeIterative = timeit.timeit(lambda: powerIterative(base, exponent), number=1000)
    resultsIterative.append(timeIterative)

    timeDivideConquer = timeit.timeit(lambda: powerDivideConquer(base, exponent), number=1000)
    resultsDivideConquer.append(timeDivideConquer)

# Plotting the results using a plotting library (e.g., Matplotlib)


plt.plot(exponents, resultsIterative, label='Iterative')
plt.plot(exponents, resultsDivideConquer, label='Divide & Conquer')
plt.xlabel('Exponent')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Iterative against Divide-Conquer')
plt.show()
print(resultsIterative)
print(resultsDivideConquer)