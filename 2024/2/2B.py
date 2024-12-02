#working

def get_input(f):
    with open(f"2024/2/{f}") as fi:
        reports = [list(map(int,report.split())) for report in fi]
        return reports  


def test_report(report):
    test_one_a  = all(x < y for x, y in zip(report,report[1:]))
    test_one_b  = all(x > y for x,y in zip(report,report[1:]))
    test_one = test_one_a or test_one_b
    test_two   = all(abs(x - y) >= 1 for x, y in zip(report,report[1:]))
    test_three = all(abs(x - y) <= 3 for x, y in zip(report,report[1:]))
    return test_one and test_two and test_three

def report_tolerable(report):
    if test_report(report):
        return True
    else:
        for ix,_ in enumerate(report):
            report_x = report[:ix] + report[ix+1:]
            if test_report(report_x):
                return True
        return False

def main(f):
    reports = get_input(f)
    pass_counts = [report_tolerable(report) for report in reports]

    for i in zip(reports,pass_counts):
        print(i[0],i[1])
    print(sum(pass_counts))
    return sum(pass_counts)

#main('test.txt')
main('input.txt')