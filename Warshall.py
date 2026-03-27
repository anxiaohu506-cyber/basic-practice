def warshall_algorithm(relation_matrix):
    n = len(relation_matrix)
    closure = [row[:] for row in relation_matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])
    return closure
def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
if __name__ == "__main__":
    R = [
        [0, 1, 1],
        [0, 0, 1],
        [0, 1, 0],
    ]
    print("原关系矩阵 R:")
    print_matrix(R)
    closure = warshall_algorithm(R)
    print("\n传递闭包矩阵 R*:")
    print_matrix(closure)