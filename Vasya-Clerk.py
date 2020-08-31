def tickets(people):
    c25=0
    c50=0
    output="YES"
    for c in people:
        if c==25:
            c25+=1
        if c==50:
            if c25>=1:
                c25-=1
                c50+=1
            else:
                output="NO"
        if c==100:
            if ((c25>=1)and(c50>=1)):
                c25-=1
                c50-=1
            elif ((c25>=3)and(c50<1)):
                c25-=3
            else:
                 output="NO"

    return output

print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25,25, 100]))


