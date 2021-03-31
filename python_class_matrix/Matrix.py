from functools import reduce
def dot_product(u, v):
    return sum([i * j for i,j in zip(u,v)]);

def multiplication(M, N):
    res = None;
    if type(M) == type(N) == Matrix and M.ncol == N.nrow:
        res = Matrix([[0 for i in range(N.ncol)] for j in range(M.nrow)]);
        for i in range(M.nrow):
            for j in range(N.ncol):
                res[i][j] = dot_product(M[i], [N[k][j] for k in range(N.nrow)]);
    elif type(M) == int or type(M) == float:
        res = Matrix([[N[j][i] for i in range(N.ncol)] for j in range(N.nrow)]);
        for i in range(res.nrow):
            for j in range(res.ncol):
                res[i][j] *= M;
    elif type(N)==int or type(N)==float:
        res = Matrix([[M[j][i] for i in range(M.ncol)] for j in range(M.nrow)]);
        for i in range(res.nrow):
            for j in range(res.ncol):
                res[i][j] *= N;      
    else:
        raise TypeError("M and N should be either a compatible Matrix object, or a constant");
    
    return res;

def matrixCopy(M):
    m = M.ncol;
    n = M.nrow;
    N = [];
    for i in range(n):
        row = [M[i][j] for j in range(m)];
        N.append(row);
    return Matrix(N);

def gauss(M):
    # assert type(M) == Matrix,"The input should be a Matrix!";
    bound = 10 ** (-10);
    M = matrixCopy(M); #Otherwise the variable M will be changed
    n = M.nrow;
    m = M.ncol;
    t = min(m,n);
    sign = 1;
    h = -1;
    l = -1;
    for k in range(t):
        h += 1;
        if h == n:
            break;
        absMax = 0;
        while  absMax < bound and l < m - 1:
            l += 1; 
            pivots = [abs(M[i][l]) for i in range(h,n)];
            i_max = pivots.index(max(pivots)) + h; #index of the row of the matrix M 
            absMax = abs(M[i_max][l]); #Check for signular matrix
            
        if i_max > h:    
            M[h],M[i_max] = M[i_max],M[h]; # swap rows
            sign *= -1;
        if h + 1 < n and l + 1 < m:
            for i in range(h + 1,n):
                f = M[i][l] / M[h][l];
                for j in range(l + 1,m):
                    M[i][j] -= M[h][j] * f;    
                M[i][l] = 0; #Fill lower triangular matrix with 0
    #rank
    r = 0;
    for k in range(t):
        if abs(M[k][k]) > bound:
            r += 1;
        
    if r < n:
        for h in range(r,n):
            for l in range(m):
                M[h][l] = 0;
                
    return M,sign,r;

def linSolve(M,b):
    M = matrixCopy(M);
    m = M.ncol;
    n = M.nrow;    
    assert n == len(b);
    r1 = M.rank;
    for i in range(n):
        M[i].append(b[i]);
    
    M2 = Matrix([M[i] for i in range(n)]);
    M2 = gauss(M)[0];
    r2 = M2.rank;
    assert r1 == r2,"No soluion!";
    r = r1 - 1;
    #Back substitution
    for k in range(r,0,-1):
        for i in range(k - 1,-1,-1):
            f = M2[i][k] / M2[k][k];
            for j in range(k + 1,m + 1):
                M2[i][j] -= M2[k][j] * f;
            M2[i][k] = 0;
    M3 = [];
    for k in range(n):
        row = [M2[k][j] / M2[k][k]  for j in range(m + 1)];
        M3.append(row);
        
    x = [];
    for i in range(n):
        x.append(M3[i][m]);
        
    if r1 == max(m,n):
        return x;
    
    elif r1 < m:
        r_n = m - r1;# dimention of the null space
        basis = [];
        for k in range(r1,m):
            base = [-M3[i][k] for i in range(n)] + [0] * r_n;
            base[k] = 1;
            basis.append(base);
            
        x = x + [0] * (m - r1);
        return x,basis,r_n;

def det(M):
    M,sign= gauss(M)[0:2];
    return sign * reduce(lambda x,y:x * y,M.diag);

class Matrix(list):
    #Class Matrix is based on the Class list
    def __init__(self, the_list):
        super().__init__(the_list)

    @property
    def nrow(self):
        return len(self)

    @property
    def ncol(self):
        return len(self[0])

    def dim(self):
        return self.nrow, self.ncol

    def __add__(self, M):
        return Matrix(
            [[sum(x) for x in zip(*rows)] for rows in zip(self, M)])

    def __mul__(self, M):
        return multiplication(self, M)

    def __rmul__(self, M):
        return multiplication(M, self)

    def add_rows(self, rows):
        super().extend(rows)

    def append(self, row):
        try:
            sum(row)  # Check if all numbers
            if len(row) < self.ncol:
                row.extend([0] * (self.ncol - len(row)))
            elif len(row) > self.ncol:
                [row.pop() for i in range(len(row) - self.ncol)]
            super().append(row)
        except:
            raise AssertionError('Elements in row must be mumbers')
    @property
    def diag(self):
        assert self.ncol == self.nrow;
        n = self.ncol;
        return [self[k][k] for k in range(n)];

    @property
    def transpose(self):
        return Matrix(map(list, zip(*self)))
    @property
    def rank(self):
        return gauss(self)[2];
    
    def show(self,precision_level = 5):
        print("Printing matrix: ");
        maxLen = precision_level + 3;
        List_Matrix = [];
        #Ensure that the output matrix is neat
        for row in self:
            row2 = list(map(lambda x:str(round(x,precision_level)),row)); 
            List_Matrix.append(row2);
        for row2 in List_Matrix:
            for i in range(len(row2)):
                element = row2[i];
                Length = len(element);
                element += ' ' * (maxLen - Length);
                row2[i] = element;
            print(row2);