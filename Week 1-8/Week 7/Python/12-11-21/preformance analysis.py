#1. Creation of List,set and tuple

import timeit
print(timeit.timeit(stmt="lst=[1,2,3,4,5,6,7]", number=10000))
print(timeit.timeit(stmt="tup=(1,2,3,4,5,6,7)", number=10000))
print(timeit.timeit(stmt="s={1,2,3,4,5,6,7}", number=10000))
