from typing import List
import numpy as np

def get_data(fname: str) -> List[int]:
    with open(fname, 'r') as f:
        numbers = [int(n) for n in f.readlines()]
    return numbers


def check_number(data: List[int], pos: int, preamble_len: int) -> bool:
    number = data[pos]
    preamble = data[pos-preamble_len:pos]

    X = np.array(preamble)
    mat_X = np.matrix([X]* X.shape[0])
    res = mat_X + mat_X.T
    res
    locs, _ = np.where(res == number)
    # print(number, preamble, True if locs.shape[0] > 0 else False)
    return True if locs.shape[0] > 0 else False


def check_data(data: List[int], preamble_len: int) -> int:
    init_pos = preamble_len
    for pos in range(init_pos, len(data)):
        is_valid = check_number(data, pos, preamble_len)
        if not is_valid:
            return data[pos]


def find_contiguos_sum(data: List[int], corrupted_nmbr: int) -> int:
    for i in range(len(data)):
        for j in range(len(data)):
            total = sum(data[i:j])
            if total == corrupted_nmbr:
                return min(data[i:j]) + max(data[i:j])
            elif total > corrupted_nmbr:
                break
            else:
                continue

# data, preamble = get_data('advent_of_code/09_encoding_error/ex.txt'), 5
data, preamble = get_data('advent_of_code/09_encoding_error/input.txt'), 25
# print(data)
# print(preamble)
corrupted_nmbr = check_data(data, preamble)
# print(corrupted_nmbr)
print(find_contiguos_sum(data, corrupted_nmbr))
