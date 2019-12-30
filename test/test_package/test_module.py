'''
Created on Dec 26, 2019

@author: nicolaburri
'''

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
            print ('\t',f)
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
    return True  

num = 600851475143
grosste_primzahl = 0

#kanns dividiert werden, Rest 0?
for x in range(2, num//2):
    if num % x == 0:
        print(x, "--> kann dividiert werden")
        
#         #primCheck
#         primZahl = True
#         for y in range(2, x//2):
#             if x % y == 0:
#                 print(x, "--> ist KEINE Primzahl")
#                 primZahl = False
#                 break
            
        if is_prime(x):
            grosste_primzahl = x
            
print("Groesste Primzahl ist: ", grosste_primzahl)            
            
    
    
    