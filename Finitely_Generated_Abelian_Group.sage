######
#The algorithm is based on the fundamental theorem of finitely generated abelian group
######

def simplifyAbelianGroup(n,M):
    #n is the cardinality of the generator set
    #M is the matrix of relathionship equations 
    #M should be a nxn SageMath matrix
    D = M.smith_form()[0];
    #Diagnal elements
    diagnal = [D[i][i] for i in range(n)];
    return AbelianGroup(diagnal);

######
#Test
#####
def main():
    print("Please enter the size of the set of generators of the abelian Group:")
    print('(It should be a positive integer)');
    n = int(input());
    print("Please enter a",n,"x",n,"matrix below:");
    print("One row at a time!");
    rows = [list(map(int,input().split())) for i in range(n)];
    M = Matrix(IntegerRing(),rows);
    print(simplifyAbelianGroup(n,M));
    return 0;

if __name__ == "__main__":
    main();


