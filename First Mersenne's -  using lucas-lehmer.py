import math


def lucas_lehmer(pwr):
    NumberToBeChecked = 2 ** pwr - 1
  
    nextVal = 4 % NumberToBeChecked 

    for i in range(1, pwr - 1):
        nextVal = (nextVal * nextVal - 2) % NumberToBeChecked
    if (nextVal == 0):
        return True
    else:
        return False

def main():
    n = [2, 3, 5, 7, 13, 17, 19, 31, 67, 127,257]
    for i in n:
        pwr = i
        NumberToBeChecked = 2 ** pwr - 1
        firstHundred = []
        if lucas_lehmer(NumberToBeChecked):
            print(NumberToBeChecked, 'is Prime.')
            firstHundred.append(NumberToBeChecked)
        else:
            print(NumberToBeChecked, 'is not Prime')


main()
