#works

def get_input(f):
    with open(f"2024/2/{f}") as fi:
        reports = [list(map(int,report.split())) for report in fi]
        return reports  


def test_report(report):
    test_one   = all(x < y for x, y in zip(report,report[1:])) or all(x > y for x,y in zip(report,report[1:]))
    test_two   = all(abs(x - y) >= 1 for x, y in zip(report,report[1:]))
    test_three = all(abs(x - y) <= 3 for x, y in zip(report,report[1:]))
    return all([test_one,test_two,test_three])

def main(f):
    reports = get_input(f)
    pass_counts = [test_report(report) for report in reports]

    for i in zip(reports,pass_counts):
        print(i[0],i[1])
    print(sum(pass_counts))
    return sum(pass_counts)

#main('test.txt')
main('input.txt')