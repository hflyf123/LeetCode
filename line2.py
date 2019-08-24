import sys, math
from functools import reduce


def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    n, m = 2, 2
    for i, v in enumerate(argv):
        print("argv[{0}]: {1}".format(i, v))

        if i == 0:
            n = int(v)
        elif i == 1:
            m = int(v)


    # if m >= n:
    #     if m >= 4:
    #         result = "Factorial"
    #     else:
    #         result = "Exponential"
    # else:
    #     dict_a = {2: 4}
    #     dict_b = {2: 2}
    #     for j in range(3, m+1):
    #         dict_a[j] = 2 * dict_a[j-1]
    #         dict_b[j] = j * dict_b[j-1]
    #         while dict_a[j] < dict_b[j]:
    #             result = "Factorial"
        # print(dict_b)
        # exponent_result = pow(2, n)
        # factorial_result = math.sqrt(2*math.pi*m)*pow(m/math.e, m)
        # print(factorial_result)
        # if exponent_result > factorial_result:
        #     result = "Exponential"
        # else:
        #     result = "Factorial"
    print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
