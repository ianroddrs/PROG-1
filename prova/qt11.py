r = 1
k = 1
while k <= 10:
    k += 1
    r += k
print(r)

def f(k=1,r=1):
    if k <= 10: 
        k += 1
        r += k 
    else: 
        return r
    return f(k,r)

print(f())