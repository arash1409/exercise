def main():
    n = int(input()) #tedad soalat
    key = input() #key soalat
    pasokh_barg = int(input()) #tedad paskh barg
    dic = creat_data(pasokh_barg, key, n)
    for value in score(dic).values():
        print(f'{value}')


def test_answer(inp):
    key, javab_test = inp[0], inp[1]
    li = []
    li[:0] = javab_test
    key = key.upper()
    if li.count('#') > 1:
        return False
    elif li.count('#') < 1:
        return '$$'
    elif key == 'A' and li[0] == '#':
        return True
    elif key == 'B' and li[1] == '#':
        return True
    elif key == 'C' and li[2] == '#':
        return True
    elif key == 'D' and li[3] == '#':
        return True
    else:
        return False


def creat_data(pasokh_barg, key, num_of_q):
    dic = {}
    for i in range(pasokh_barg):
        dic_1 = {} 
        for j in range(num_of_q):
            javab_test = input()
            dic_1[j] = [key[j], javab_test]
        dic[i] = dic_1
    return (dic)

def score(dic):
    scores = {}
    pasokh_barg = dic.keys()
    for pb in pasokh_barg:
        ca, wa = 0, 0
        for j in dic[pb].keys():
            if test_answer(dic[pb][j]) is True:
                ca += 1
            elif test_answer(dic[pb][j]) is False:
                wa += 1
            else:
                continue
        scores[pb] = (3 * ca - wa)
    return scores


if __name__ == '__main__':
    main()