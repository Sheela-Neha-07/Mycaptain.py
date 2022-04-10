numbers= list(map(int,input().split()))
b= len(numbers)
b= b-1
for i in range(b):
    c= numbers[i]
    if c>=0:
        print (c,end=' ')
