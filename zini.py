import numpy as np

(m, n) = input().split()
m = int(m)
n = int(n)
mat = []
for i in range(0, m):
    t = input().split()
    t = list(map(int, t))
    mat.append(t)
mat = np.array(mat)
temp = 0
if m < 3 or n < 3:
    print(temp)
else:
    for i in range(1, (m-1)):
        for j in range(1, (n-1)):
            t = mat[i][j]
            if t > mat[i][j+1]:
                if t > mat[i][j-1]:
                    if t < mat[i+1][j]:
                        if t < mat[i-1][j]:
                            temp += 1
            elif t < mat[i][j+1]:
                if t < mat[i][j-1]:
                    if t > mat[i+1][j]:
                        if t > mat[i-1][j]:
                            temp += 1
            else:
                continue
print(temp)