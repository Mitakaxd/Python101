def matrix_bombing_plan(m):
    d = {}
    def legal(i,j):
        nonlocal m
        if i < 0 or j < 0 or i >= len(m) or j >= len(m[0]):
            return False
        return True
    maxsum = sum([sum(row) for row in m])
    curSum = maxsum
    for i in range(len(m)):
        for j in range(len(m[0])):
            lst = []
            for p in range(i-1, i+2):
                for k in range(j-1,j+2):
                    if p == i and k == j:
                        continue
                    if legal(p,k):
                        if m[p][k] < m[i][j]:
                            curSum -= m[p][k]
                        else:
                            curSum -= m[i][j]
            d[(i,j)] = curSum
            curSum = maxsum
    return d
# print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
