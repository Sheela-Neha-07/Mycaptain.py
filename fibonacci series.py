no_of_terms= int(input())
term= 0
next_term= 1
for i in range (0,no_of_terms+1):
    if i<=1:
        n= i 
    else:
        n= term+next_term
        term= next_term
        next_term= n 
    print(n)
    
    
