import re

def mapToDigits(e):
    CHARS_TO_MAP = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for n in range(9):
        e = e.replace(CHARS_TO_MAP[n], f"{CHARS_TO_MAP[n]}{n+1}{CHARS_TO_MAP[n]}")
    return e

def findNumbers(e):
    e = mapToDigits(e)
    digits = re.findall(r"[\d]", e)
    return int(f"{digits[0]}{digits[-1]}")

def sumOfCalibNums(calibDoc):
    toRet = 0
    for e in calibDoc:
        print(findNumbers(e))
        toRet += findNumbers(e)
    return toRet

if __name__ == "__main__":
    #CALIB_DOC = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
    with open('2-input') as t:
        CALIB_DOC = t.readlines()
    res = sumOfCalibNums(CALIB_DOC)
    print(res)