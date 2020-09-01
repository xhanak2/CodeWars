def order(sentence):
    word=''
    words=[]
    for c in sentence:
        if c!=' ': word+=c
        else: words.append(word); print(word); word=''
    
    for word in words:
        print(word)


order("Toto je testovaci veta")
