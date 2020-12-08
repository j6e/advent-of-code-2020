def get_seatid(line: str) -> int:
    row, col = line[:7], line[7:10]
    b_row = row.replace('F', '0').replace('B', '1')
    b_col = col.replace('R', '1').replace('L', '0')
    i_row, i_col = int(b_row, 2), int(b_col, 2)
    seat_id = i_row * 8 + i_col
    print(line[:-1], row, b_row, i_row, col, b_col, i_col, seat_id)
    return seat_id


if __name__ == "__main__":
    with open('advent_of_code/05_binary_boarding/input.txt', 'r') as f:
        lines = f.readlines()

    seats = []
    for line in lines:
        seat_id = get_seatid(line)
        seats.append(seat_id)

    print(max(seats))
