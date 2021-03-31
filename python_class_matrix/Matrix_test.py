from Matrix import *
from random import randint
import numpy as np

def randomMatrixList(n,m):
    List = [randint(-50,50)/randint(1,100) for k in range(n * m)];
    List_Matrix = [];
    for i in range(n):
        row = List[i * m :i * m + m];
        List_Matrix.append(row);
    return List_Matrix;
def randomList(n):
    b = [randint(-50,50) / randint(1,100) for k in range(n)];
    return b;

if __name__ == "__main__":
    print("====Test 1:Determinant====");
    n = int(input("Please input an positive integer >= 2:"));
    List = randomMatrixList(n,n);
    A = Matrix(List);
    print("Matrix in 'Matrix':\n");
    A.show();
    B = np.matrix(List);
    print("Matrix in 'numpy':\n");
    print(B);
    D1 = det(A);
    D2 = np.linalg.det(B);
    print(f"Determinnat of matrix in 'Matrix' is :{D1}\n");
    print(f"Determinnat of matrix in 'numpy' is :{D2}\n");
    
    print("===========================");
    
    print("====Test 2:Rank====");
    print("Please input two positive integer,for row and col:");
    n1 = int(input().strip());
    m1 = int(input().strip());
    List1 = randomMatrixList(n1,m1);
    A1 = Matrix(List1);
    print("Matrix in 'Matrix':\n");
    A1.show();
    B1 = np.matrix(List1);
    print("Matrix in 'numpy':\n");
    print(B1);
    print("Rank in 'Matrix' is:");
    print(A1.rank);
    print("Rank in 'numpy' is:");
    print(np.linalg.matrix_rank(B1));
    
    print("============================");
    
    print("====Test 3:Linear Equation====");
    print("Please input two positive integer,for row and col:");
    n2 = int(input().strip());
    m2 = int(input().strip());
    if n2 > m2:
        print("Be careful!n_row > n_col,it's very likely that your randomly generated eqation has no solution!")
        print("Since it's very likely that rank(A) != rank(A|b)");
    List2 = randomMatrixList(n2,m2);
    b = randomList(n2);
    A2 = Matrix(List2);
    print(f"A = ");
    A.show();
    print(f"b = ");
    print(b);
    print("Solving equations A * x = b .....\n");
    result = linSolve(A2,b);
    def verification(x):
        x = x.copy();
        x = Matrix([x]).transpose;
        b1 = A2 * x;
        b2 = [];
        for i in range(n2):
            b2.append(b1[i][0]);
        error = 0;
        for i in range(n2):
            error += abs(b2[i] - b[i]);
        return error;
    print(result);
    if str(result)[0] == "(":
        x,basis,null = result;
    else:
        x = result;

    print(f"x = {x}");
    print("Verification (A * x = b)?...");
    bound = 10 ** (-10);
    error = verification(x);
    print(f"error = {error}");
    if error < m2 *bound:
        print("\n");
        print("The solution is correct!");
    else:
        print("The solution is wrong!");
        
    if str(result)[0] == "(":
        print("The nullspace is :\n");
        print("< ");
        for base in basis:
            print(base);
        print(">");
        vectors = [];
        for base in basis:
            c = randint(-50,50);
            vector = [base[j] * c for j in range(m2)];
            vectors.append(vector);
        
        vectors.append(x);
        x2 = [0] * m2;
        for vector in vectors:
                x2 = [x2[j] + vector[j] for j in range(m2)];
        print("\n");
        print("Verifying if x' = c1 * v1 + c2 * v2 ... + x,{v1,v2,..} \in kernal(A)");
        print("then is A * x' = b? \n");
        error2 = verification(x2);
        print(f"error = {error2}");
        if error2 < m2 * bound:
            print("The basis is correct!");
        else:
            print("The basis is wrong!");
            
        input("Press any key to exit.")
            