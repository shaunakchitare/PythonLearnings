

CURRENT_GEN = [
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 0],
[0, 1, 1, 0, 1, 0],
[1, 0, 0, 0, 0, 0]
]

SIZE_X = len(CURRENT_GEN)
SIZE_Y = len(CURRENT_GEN[0])

#-------------------------------------------------------------------------------

def print_my_data():
    for data in CURRENT_GEN:
        print(data)

def get_neighbour_count(x, y):

    count = 0

    n1_x = x - 1
    n1_y = y - 1
    v1 = get_cell_value(n1_x,n1_y)

    n2_x = x - 1
    n2_y = y
    v2 = get_cell_value(n2_x,n2_y)

    n3_x = x - 1
    n3_y = y + 1
    v3 = get_cell_value(n3_x,n3_y)

    n4_x = x
    n4_y = y + 1
    v4 = get_cell_value(n4_x,n4_y)

    n5_x = x + 1
    n5_y = y + 1
    v5 = get_cell_value(n5_x,n5_y)

    n6_x = x + 1
    n6_y = y
    v6 = get_cell_value(n6_x,n6_y)

    n7_x = x + 1
    n7_y = y - 1
    v7 = get_cell_value(n7_x,n7_y)

    n8_x = x
    n8_y = y - 1
    v8 = get_cell_value(n8_x,n8_y)

    count = sum([v1, v2, v3, v4, v5, v6, v7, v8])
    return count

#-------------------------------------------------------------------------------



def get_cell_value(n_x, n_y):
    v = 0
    if n_x >= 0 and n_y >= 0 and n_x < SIZE_X and n_y < SIZE_Y:
        v = CURRENT_GEN[n_x][n_y]
    return v


#-------------------------------------------------------------------------------

count = get_neighbour_count(5, 5)

print(count)
