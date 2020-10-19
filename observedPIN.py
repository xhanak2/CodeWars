def get_pins(observed):
    opt=[]
    o=1
    pocet=1
    result=[]
    options = dict({'1': ['1','2','4'], 
                    '2': ['1','2','3','5'], 
                    '3': ['2','3','6'],
                    '4': ['1','4','5','7'],
                    '5': ['2','4','5','6','8'],
                    '6': ['3','5','6','9'],
                    '7': ['4','7','8'],
                    '8': ['5','7','8','9','0'],
                    '9': ['6','8','9'],
                    '0': ['0','8']})
    for n in str(observed):
        pocet=pocet*len(options[n])
        opt.append(options[n])

    for n in range(pocet):result.append((''))

    for o in opt:
        for n in range(pocet):
            result[n]+=o[n%len(o)]
        result.sort()

    return result

get_pins(123)
#get_pins(111)

# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘