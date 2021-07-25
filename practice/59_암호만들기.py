# 4 6
# a t c i s w

# https://www.acmicpc.net/problem/1759

def go(depth, string):
    if depth == l:
        if check(string):
            print(''.join(string))
        return

    for w in alphabet:
        if not string or ord(w) > ord(string[-1]):
            string.append(w)
            go(depth+1, string)
            string.pop()

def check(string):
    j = 0
    m = 0
    for w in string:
        if w in moeum:
            m += 1
        else:
            j += 1

        if m >= 1 and j >= 2:
            return True

    return False

l, c = map(int, input().split())

alphabet = list(input().split())
alphabet.sort(key=lambda x: ord(x))
moeum = ['a', 'e', 'i', 'o', 'u']
go(0, [])