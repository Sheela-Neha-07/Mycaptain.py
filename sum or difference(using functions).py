# 1 indicates sum 
#2 indicates difference
def sum_difference(a: int, b: int, c: int) -> int:
    if c==1:
        result= a+b 
        return result
    else:
        result= a-b
        return result
        
print(sum_difference(5637,4,1))
print(sum_difference(213,456,2))
