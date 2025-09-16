# Iterative Method to find root of the equation x^3 + x - 1 = 0
def iteration(g, x0, tol=12e-6, max_iter=100):
    for i in range(max_iter):
        x1 = g(x0)
        print(f"Iteration {i+1}: x = {x1:.6f}")
        if abs(x1 - x0) < tol:
            print(f"Root is {x1:.6f} after {i+1} iterations.")
            return x1
        x0 = x1
    print("Did not converge within the maximum number of iterations.")
    return None

g = lambda x: (1 - x)**(1/3) 
x0 = 0.5
iteration(g, x0)