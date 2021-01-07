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
