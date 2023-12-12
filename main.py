# Sara Ghasedi
# MATH 4610 Project 2

import math


def f(x):
    return (2 / math.sqrt(math.pi)) * math.exp(-x ** 2)


def second_der(x):
    return (4 / math.sqrt(math.pi)) * (2 * x ** 2 - 1) * math.exp(-x ** 2)


def fourth_der(x):
    return (8 / math.sqrt(math.pi)) * (4 * x ** 4 - 12 * x ** 2 + 3) * math.exp(-x ** 2)


def trapezoidal(a, b, n):
    h = (b - a) / n
    j = 1
    fxj = 0
    while j <= n - 1:
        xj = a + j * h
        fxj = fxj + f(xj)
        j = j + 1
    return (h / 2) * (f(a) + 2 * fxj + f(b))


def trapezoidal_error_bound(a, b, n):
    theta = 0
    h = (b - a) / n
    return abs(((b - a) / 12) * h ** 2 * second_der(theta))


def simpsons(a, b, n):
    h = (b - a) / n
    fxj1 = 0
    fxj2 = 0
    j = 1
    while j <= (n / 2) - 1:
        xj = a + 2 * j * h
        fxj1 = fxj1 + f(xj)
        j = j + 1
    j = 1
    while j <= (n / 2):
        xj = a + (2 * j - 1) * h
        fxj2 = fxj2 + f(xj)
        j = j + 1
    return (h / 3) * (f(a) + 2 * fxj1 + 4 * fxj2 + f(b))


def simpsons_error_bound(a, b, n):
    theta = 0
    h = (b - a) / n
    return abs(((b - a) / 180) * h ** 4 * fourth_der(theta))


def actual_error(val):
    return abs(0.842700792949715 - val)


def error_ratios(vals):
    ratios = []
    x = 0
    while x + 1 < len(vals):
        ratios.append(vals[x] / vals[x + 1])
        x = x + 1
    return ratios


def main():
    a = 0
    b = 1

    print("Trapezoidal Rule:")
    tvals = [trapezoidal(a, b, 2), trapezoidal(a, b, 4), trapezoidal(a, b, 8), trapezoidal(a, b, 16),
             trapezoidal(a, b, 32)]
    t_errors = []
    x = 0
    while x < len(tvals):
        t_errors.append(actual_error(tvals[x]))
        print(tvals[x], "; error:", t_errors[x])
        x = x + 1
    print("Ratios for Trapezoidal Rule errors:", error_ratios(t_errors))
    t_error_bounds = [trapezoidal_error_bound(a, b, 2), trapezoidal_error_bound(a, b, 4),
                      trapezoidal_error_bound(a, b, 8), trapezoidal_error_bound(a, b, 16),
                      trapezoidal_error_bound(a, b, 32)]
    print("Trapezoidal error bounds:", t_error_bounds)

    print()

    print("Simpson's Rule:")
    svals = [simpsons(a, b, 2), simpsons(a, b, 4), simpsons(a, b, 8), simpsons(a, b, 16), simpsons(a, b, 32)]
    s_errors = []
    x = 0
    while x < len(svals):
        s_errors.append(actual_error(svals[x]))
        print(svals[x], "; error:", s_errors[x])
        x = x + 1
    print("Ratios for Simpson's Rule errors:", error_ratios(s_errors))
    s_error_bounds = [simpsons_error_bound(a, b, 2), simpsons_error_bound(a, b, 4), simpsons_error_bound(a, b, 8),
                      simpsons_error_bound(a, b, 16), simpsons_error_bound(a, b, 32)]
    print("Simpson's error bounds:", s_error_bounds)


main()
