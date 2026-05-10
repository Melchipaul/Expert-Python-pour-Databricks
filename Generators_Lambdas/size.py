import sys

def my_range(n: int):
    """A generator that yields numbers from 0 to n-1"""
    start = 0
    while start < n:
        yield start
        start += 1



#big_range = range(100000)
big_range = my_range(5) 

print(next(big_range))  # → 0

print("big_range is of type: {0}".format(type(big_range)))
print("Size of big_range: {0} bytes".format(sys.getsizeof(big_range)))

# create a list from big_range
big_list = []

for val in big_range:
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again ... or not")

for i in my_range(5):
    print("i is {}".format(i))