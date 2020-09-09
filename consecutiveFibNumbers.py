def productFib(prod):
    fib=[]
    result=[]
    fib.append(0)
    fib.append(1)
    index=1
    while (fib[index-1]*fib[index])<prod:
        fib.append(fib[index-1]+fib[index])
        index+=1
    result.append(fib[index-1])
    result.append(fib[index])
    if result[0]*result[1]==prod:
        result.append(True)
    else: result.append(False)
    return result

print(productFib(1871))
