import random

#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    ###################################your code goes here#####################################
    original_z = z
    x0, x1 = 1, 0

    while z != 0:
        q, e, z = e // z, z, e % z
        x0, x1 = x1, x0 - q * x1
        

    # d is the modular inverse of e mod z
    d = x0 % original_z
    return d

    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    n = p * q
    z = (p - 1) * (q - 1)

    # Choose e such that 1 < e < z and gcd(e, z) == 1
    e = 3  # Common choice for e
    while gcd(e, z) != 1:
        e += 2  # Increment by 2 to ensure e is odd

    # Calculate d using the Extended Euclidean Algorithm
    d = get_d(e, z)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!

    e, n = pk
    # Convert character to number (ASCII)
    plain_num = ord(plaintext)
    # The encrypted version of plaintext
    cipher = pow(plain_num, e, n)
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    
    d, n = pk
    # Decrypt the ciphertext to get the plain number
    plain_num = pow(ciphertext, d, n)
    # Convert number back to character
    plain = chr(plain_num)
    
    return ''.join(plain)

