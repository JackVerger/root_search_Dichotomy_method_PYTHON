
    #############
    # LIBRARIES #
    #############

import time



    ###############
    # SUBPROGRAMS #
    ###############

# Method to define our function
def f(x):
    return pow(x, 2) - x - 1 # YOUR FUNCTION


# Method to apply the dichotomy algorithm
def simpleDichotomy():
    epsilon = 1.0E-10 # Determines the precision
    n_max = 200 # Determines the maximum number of iterations
    n = 0  # Calculates the number of iteration
    a, b = 0, 0 # Respectively the left bound and the right bound of the algorithm

    # The user has to enter valid values to define the first bounds of the algorithm
    while b<a or f(a)*f(b)>=0.0:
        a = int(input("Left bound : "))
        b = int(input("Right bound : "))

    # We register the time at the beginning to calculate the execution time later
    beginning = time.perf_counter()

    while abs(b-a)>epsilon and n<n_max:

        # We increment the number of iterations
        n += 1

        # Calculate the value of the middle of the interval
        x = (a+b)/2
        y = f(x)

        # IF the left part does not contain the root
        if f(a)*y > 0.0:
            a = x # We move the left bound

        # ELSE IF the right part does not contain the root
        else:
            b = x # We move the right bound

    # We register the time at the end to calculate the execution time later
    end = time.perf_counter()

    print("iteration : " + str(n))
    print("racine x : " + str(x))
    print("f(x) : " + str(f(x)))
    print("Time : " + str(end - beginning))


# Method to apply the dichotomy algorithm in a recursive way
def recursiveDichotomyMain():
    def recursiveDichotomy(a, b, epsilon, n, n_max, x):

        # IF we didn't find the root
        if abs(b - a) > epsilon and n < n_max:

            # We calculate the value of the middle of the interval
            x = (a + b) / 2
            y = f(x)

            # IF the left part does not contain the root
            if f(a) * y > 0.0:
                return recursiveDichotomy(x, b, epsilon, n + 1, n_max,
                                          x)  # We continue the recursive method and move the left bound

            # ELSE IF the right part does not contain the root
            else:
                return recursiveDichotomy(a, x, epsilon, n + 1, n_max,
                                          x)  # We continue the recursive method and move the right bound

        # ELSE, we found the root
        else:
            return x, n

    epsilon = 1.0E-10  # Determines the precision
    n_max = 200  # Determines the maximum number of iterations
    a, b = 0, 0  # Respectively the left bound and the right bound of the algorithm

    # The user has to enter valid values to define the first bounds of the algorithm
    while b < a or f(a) * f(b) >= 0.0:
        a = int(input("Left bound : "))
        b = int(input("Right bound : "))

    # We register the time at the beginning to calculate the execution time later
    beginning = time.perf_counter()

    # We apply the recursive dichotomy
    x, n = recursiveDichotomy(a, b, epsilon, 0, n_max, 0)

    # We register the time at the end to calculate the execution time later
    end = time.perf_counter()

    print("iteration : " + str(n))
    print("racine x : " + str(x))
    print("f(x) : " + str(f(x)))
    print("Time : " + str(end - beginning))


# We define a shortcut to better choose the method to apply
dichotomy_methods = {
    0: simpleDichotomy,
    1: recursiveDichotomyMain,
}


    ########
    # MAIN #
    ########

# We display a simple menu
print("Choose one method to calculate the root of your function:")
print("1. Simple dichotomy")
print("2. Recursive dichotomy")
print("3. Visualisation of the dichotomy algorithm")

# The user has to choose between the three options
method_choice = -1
while method_choice not in [1, 2, 3]:
    method_choice = int(input("Choice : "))

    # IF the user made a mistake
    if method_choice not in [1, 2, 3]:
        print("Invalid choice\n")

# We launch the method that has been chosen by the user
dichotomy_methods[method_choice-1]()
