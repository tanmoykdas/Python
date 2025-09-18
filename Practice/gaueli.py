import copy
def elimination(b, n):

    #forward elimination
    for i in range(n):
        for j in range(i+1,n):
            factor = b[j][i]/b[i][i]
            for k in range(i,n+1):
                b[j][k] -= factor * b[i][k]
        for l in range(n): #printing array after one row operation
            print(b[l])
        print()

    #back substitution   
    solve = [0] * n
    for i in range(n-1, -1, -1):
        solve[i] = a[i][n]
        for j in range(i+1,n):
            solve[i] -= b[i][j] * solve[j]
        solve[i] /= b[i][i]

    print("final soltuion", solve)
    return solve

a = [
    [3,-0.1,-0.2,7.85],
    [0.1,7,-0.3,-19.3],
    [0.3,-0.2,10,71.4]
]

b = copy.deepcopy(a)
n = 3
elimination(b, n)