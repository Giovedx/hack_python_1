"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    
    i = 0
    result = [1,2,3]
    result = []
    
    while i < 3:
        i += 1
        result.append(i)
        result.append('@')   
    
    return result  

final = fn_hack_9()
print(final)


