from time import perf_counter
import random

# Fibonacci implementation
def Fib(n):

    if n in {0, 1}:
         return n
    return Fib(n - 1) + Fib(n - 2) 

# Variable to hold the start time
start_time = perf_counter()

# Generate the nth term where n is a random number from 15 to 35
n = random.randint(15, 35) 

# Print  the result of the Fibonacci implementation
print('fib(',n,')=',Fib(n))

# Variable to hold the end time
end_time = perf_counter()

# Calculate the elapsed time and store in a variable
time_elapsed = end_time - start_time

# Print the time elapsed for the fibonacci implemetaion
print('fib(',n,') took ', time_elapsed, 'seconds' )