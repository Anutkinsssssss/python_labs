def transpose(mat):
    new_mat = []
    if len(mat) == 0:
        return []
    kol_simv = len(mat[0])
    for elem in mat:
        if len(elem) != kol_simv:
            raise ValueError
    for stolbik in range(kol_simv):
        new_strochechka = []
        for strochechka in range(len(mat)):
            new_strochechka.append(mat[strochechka][stolbik])
        new_mat.append(new_strochechka)
    return new_mat

mat = [[1, 2, 3]]
print(transpose(mat))
mat = [[1], [2], [3]]
print(transpose(mat))
mat = [[1, 2], [3, 4]]
print(transpose(mat))
mat = []
print(transpose(mat))
mat = [[1, 2], [3]]
print(transpose(mat))