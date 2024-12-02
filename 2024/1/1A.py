#works


def get_input(f):
    with open(f"2024/1/{f}") as fi:
        a_list = []
        b_list = []
        for i in fi.readlines():
            #print("stripping", i.split())
            a, b = i.split()
            a_list.append(int(a))
            b_list.append(int(b))
        #print(a_list)
        #print(b_list)
        return a_list, b_list

def main(f):
    a_list, b_list = get_input(f)
    a_list, b_list = sorted(a_list), sorted(b_list)
    res = 0
    for i in zip(a_list,b_list):

        res+= abs(i[0]-i[1])
    print(res)
    return res

#main('test.txt')
main('input.txt')