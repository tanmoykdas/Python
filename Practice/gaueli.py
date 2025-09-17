import copy

def print_arr(arr, N):
    for i in range(N):
        print(arr[i])

def gauss_elimination(arr, N):
    for i in range(N):
        for j in range(N):
            arr[i][j] /= arr[i][i]
        
        for j in range(i+1, N):
            factor = arr[j][i]
            for k in range(i, N+1):
                arr[j][k] -= arr[i][k] * factor

        print("After elimination step", i+1)
        print_arr(arr, N)
        print()

    solve = [0] * N
    for i in range(N-1, -1, -1):
        solve[i] = arr[i][N]
        for j in range(i+1, N):
            solve[i] -= arr[i][j] * solve[j]
        solve[i] /= arr[i][i]

    print("Solution:", solve)
    return solve

N = 3
arr = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

arr_copy = copy.deepcopy(arr)

print("Initial matrix:")
print_arr(arr, N)
print()

gauss_elimination(arr_copy, N)