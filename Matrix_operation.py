import numpy as np

def get_matrix(rows, cols, name="Matrix"):
    print(f"\nEnter elements of {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Please enter the correct number of elements!")
            return None
        matrix.append(row)
    return np.array(matrix)

def matrix_operations():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    A = get_matrix(rows, cols, "Matrix A")
    B = get_matrix(rows, cols, "Matrix B")

    if A is None or B is None:
        return

    print("\nMatrix A:\n", A)
    print("\nMatrix B:\n", B)

    print("\nSelect Operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose\n5. Determinant")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print("\nResult (A + B):\n", A + B)
    elif choice == 2:
        print("\nResult (A - B):\n", A - B)
    elif choice == 3:
        print("\nResult (A * B):\n", np.dot(A, B))
    elif choice == 4:
        print("\nTranspose of Matrix A:\n", A.T)
        print("\nTranspose of Matrix B:\n", B.T)
    elif choice == 5:
        if rows == cols:
            print("\nDeterminant of Matrix A:", np.linalg.det(A))
            print("\nDeterminant of Matrix B:", np.linalg.det(B))
        else:
            print("Determinant can only be calculated for square matrices!")
    else:
        print("Invalid choice!")

matrix_operations()

