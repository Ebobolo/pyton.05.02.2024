# class fib:
#     def __init__(self, nn):
#         print("__init__")
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print("__iter__")
#         return self
#
#     def __next__(self):
#         print("__next__")
#         self.__i += 1
#         if self.__i > self.__n:
#             return StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
# for i in fib(10):
#     print(i)




def fun(n):
    for i in range(n):
        return i
print(fun(5))




def fun(n):
    for i in range(n):
        yield i
for v in fun(5):
    print(v)

# def powersOf2(n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2
# t = [x for x in powersOf2(5)]
# print(t)

# def powersOf2(n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2
# t = list(powersOf2(3))
# print(t)

def powersOf2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2
for i in range(20):
    if i in powersOf2(4):
        print(i)


def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n
fibs = list(Fib(10))

print(fibs)

kkr = [1>]