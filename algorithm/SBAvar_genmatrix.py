import SBA_variant
import numpy

outfile = "../ember_capacity/SBAvar"

def decide_end_level(point, level_alloc):
    for i in range(len(level_alloc)):
        rmin, rmax, wmin, wmax = level_alloc[i]    
        if point >= rmin and point < rmax:
            return i
    if point == 64: # last level
        return len(level_alloc)-1
    assert False, point

def simulate_error(level_alloc):
    num_levels = len(level_alloc)
    P = numpy.zeros((num_levels, num_levels))
    num_points = 0
    for i in range(len(level_alloc)):
        rmin, rmax, wmin, wmax = level_alloc[i]    
        d1s = SBA_variant.distributions[(wmin, wmax)]
        for point in d1s:
            end_level = decide_end_level(point, level_alloc)
            P[end_level][i] += 1
        for j in range(0, len(level_alloc)):
            P[j][i] = P[j][i] / len(d1s)
        num_points += len(d1s)
    return P

def get_dala():
    res = {}
    for i in range(4, 9):
        if i <= 5:
            res[i] = SBA_variant.minimal_BER(i, 1e-3, 0, 1, True)
        else:
            res[i] = SBA_variant.minimal_BER(i, 1e-3)
    print(res)
    return res

def simulate_all_levels(dala_allocs):
    for i in range(4, 9):
        P = simulate_error(dala_allocs[i])
        dump_matrix(P, outfile)

def dump_matrix(matrix, hint):
    num_level = len(matrix)
    with open(hint + str(num_level), "w") as fout:
        to_write = []
        for i in range(len(matrix)):
            to_write.append(",".join(map(str, matrix[i])) + "\n")
        fout.writelines(to_write)

if __name__ == "__main__":
    SBA_variant.init_model()
    dala_allocs = get_dala()
    simulate_all_levels(dala_allocs)