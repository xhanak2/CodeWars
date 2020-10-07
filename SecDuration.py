def format_duration(seconds):
    #your code here
    sec=seconds
    y=0;d=0;h=0;m=0;s=0;comp=0
    out=''

    if sec==0:out+='now'

    while sec>=31536000:sec-=31536000;y+=1
    while sec>=86400:sec-=86400;d+=1
    while sec>=3600:sec-=3600;h+=1
    while sec>=60:sec-=60;m+=1
    while sec>=1:sec-=1;s+=1

    if y>0:comp+=1
    if d>0:comp+=1
    if h>0:comp+=1
    if m>0:comp+=1
    if s>0:comp+=1

    if y>=2:out+=str(y);out+=' years';comp-=1
    if y==1:out+=str(y);out+=' year';comp-=1
    if (comp>=2)and(y>=1):out+=', '
    if (comp==1)and(y>=1):out+=' and '

    if d>=2:out+=str(d);out+=' days';comp-=1 
    if d==1:out+=str(d);out+=' day';comp-=1
    if (comp>=2)and(d>=1):out+=', '
    if (comp==1)and(d>=1):out+=' and '

    if h>=2:out+=str(h);out+=' hours';comp-=1
    if h==1:out+=str(h);out+=' hour';comp-=1
    if (comp>=2)and(h>=1):out+=', '
    if (comp==1)and(h>=1):out+=' and '

    if m>=2:out+=str(m);out+=' minutes';comp-=1
    if m==1:out+=str(m);out+=' minute';comp-=1
    if (comp>=2)and(m>=1):out+=', '
    if (comp==1)and(m>=1):out+=' and '

    if s>=2:out+=str(s);out+=' seconds';comp-=1
    if s==1:out+=str(s);out+=' second';comp-=1

    return out
