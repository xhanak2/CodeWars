def solution(n):
    # TODO convert int to roman string
    n1=n
    out=''
    while n1 >= 1000:out+='M';n1-=1000
    while n1 >= 900:out+='CM';n1-=900
    while n1 >= 500:out+='D';n1-=500
    while n1 >= 400:out+='CD';n1-=400
    while n1 >= 100:out+='C';n1-=100
    while n1 >= 90:out+='XC';n1-=90
    while n1 >= 50:out+='L';n1-=50
    while n1 >= 40:out+='XL';n1-=40
    while n1 >= 10:out+='X';n1-=10
    while n1 >= 9:out+='IX';n1-=9
    while n1 >= 5:out+='V';n1-=5
    while n1 >= 4:out+='IV';n1-=4
    while n1 >= 1:out+='I';n1-=1
    return out

print(solution(90))
