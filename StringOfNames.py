def namelist(names):
    result1=[]
    result2=[]
    result3=""
    last=""
    if len(names)>0:
        for n in names:
            result1.append(n['name'])
        last=result1.pop()
        result2= ", ".join(result1)
        if len(result1)>0:result3=result2 + " & " + last
        else: result3=last
        return result3
    else:return ""



print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
print(namelist([ {'name': 'Bart'} ]))
print(namelist([]))