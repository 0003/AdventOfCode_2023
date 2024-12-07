#works
from itertools import product

operators = ("+","*","||")

def gen_combos(operators : tuple, operator_spaces_count : int):
    for combo in product(operators,repeat=operator_spaces_count):
        yield combo

def test_equation(test_value,numbers,operator_combo):
    eqaution_result = numbers[0]
    for i, n in enumerate(numbers[1:]):
        operator = operator_combo[i]
        if operator == "+":
            eqaution_result += n
        elif operator == "*":
            eqaution_result *= n
        elif operator == "||":
            eqaution_result = int(str(eqaution_result) + str(n))
    return test_value == eqaution_result


def get_input(f):
    with open(f"2024/7/{f}") as fi:
        calibrations = []
        for e in  fi:
            #190: 10 19
            e_ = e.split(":")
            test_value = int(e_[0])
            numbers = [int(x) for x in e_[1].strip().split(" ")]
            calibrations.append( (test_value,numbers))
    
    return calibrations

def main(f):
    calibrations = get_input(f)
    print(calibrations)

    score = 0
    for e in calibrations:
        test_value = e[0]
        numbers = e[1]
        operator_spaces_count = len(numbers) - 1
        for operator_combo in  gen_combos(operators, operator_spaces_count):
            if test_equation(test_value,numbers,operator_combo):
                score += test_value
                break
    print (f"Final Score = {score}")

#main("test.txt")
main("input.txt")
