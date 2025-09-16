def falsi(f, a, b, tol = 1e-6, max = 100):
    if (f(a) * f(b) >= 0):
        print("false position not possible with this a and b")
        return None
    else:
        for i in range(max):
            c = (a * f(b) - b * f(a)) / (f(b) - f(a))
            print(f"after {i + 1} itertation c = {c:.4f} and f(c) = {f(c):.6f}")
            if abs(f(c)) < tol:
                print(f"the root is {c:.6f} after {i + 1} iterations")
                return c
            if (f(c) * f(a) < 0):
                b = c
            else:
                a = c

        print("did not converge within the maximum number of iterations")
        return None



f = lambda x: x**3 - 5*x - 9
a = 2
b = 3
falsi(f, a, b)