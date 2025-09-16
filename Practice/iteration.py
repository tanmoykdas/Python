def iteration(f, x0, tol = 1e-6, max = 100):
    for i in range(max):
        x1 = f(x0)
        print(f"for iteration num:{i + 1} and value{x1:.6f}")
        if (abs(x1 - x0) < tol):
            print(f"the root is {x1:.6f} after {i + 1} iterations")
            return x1
        x0 = x1
    print("did not converge within the maximum number of iterations")
    return None
f = lambda x: 0.5 * (x + 2)
x0 = 1
iteration(f, x0)