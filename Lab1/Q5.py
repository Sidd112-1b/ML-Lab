import random
import statistics

def operations(numbers):
    mean=statistics.mean(numbers)
    median=statistics.median(numbers)
    mode=statistics.mode(numbers)
    return mean,median,mode

numbers = [random.randint(100, 150) for _ in range(100)]
print("List of 100 random numbers: ")
print(numbers)

m1,m2,m3=operations(numbers)

print("Mean =", m1)
print("Median =", m2)
print("Mode =", m3)