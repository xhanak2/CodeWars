def printer_error(s):
    error=0
    for c in s:
        if c not in '[a-m]':
            error+=1
    return (str(error)+"/"+str(len(s)))

print(printer_error("aaddfgdfgfjhawertwretdffxx"))
