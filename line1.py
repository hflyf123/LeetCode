import sys


def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    n, k, q = 2, 1, 1  # init
    for i, v in enumerate(argv):
        # print("argv[{0}]: {1}".format(i, v))
        # get arguments
        if i == 0:
            n = int(v)
        elif i == 1:
            k = int(v)
        else:
            q = int(v)
    # init cups list
    sets = [0] * n
    sets[0] = 1
    # Determine the number of executions
    while k:
        one_movement(q, sets)
        k -= 1
    answer = sets.index(1) + 1
    print(answer)


def one_movement(q, sets):
    """
    After the q times operation of the Cup list
    :param q: swap times
    :param sets: cups list
    :return: none
    """
    cur = 0
    while q:
        if cur + 1 == len(sets):
            sets[cur], sets[(cur + 1) % len(sets)] = sets[(cur + 1) % len(sets)], sets[cur]
            q -= 1
            cur = (cur + 1) % len(sets)
            continue
        sets[cur], sets[cur + 1] = sets[cur + 1], sets[cur]
        cur += 1
        q -= 1


if __name__ == '__main__':
    main(sys.argv[1:])
