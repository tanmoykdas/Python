# Bisection Method to find the root of a function
def bisection(f, a, b, tol = 1e-6, max = 100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    for i in range(max):
        c = (a + b) / 2
        print(f"Iteration {i + 1}: c = {c:.6f}, f(c) = {f(c):.6f}")
        if abs(f(c)) < tol:
            print(f"The root is approximately {c:.6f} after {i + 1} iterations.")
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    print("Did not converge within the maximum number of iterations.")
    return None


f = lambda x: x**3 + x - 1
a = 0
b = 1
bisection(f, a, b, tol = 1e-6, max = 100)