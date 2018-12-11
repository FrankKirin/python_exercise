matrix_p = [30, 35, 35, 15, 15, 5, 5, 10, 10, 20, 20, 25]
# matrix_p = [10, 100, 100, 5, 5, 50]

total_matrix_count = int(len(matrix_p)/2)

def calculate_multi_time(first_matrix, last_matrix):
    if first_matrix < 0 or last_matrix > total_matrix_count-1:
        return False

    if first_matrix == last_matrix:
        return 0


def save_matrix_result():
    matrix_multi_count = [[0 for x in range(total_matrix_count)] for y in range(total_matrix_count)]

    for count in range(0, total_matrix_count):
        for i in range(0, total_matrix_count-count):
            j = i+count
            if i==j:
                matrix_multi_count[i][j] = calculate_multi_time(i, j)

            if j>i :
                matrix_multi_count[i][j] = matrix_multi_count[i][i] \
                                        + matrix_multi_count[i+1][j] \
                                        + matrix_p[i*2] * matrix_p[2*i+1] * matrix_p[2*j+1]

                for k in range(i+1, j):
                    multi_count = matrix_multi_count[i][k] \
                                + matrix_multi_count[k+1][j] \
                                + matrix_p[2*i] * matrix_p[2*k+1] * matrix_p[2*j+1]

                    if multi_count < matrix_multi_count[i][j]:
                        matrix_multi_count[i][j] = multi_count

    print(matrix_multi_count)
    print("The count of minium multip count is", matrix_multi_count[0][total_matrix_count-1])


if __name__ == '__main__':
    save_matrix_result()