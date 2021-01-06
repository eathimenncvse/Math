from functools import reduce
from itertools import product

def expList(base,List):
    return [base ** x for x in List];
    
def deleteBraket(List):
    #To string
    string = str(List);
    #Delete all the brakets
    string = ''.join([s for s in string if s not in ['(',')','[',']']]);
    #Seperate numbers 
    stringNumberList = string.split(',');
    return [int(s) for s in stringNumberList];

def AbelianGroups(n):
    #Get prime factors of integer n
    factorsList = list(factor(n));
    #Exponets of primes
    primeIndex = [index for prime,index in factorsList];
    #Primes
    primes = [prime for prime,index in factorsList];
    #Total number of different prime numbers in n
    primeN = len(primes);
    #Integer partitions of exponents of primes 
    partitionsIndex = [list(Partitions(x)) for x in primeIndex];
    #How many different abelian groups of order n:
    totalNumber = reduce((lambda x,y:x * y),[len(x) for x in partitionsIndex]);
    
    ##################################
    #Now we need to figure out exact structures of these abelian groups
    ##################################
    
    #For each prime number in n,for example when prime is 2
    #If prime index of 2 is 3 ,thus 2^3 | n 
    #The partitions of index 3 is {{3},{2,1},{1,1,1}}
    #Then we can divide 2^3 into {{8},{4,2},{2,2,2}}
    #So for each prime in primes ,and each partiotions in partitionsIndex,we need to do the function 
    #expList(prime,partitions)
    primePartitions = [[expList(primes[t],partitionsIndex[t][k]) for k in range(len(partitionsIndex[t]))] for t in range(primeN)];
    #The set of all distinct abelian groups of order n is in fact ,
    #the Cartesian product of sets of all abelian groups of order p^k
    
    #We should also delete the brakets in the result
    return [totalNumber,[deleteBraket(group) for group in  list(reduce(lambda x,y:product(x,y),primePartitions))]];
    
#####################
#TEST
####################
def main():
    print("Please enter an positive integer below:");
    n = int(input());
    result = AbelianGroups(n);
    print("The total number of different abelian groups of order ",n,"is:");
    print(result[0]);
    print("Show all the grous?");
    print('Enter Y or N below:');
    choice = input();
    if choice == 'Y':
        print(result[1]);
    return 0;
if __name__ == "__main__":
    main();
