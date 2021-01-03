def SieveOfEratosthenes(n): 
      
 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]: 
            print (p) #Use print(p) for python 3 
  
# driver program 
n = 30
print ("Following are the prime numbers smaller"),  
#Use print("Following are the prime numbers smaller") for Python 3 
print ("than or equal to", n )
#Use print("than or equal to", n) for Python 3 
SieveOfEratosthenes(n) 