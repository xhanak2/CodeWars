def disemvowel(string):
    result=''
    for c in string:
        if c not in 'aeiouyAEIOUY': 
            result+=c
    string=result
    return string

print(disemvowel("Toto je test TAKY TOTO"))
