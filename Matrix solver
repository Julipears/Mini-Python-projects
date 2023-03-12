import numpy as np


def print_matrix(M_lol):
    M = np.array(M_lol)
    print(M)


def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)


def get_row_to_swap(M, start_i):
    max_l_ind = len(M)
    max_l_row = start_i
    for i in range(len(M)-start_i):
        row_ind = get_lead_ind(M[start_i+i])
        if row_ind < max_l_ind:
            max_l_ind = row_ind
            max_l_row = start_i+i
    return max_l_row


def add_rows_coefs(r1, c1, r2, c2):
    new_r = [0] * len(r1)
    for i in range(len(r1)):
        new_r[i] = c1*r1[i] + c2*r2[i]
    return new_r


def eliminate(M, row_to_sub, best_lead_ind):
    start_ind = best_lead_ind
    for row in range(row_to_sub+1, len(M)):
        if M[row_to_sub][start_ind] != 0:
            coef = M[row][start_ind] / M[row_to_sub][start_ind]
            for col in range(start_ind, len(M[row])):
                M[row][col] = M[row][col] - coef*M[row_to_sub][col]


def forward_step(M):
    print("Now performing the forward step")
    print(f"The matrix is currently:\n{M}")
    for i in range(len(M)):
        print(f"Now looking at row {i}:")
        swap = get_row_to_swap(M, i)
        print(f"Swapping rows {i} and {swap} so that entry {get_lead_ind(M[swap])} in the current row is non-zero.")
        M[i], M[swap] = M[swap], M[i]
        print(f"The matrix is currently:\n{M}")

        eliminate(M, i, get_lead_ind(M[i]))
        print(f"Adding row {len(M)-i-1} to rows below it to eliminate coefficients in column {get_lead_ind(M[i])}")
        print(f"The matrix is currently:\n{M}")
        print("===================================")
    print("Done with the forward step")


def backward_step(M):
    print("Now performing the backward step")
    for i in range(len(M)):
        M2 = M[::-1]
        eliminate(M2, i, get_lead_ind(M2[i]))
        print(f"Adding row {len(M)-i-1} to rows above it to eliminate coefficients in column {get_lead_ind(M2[i])}")
        print(f"The matrix is currently:\n{M}")
        print("===================================")
    print("Now divide each row by the leading coefficient")
    for i in range(len(M)):
        coef = M[i][get_lead_ind(M[i])]
        for j in range(get_lead_ind(M[i]), len(M[i])): # Starting index could also just be 0
            M[i][j] /= coef
    print(f"The matrix is currently:\n{M}")
    print("Done with the backward step")


def solve_x(M, b):
    for row in range(len(M)):
        M[row].append(b[row])
    forward_step(M)
    backward_step(M)
    solution = []
    for i in range(len(M)):
        solution.append(M[i][-1])
    return solution
    
print(solve_x([[1,-2,3],[3,10,1],[1,5,3]], [22, 314, 92]))
