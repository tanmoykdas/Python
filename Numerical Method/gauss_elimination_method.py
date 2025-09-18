import copy
def gauss_elimination(arr,N):
    for i in range(N):
        # Eliminate entries below the pivot
        for j in range(i + 1, N):
            factor = arr[j][i] / arr[i][i]
            for k in range(i, N + 1):
                arr[j][k] -= factor * arr[i][k]
        print(f"after elimination {i + 1}")
        for l in range(N):
            print(arr[l])
        print()

    # Back substitution
    solve = [0] * N
    for i in range(N-1, -1, -1):
        solve[i] = arr[i][N]
        for j in range(i+1, N):
            solve[i] -= arr[i][j] * solve[j]
        solve[i] /= arr[i][i]
    print("Solution:", solve)
    return solve
N = 3
a = [
    [3,-0.1,-0.2,7.85],
    [0.1,7,-0.3,-19.3],
    [0.3,-0.2,10,71.4]
]
print ("initial array:")
for i in range(N):
    print (a[i])
print()
b = copy.deepcopy(a)
gauss_elimination(b, N)