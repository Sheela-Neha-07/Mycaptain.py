# 1 indicates sum 
#2 indicates difference
#Enter the sum or difference as c
a,b,c= map(int,input().split())
if c==1:
    result= a+b 
    print(result)
else:
    result = a-b
    print(result)
