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

def gcd(a, b): 
    if a == 0 :
        return b 
     
    return gcd(b%a, a);

def pollard_rtho(n,maxStep = 10000000):
    f = lambda x : x ** 2 % n;
    x = 2;y = 2;d = 1;s = 1;
    while d == 1 and s <= maxStep:
        x = f(x);
        y = f(f(y));
        d = gcd(abs(x - y),n);
        s += 1;
        
    return d;

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

if __name__ == "__main__":
    print("Please enter an integer of the form n = p * q,\n which both p and q are prime integers:");
    print("The default maxmium step is 1000000,and make sure your prime factor is relative small");
    print("Of course you can increase the maxmium step in the loop,  but if the number factor is large,it won't run very efficiently.")
    n = int(input("The integer is:"));
    result = pollard_rtho(n);
    q = n // result;
    print(f"The result is:{result}");
    if result == 1:
        print("Factorization failed");
    elif isPrime(result) and isPrime(q):
        print(f'{n} = {result} * {q}');
    else:
        print("Something wrong...,the input number should be in the form of p * q")
    
    input("Press ENTER to exit:");


