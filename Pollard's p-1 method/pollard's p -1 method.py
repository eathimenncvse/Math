from random import randint;

# Fast modular 
def powerMod(x, y, p): 
      
    # Initialize result 
    res = 1;  
    x = x % p;  
    while (y > 0): 
          
        # If y is odd, multiply 
        # x with result 
        if (y & 1): 
            res = (res * x) % p; 
  
        # y must be even now 
        y = y>>1; # y = y/2 
        x = (x * x) % p; 
      
    return res; 


# Euclidean algorithm
def gcd(a, b): 
    if a == 0 :
        return b 
     
    return gcd(b%a, a);

# Miller - Rabin primality test    
def miillerTest(d, n): 
    
    a = 2 + randint(1, n - 4); 
    x = powerMod(a, d, n); 
  
    if (x == 1 or x == n - 1): 
        return True; 

    while (d != n - 1): 
        x = (x * x) % n; 
        d *= 2; 
  
        if (x == 1): 
            return False; 
        if (x == n - 1): 
            return True; 

    return False; 
  
def isPrime( n, k = 5): 
      
    # Corner cases 
    if (n <= 1 or n == 4): 
        return False; 
    if (n <= 3): 
        return True; 
  
    # Find r such that n =  
    # 2^d * r + 1 for some r >= 1 
    d = n - 1; 
    while (d % 2 == 0): 
        d //= 2; 
  
    # Iterate given nber of 'k' times 
    for i in range(k): 
        if (miillerTest(d, n) == False): 
            return False; 
  
    return True; 

# Pollard's p -1 method
def pollard2(n,B = 100000,base = 2):
    if isPrime(n):
        return n;
    d = gcd(base,n);
    s = 2;
    x = base;
    while d == 1 and s <= B - 1:
        x = powerMod(x,s,n);
        d = gcd(x - 1,n);
        if d > 1 and d < n:
            return d;
        s += 1;
        
    return d;

if __name__ == "__main__":
    print("Please enter an integer of the form n = p * q,\n which both p and q are prime integers:");
    print("The default upperbound is 100000,so make sure p -1 or q - 1 is a 100000- smooth integer");
    n = int(input("The integer is:"));
    result = pollard2(n);
    q = n // result;
    print("The result is:",result);
    if result == 1:
        print("Factorization failed");
    elif isPrime(result) and isPrime(q):
        print(n,"=",result," * ",q);
    else:
        print("Something wrong...,the input number should be in the form of p * q")
