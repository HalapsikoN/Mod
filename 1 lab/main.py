import math
import matplotlib.pyplot as plt


def generateR1(R0, a, m):
    return R0 * a % m


def generateRandomNumbersList(R0, a, m, N):
    result = []
    for i in range(0, N):
        R0 = generateR1(R0, a, m)
        result.append(R0 / m)
    return result


def countDespersion(array, mathematicalExpectation):
    tempArray = []
    for i in array:
        tempArray.append(pow(i - mathematicalExpectation, 2))
    return sum(tempArray) / len(tempArray)


def countKPairs(array):
    k = 0
    for i in range(0, len(array), 2):
        if (pow(array[i], 2) + pow(array[i + 1], 2)) < 1:
            k += 1
    return k

def findPeriod(array):
    xV=array[-1]
    i1=0
    while i1<len(array) and array[i1]!=xV:
        i1+=1
    i2=i1+1
    while i2<len(array) and array[i2]!=xV:
        i2+=1

    if not (i1<i2 and i2<len(array)):
        return 0
    else:
        return i2-i1


def findAperiodicitySegmentLength(array, period):
    if period==0:
        return math.inf
    i3=0
    while array[i3]!=array[period+i3]:
        if period+i3==len(array):
            return math.inf
        i3+=1
    return i3+period

if __name__ == '__main__':
    print('A generator of a sequence of uniformly distributed random numbers based on Lehmer\'s algorithm')

    N = 1000000
    while True:
        tempN = input('Enter the number (N) of needed random numbers(DEFAULT N=' + str(N) + '):')
        if (tempN.isdigit()):
            N = int(tempN)
            break
        elif (tempN == ''):
            break

    while True:
        R0 = input('Enter (R0):')
        if (R0.isdigit()):
            R0=int(R0)
            break

    while True:
        a = input('Enter (a):')
        if (a.isdigit()):
            a=int(a)
            break

    while True:
        m = input('Enter (m):')
        if (m.isdigit() and a<int(m)):
            m=int(m)
            break

    # N = 10000
    # R0 = 982489
    # a = 981199
    # m = 982931
    # N = 1000000
    # R0 = 1
    # a = 134279
    # m = 313107


    # 1 Random list ------------------------------------------------------------------------
    randomList = generateRandomNumbersList(R0, a, m, N)
    print('The part of random number list: ' + str(randomList[0:10]))

    # 2 Histogram --------------------------------------------------------------
    print()
    plt.hist(randomList, bins=20, range=(0, 1), edgecolor='black', linewidth=1.2)
    plt.show()

    # mathematical expectation
    mathematicalExpectation = sum(randomList) / len(randomList)
    # dispersion
    dispersion = countDespersion(randomList, mathematicalExpectation)
    # standard deviation
    standardDeviation = math.sqrt(dispersion)
    print('Mathematical expectation: (' + str(mathematicalExpectation) + ')')
    print('Dispersion: (' + str(dispersion) + ')')
    print('Standard deviation: (' + str(standardDeviation) + ')')

    # 3  The uniformity of the sequence by indirect signs --------------------------------------------------------------
    print()
    print('The uniformity of the sequence by indirect signs: ('+ str(2*countKPairs(randomList)/N)+') => ('+str(math.pi/4)+')')

    # 4  The length of the period and segment of the aperiodicity ----------------------------------------------------
    print()

    period=findPeriod(randomList)
    print('The length of the period: ('+str(period)+')')
    aperiodicitySegmentLength=findAperiodicitySegmentLength(randomList, period)
    print('The length of segment of the aperiodicity: ('+str(aperiodicitySegmentLength if aperiodicitySegmentLength!=math.inf else '>'+str(N))+')')

