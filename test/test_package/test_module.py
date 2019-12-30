'''
Created on Dec 26, 2019

@author: nicolaburri
'''
num = 600851475143
grosste_primzahl = 0

#kanns dividiert werden, Rest 0?
for x in range(2, num):
    if num % x == 0:
        print(x, "--> kann dividiert werden")
        
        #primCheck
        primZahl = True
        for y in range(2, x):
            if x % y == 0:
                print(x, "--> ist KEINE Primzahl")
                primZahl = False
                break
            
        if primZahl:
            grosste_primzahl = x
            
print("Groesste Primzahl ist: ", grosste_primzahl)            
            
    
    
    