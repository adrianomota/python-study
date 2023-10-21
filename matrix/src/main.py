"""
matrix = [[1,2,3],
          [3,4,3],
          [5,6,6]]

"""

def print_matrix(m):
    if m == []:
        return
    
    # num_rows = len(m)
    # num_cols = len(m[0])

    for row in m:
        line_to_print=""
        for num in row:
            line_to_print += str(num) + " "
        print(line_to_print)

def create_matrix(m,n):
    my_matrix = []
    for i in range(n):
        my_row = []
        for j in range(n):
            my_row.append(j)
        my_matrix.append(my_row)
    return my_matrix

print_matrix(create_matrix(3,3))