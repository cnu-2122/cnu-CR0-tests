# Three different (correct) example solutions.

# ---
# First example solution

def p_norm_sol1(x, p):
    # Initialise the sum of all terms
    sum_elements = 0

    # Loop over each element
    for xi in x:
        # Take the absolute value, raise to the power of p, add to the sum
        sum_elements += abs(xi) ** p

    # Take the pth root of the result, return it
    return sum_elements ** (1 / p)


# ---
# Second example solution

def p_norm_sol2(x, p):
    # Start a list of terms
    list_terms = []

    # Loop over the number of elements in x
    for i in range(len(x)):
        # Take the absolute value, raise to the power of p
        new_term = abs(x[i]) ** p

        # Append the new term to the list
        list_terms.append(new_term)

    # Sum all elements of the list, take the pth root
    norm = sum(list_terms) ** (1/p)
    return norm


# ---
# Third example solution

import numpy as np

def p_norm_sol3(x, p):
    # Use np.linalg.norm() from the NumPy documentation
    return np.linalg.norm(x, p)


# ---
# Tests
# This is not exhaustive -- you may have found other tests yourself.

# First, pick one of the 3 example solutions.
# (note that we can give alternative names to functions too!)
p_norm = p_norm_sol1

# The following tests pass if the result is True.

# Testing different values of p
print(round(p_norm([1, 1], 1), 5) == 2)
print(round(p_norm([1, 1], 2), 5) == 1.41421)
print(round(p_norm([1, 1], 3), 5) == 1.25992)
print(round(p_norm([1, 1], 8), 5) == 1.09051)

# Testing different lengths of x
print(round(p_norm([1], 4), 5) == 1)
print(round(p_norm([1]*3, 4), 5) == 1.31607)
print(round(p_norm([1]*5, 4), 5) == 1.49535)

# Test with a known result
x = [2, 2, 2]
y = [2, -2, 2]

import numpy as np
print(round(p_norm(x, 2), 5) == round(np.sqrt(12), 5))

# Testing that the absolute value was taken correctly (odd values of p, negative values of x_i)
for p in range(1, 10):
    print(p_norm(x, p) == p_norm(y, p))

# Test some edge cases
for p in range(1, 6):
    print(p_norm([0]*10, p) == 0)
    print(p_norm([0, 0, 0, 1, 0, 0], p) == 1)
