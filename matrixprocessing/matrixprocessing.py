def read_matrix(prompt=""):
    if prompt:
        print(prompt)
    else:
        print("Enter matrix size: ", end="")
    size_input = input().split()
    rows, cols = int(size_input[0]), int(size_input[1])
    print("Enter matrix:")
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(float, input().split())))
    return matrix, rows, cols

def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        formatted_row = []
        for x in row:
            if abs(x) == 0:
                x = 0.0
            formatted_row.append(str(round(x, 2) if x % 1 != 0 else int(x)))
        print(" ".join(formatted_row))

def add_matrices():
    matrix_a, rows_a, cols_a = read_matrix("Enter size of first matrix: ")
    matrix_b, rows_b, cols_b = read_matrix("Enter size of second matrix: ")

    if rows_a != rows_b or cols_a != cols_b:
        print("The operation cannot be performed.")
    else:
        result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(cols_a)] for i in range(rows_a)]
        print_matrix(result)

def multiply_by_constant():
    matrix, rows, cols = read_matrix()
    constant = float(input("Enter constant: "))
    result = [[element * constant for element in row] for row in matrix]
    print_matrix(result)

def multiply_matrices():
    matrix_a, rows_a, cols_a = read_matrix("Enter size of first matrix: ")
    matrix_b, rows_b, cols_b = read_matrix("Enter size of second matrix: ")

    if cols_a != rows_b:
        print("The operation cannot be performed.")
    else:
        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]
        print_matrix(result)

def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = input("Your choice: ")
    
    matrix, rows, cols = read_matrix()
    
    if choice == "1":
        result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    elif choice == "2":
        result = [[matrix[rows - 1 - j][cols - 1 - i] for j in range(rows)] for i in range(cols)]
    elif choice == "3":
        result = [row[::-1] for row in matrix]
    elif choice == "4":
        result = matrix[::-1]
    else:
        return

    print_matrix(result)

def get_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def calculate_determinant_recursive(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * calculate_determinant_recursive(get_minor(matrix, 0, c))
    return det

def calculate_determinant():
    matrix, rows, cols = read_matrix()
    if rows != cols:
        print("The operation cannot be performed.")
        return
    
    result = calculate_determinant_recursive(matrix)
    print("The result is:")
    print(result)

def inverse_matrix():
    matrix, rows, cols = read_matrix()
    if rows != cols:
        print("This matrix doesn't have an inverse.")
        return

    det = calculate_determinant_recursive(matrix)
    
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return

    if rows == 1:
        print_matrix([[1 / matrix[0][0]]])
        return

    cofactors = []
    for r in range(rows):
        cofactor_row = []
        for c in range(cols):
            minor = get_minor(matrix, r, c)
            cofactor_row.append(((-1) ** (r + c)) * calculate_determinant_recursive(minor))
        cofactors.append(cofactor_row)

    adjugate = [[cofactors[j][i] for j in range(rows)] for i in range(cols)]
    
    inverse = [[element / det for element in row] for row in adjugate]
    print_matrix(inverse)

def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            calculate_determinant()
        elif choice == "6":
            inverse_matrix()
        elif choice == "0":
            break
        print()

if __name__ == "__main__":
    main()
