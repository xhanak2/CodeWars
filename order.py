def order(sentence):
    if len(sentence)>0:
        sentence+=' '
        count=0
        word=''
        words=['','','','','','','','','']
        for c in sentence:
            if (c!=' '): 
                word+=c
                if c in '123456789':index=int(c)
            else: words[index]=word;word='';count+=1
        finalstring=' '.join(words[:count+1])
        return finalstring[1:]
    else: return ""

    
print(order("To3to j1e tes4tovaci ve2ta"))
print(order(""))
