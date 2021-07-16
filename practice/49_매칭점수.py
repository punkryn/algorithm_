# https://programmers.co.kr/learn/courses/30/lessons/42893

import re

def solution(word, pages):
    answer = 0
    word = word.lower()
    #m = re.compile('[^a-zA-Z]?' + word + '[^a-zA-Z]?')
    #print(m)

    score = [[] for _ in range(len(pages))]
    for i, page in enumerate(pages):
        head = 1501
        body = 1501
        notbody= False
        wc = 0
        outlink = 0
        for j, html in enumerate(page.split('\n')):
            print(html)

            if 'meta' in html and 'content' in html:
                # print(html.split()[2].split('\"')[1])
                score[i].append(html.split()[2].split('\"')[1])

            # if html == '<body>':
            #     body = j
            #
            # if html == '</body>':
            #     notbody = True

            #if not notbody and body < j:
            for w in html.split():
                if '<a ' in html:
                    # print("abc", html)
                    if 'href=' in w:
                        outlink += 1
                        score[i].append(w.split('\"')[1])

                w = w.lower()
                #print('w', w)
                #print('ww', m.findall(w))


                if word in w:
                    poslist = []
                    for wordindex in range(len(w) - len(word) + 1):
                        if w[wordindex: wordindex+len(word)] == word:
                            poslist.append(wordindex)

                    print('poslist', poslist)

                    for pos in poslist:
                        flag = False
                        flag2 = False
                        #pos = w.index(word)
                        print('123', word, w, pos+len(word), len(w))
                        if 0 < pos:
                            if ord(w[pos - 1]) < ord('a') or ord(w[pos - 1]) > ord('z'):
                                flag = True
                        elif pos == 0:
                            flag = True

                        if pos + len(word) < len(w):
                            #print(pos + len(word), (w[pos + len(word)]))
                            if ord(w[pos + len(word)]) < ord('a') or ord(w[pos + len(word)]) > ord('z'):
                                flag2 = True
                        elif pos + len(word) == len(w):
                            flag2 = True

                        print(flag, flag2)

                        if flag and flag2:
                            wc += 1

        score[i].append(wc)
        score[i].append(outlink)

    print(score)

    result = {}
    for cal in score:
        wc = cal[-2]
        result[cal[0]] = wc

    for cal in score:
        url = cal[0]
        wc = cal[-2]
        outlink = cal[-1]
        for link in cal[1: 1+outlink]:
            if link in result.keys():
                result[link] += (wc / outlink)

    print((result))

    maxvalue = 0
    for v in result.keys():
        if maxvalue < result[v]:
            maxvalue = result[v]
            answer = v

    for i in range(len(score)):
        if score[i][0] == answer:
            return i

    return answer

word = 'Muzi'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))