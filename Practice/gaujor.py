import copy

def gauss_jordan(b, n):
    # Gauss-Jordan elimination
    for i in range(n):
        # Make the diagonal element 1
        factor = b[i][i]
        for k in range(i, n+1):
            b[i][k] /= factor
        # Eliminate all other entries in column i
        for j in range(n):
            if j != i:
                factor = b[j][i]
                for k in range(i, n+1):
                    b[j][k] -= factor * b[i][k]
        # Print matrix after each row operation
        for l in range(n):
            print(b[l])
        print()
    # Solution is last column
    solution = [b[i][n] for i in range(n)]
    print("Final solution:", solution)
    return solution

a = [
    [3,-0.1,-0.2,7.85],
    [0.1,7,-0.3,-19.3],
    [0.3,-0.2,10,71.4]
]

b = copy.deepcopy(a)
n = 3
gauss_jordan(b, n)
