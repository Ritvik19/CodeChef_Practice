import os
import sys

def birthdayCakeCandles(n, ar):
    return ar.count(max(ar))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()
