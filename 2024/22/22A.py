#working

def get_input(f):
    with open(f"2024/22/{f}") as fi:
        numbers = [int(x) for x in fi.readlines()]
        return numbers

def prune(n):
    #modul0
    return n % 16777216

def mix(n,n_):
    #xor
    return n ^ n_ 


def foo(n,times,_score = 0):
    while times > 0:
        #print(f"{n = }")
        n_ = n << 6 #equiv of x 64
        n_1 = mix(n,n_)
        n_2 = prune(n_1)
        n_3 = n_2 >> 5 #equiv of floor division 32
        n_4 = mix(n_2,n_3)
        n_5 = prune(n_4)
        n_6 = n_5 << 11 #equiv of x 2048
        n_7 =  mix(n_5,n_6)
        n_8 = prune(n_7)
        times -= 1
        n = n_8
    return n

def main(f,times):
    score = 0
    numbers = get_input(f)
    for n in numbers:
        n = foo(n,times)
        print(f"{n = }")
        score += n
    print(f"{n = }")

    print(f"final: {score = }")
    return 

#main("test.txt",2000)
#main("test1.txt",10)
main("input.txt",2000)