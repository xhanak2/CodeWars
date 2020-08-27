def DNA_strand(dna):
    # code here
    result=''
    for c in dna:
        if c=='A':
            result+='T'
        elif c=='T':
            result+='A'
        elif c=='C': 
            result+='G'
        elif c=='G':
            result+='C'
    return result

test='CATA'

print(test)
print(DNA_strand(test))
