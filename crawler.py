import requests
from bs4 import BeautifulSoup
import time
import os
from os.path import getsize
import re

def image_download(BASE_URL, title):
    # 헤더 설정 (필요한 대부분의 정보 제공 -> Bot Block 회피)
    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "sec-ch-ua-mobile": "?0",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9"
    }

    titleRule = ["\\", "\"", "/", ":", "*", "?", "<", ">", "|"]
    for word in titleRule:
        if word in title:
            title = title.replace(word, "_")
    print(title)

    if os.path.isdir(f"Image/{title}"):
        print("동일한 폴더가 있음")
        return

    os.mkdir(f"Image/{title}")

    res = requests.get(BASE_URL, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    # 아래 이미지 다운로드 받는 곳에서 시작
    image_download_contents = soup.select("div.appending_file_box ul li")
    for li in image_download_contents:
        img_tag = li.find('a', href=True)
        img_url = img_tag['href']

        file_ext = img_url.split('.')[-1]
        # 저장될 파일명
        savename = img_url.split("no=")[2]
        headers['Referer'] = BASE_URL
        try:
            response = requests.get(img_url, headers=headers)
        except:
            print("error ocuured")
            continue


        path = f"Image/{title}/{savename}"
        file_size = len(response.content)

        regexp = re.compile('\[\d+\]')

        if os.path.isfile(path):  # 이름이 똑같은 파일이 있으면
            if getsize(path) != file_size:  # 받을 파일과 기존파일의 크기가 다를경우 (다른 파일일경우)
                print("이름은 겹치는 다른파일입니다. 다운로드 합니다.")

                # fileName = path.split('.')
                # order = fileName[0][-3:]
                # ext = fileName[-1]
                # if regexp.fullmatch(order):
                #     idx = int(order[1:-1])
                #     while True:
                #         idx = idx + 1
                #         path = fileName[0][:-3] + str(idx) + '.' + ext
                #         if not os.path.isfile(path):
                #             break
                # else:
                #     path = fileName[0] + "[1]" + "." + ext

                try:
                    file = open(path, "wb")  # 경로 끝에 [1] 을 추가해 받는다.
                    file.write(response.content)
                    file.close()
                except:
                    print("same file download error")
            else:
                print("동일한 파일이 존재합니다. PASS")
        else:
            try:
                file = open(path, "wb")
                file.write(response.content)
                file.close()
            except:
                print("download error")


def image_check(text):
    text = str(text)
    if "icon_img" in text:
        return True
    else:
        return False


# while True:
BASE_URL = "https://gall.dcinside.com/board/lists?id=dcbest"

# 헤더 설정 (필요한 대부분의 정보 제공 -> Bot Block 회피)
headers = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "sec-ch-ua-mobile": "?0",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ko-KR,ko;q=0.9"

}

max_page = 3
for page in range(1, max_page + 1):
    res = requests.get(BASE_URL + "&page=" + str(page), headers=headers)

    if res.status_code == 200:
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        doc = soup.select("td.gall_tit > a[view-msg]")
        print(doc)
        for i in range(1, len(doc)):  # 공지사항 거르고 시작 (인덱스 뒤부터)
            # print(doc[i])
            link = "https://gall.dcinside.com" + doc[i].get("href")  # 글 링크
            title = doc[i].text.strip()  # 제목
            # print("title", title, " ", i)
            if("ㅇㅎ" not in title):
                continue
            image_insert = image_check(doc[i])  # 이미지 포함여부
            print("link", link, ' ', title, ' ', image_insert)

            if (image_insert == True):  # 이미지 포함시
                image_download(link, title)  # 이미지 다운로드하기
            # break  # 바로 break해서 첫글만 가져옴
            time.sleep(1)