def row_sums(mat):
    kol_simv = len(mat[0])
    for elem in mat:
        if len(elem) != kol_simv:
            raise ValueError
    otvetik = []
    for elem in mat:
        otvetik.append(sum(elem))
    return otvetik

mat = [[1, 2, 3], [4, 5, 6]]
print(row_sums(mat))