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


if __name__ == '__main__':
    print('A generator of a sequence of uniformly distributed random numbers based on Lehmer\'s algorithm')

    N = 10
    # while True:
    #     tempN = input('Enter the number (N) of needed random numbers(DEFAULT N=' + str(N) + '):')
    #     if (tempN.isdigit()):
    #         N = tempN
    #         break
    #     elif (tempN == ''):
    #         break

    # while True:
    #     R0 = input('Enter (R0):')
    #     if (R0.isdigit()):
    #         R0=int(R0)
    #         break
    #
    # while True:
    #     a = input('Enter (a):')
    #     if (a.isdigit()):
    #         a=int(a)
    #         break
    #
    # while True:
    #     m = input('Enter (m):')
    #     if (m.isdigit()):
    #         m=int(m)
    #         break

    N = 10000
    R0 = 982489
    a = 981199
    m = 982931

    # 1 Random list ------------------------------------------------------------------------
    randomList = generateRandomNumbersList(R0, a, m, N)
    print('Random number list: ' + str(randomList))

    # 2 Histogram --------------------------------------------------------------
    plt.hist(randomList, bins=20, range=(0, 1), edgecolor='black', linewidth=1.2)
    # plt.show()

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

    

    # 4  The length of the period and segment of the aperiodicity ----------------------------------------------------
