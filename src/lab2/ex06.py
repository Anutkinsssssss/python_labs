def col_sums(mat):
    kol_simv = len(mat[0])
    for elem in mat:
        if len(elem) != kol_simv:
            raise ValueError
    otvetik = [0] * len(mat[0])
    for strochechka in mat:
        for stolbik in range(len(strochechka)):
            otvetik[stolbik] = otvetik[stolbik] + strochechka[stolbik]
    return otvetik

mat = [[1, 2, 3], [4, 5, 6]]
print(col_sums(mat))
mat = [[-1, 1], [10, -10]]
print(col_sums(mat))
mat = [[0, 0], [0, 0]]
print(col_sums(mat))
mat = [[1, 2], [3]]
print(col_sums(mat))