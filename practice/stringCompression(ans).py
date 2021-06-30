# 1부터 문장 길이의 절반까지 길이로 단위를 지정한다. 이 때 문장의 전체 길이도 단위로 지정한다.
# 지정된 단위로 문장을 쪼개어 리스트에 저장한다.
# 저장된 첫 번째 단어를 현재 단어로 하고, 카운터를 1로 지정한다.
# 연속된 단위를 찾기 위해 zip을 이용한다.
# 단어 리스트와 그 단어리스트의 한 칸 뒤부터 비교하여 같으면 카운터를 1증가시키고
# 같지 않으면 현재 단어와 다음 단어가 다르기 때문에 결과에 현재 단어와 카운터를 저장한다.
# 결과를 반환할 때 카운터와 단어의 길이를 모두 합쳐서 정수로 반환한다.
# 반환 받은 곳에서는 이 중 최솟값을 출력한다.

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    print(words)
    print(words[1:] + [''])
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    print(res)
    print(sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res))
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    print(list(range(1, int(len(text)/2) + 1)) + [len(text)])
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))