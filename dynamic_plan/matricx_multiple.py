matrix_p = [3,5,5,7,7,4]
total_matrix_count = int(len(matrix_p)/2)

def calculate_multi_time(first_matrix, last_matrix):
    if first_matrix < 0 or last_matrix > total_matrix_count-1:
        return False

    if first_matrix == last_matrix:
        return 0

def save_matrix_result():
    matrix_multi_count = [[0 for x in range(total_matrix_count)] for y in range(total_matrix_count)]

    count = 0
    for k in range(total_matrix_count):
        i = 0
        for j in range(i+count, total_matrix_count):
            if i == j:
                matrix_multi_count[i][j] = calculate_multi_time(i, j)
            
            if j > i:
                matrix_multi_count[i][j] = matrix_multi_count[i][i] \
                                        + matrix_multi_count[i+1][j] \
                                        + matrix_p[i] * matrix_p[i+1] * matrix_p[j+1]

                for k in range(i+1, j):
                    multi_count = matrix_multi_count[i][k] \
                                + matrix_multi_count[k+1][j] \
                                + matrix_p[i] * matrix_p[k+1] * matrix_p[j+1]

                    if multi_count < matrix_multi_count[i][j]:
                        matrix_multi_count[i][j] = multi_count
            i += 1
        count += 1
    print(matrix_multi_count)

if __name__ == '__main__':
    save_matrix_result()