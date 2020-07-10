

current_gen = [
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 0],
[0, 1, 1, 0, 0, 0],
[1, 0, 0, 0, 0, 0]
]


def print_my_data():
    for data in current_gen:
        print(data)

#-------------------------------------------------------------------------------
def get_neighbour_count(current_gen, x, y):

    count = 0
    n1_x = x - 1
    n1_y = y - 1
    v1 = current_gen[n1_x][n1_y]
    if 1 == v1:
        count = count + 1

    n2_x = x - 1
    n2_y = y
    v2 = current_gen[n2_x][n2_y]
    if 1 == v2:
        count = count + 1

    n3_x = x - 1
    n3_y = y + 1
    v3 = current_gen[n3_x][n3_y]
    if 1 == v3:
        count = count + 1

    n4_x = x
    n4_y = y + 1
    v4 = current_gen[n4_x][n4_y]
    if 1 == v4:
        count = count + 1

    n5_x = x + 1
    n5_y = y + 1
    v5 = current_gen[n5_x][n5_y]
    if 1 == v5:
        count = count + 1

    n6_x = x + 1
    n6_y = y
    v6 = current_gen[n6_x][n6_y]
    if 1 == v6:
        count = count + 1

    n7_x = x + 1
    n7_y = y - 1
    v7 = current_gen[n7_x][n7_y]
    if 1 == v7:
        count = count + 1

    n8_x = x
    n8_y = y - 1
    v8 = current_gen[n8_x][n8_y]
    if 1 == v8:
        count = count + 1

    return count


count = get_neighbour_count(current_gen, 0, 1)

print(count)
