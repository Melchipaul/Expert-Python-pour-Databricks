def oodnumbers():
    n = 1
    while True:
        yield n
        n += 2

def pi_series():
    odds = oodnumbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation

approxi_pi = pi_series()
for _ in range(10000000):
    print(next(approxi_pi))