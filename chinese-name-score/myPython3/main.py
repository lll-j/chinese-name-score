#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
/html/body/div[6]/div[1]/div[2]/div[4]/div[14]/font[1]/b
/html/body/div[6]/div[1]/div[2]/div[4]/div[14]/font[2]/b

//div[@class="chaxun_b"]/font[@style="color:#3333FF;font-size:24px;font-family:arial;"]/b
//div[@class="chaxun_b"]/font[@style]/b

"""

from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

xing = "李".encode("gb2312")
def get_name_score(name):
    url = "http://life.httpcn.com/xingming.asp"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "data_type": 0,
        "year": 2019,
        "month": 7,
        "day": 23,
        "hour": 13,
        "minute": 50,
        "pid": "河北".encode("gb2312"),
        "cid": "石家庄".encode("gb2312"),
        "wxxy": 0,
        "xishen": "水".encode("gb2312"),
        "yongshen": "金".encode("gb2312"),
        "xing": "李".encode("gb2312"),
        # "ming": name.encode("GB18030"),
        # "ming": name.encode("utf-8"),
        # "ming": name.encode("gb2312"),
        "ming": name.encode("utf-8"),
        "sex": 1,
        "act": "submit",
        "isbz": 1
    }

    params_data = urlencode(data)
    # print(params_data)
    # r = request.get(url, data=params_data, headers=headers)
    r = requests.post(url, data=params_data, headers=headers)
    r.encoding = 'gb2312'

    if r.status_code != 200:
        raise Exception()
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    for node in soup.find_all("div", class_="chaxun_b"):
        # print(node)
        #//*[@id="raphael-paper-0"]/g[3]/text[1]/tspan
        #//*[@id="raphael-paper-34"]/g[3]/text[1]/tspan
        if "姓名五格评分" not in node.get_text():
            continue
        score_fonts = node.find_all("font")
        wuge_score = score_fonts[0].get_text()
        bazi_score = score_fonts[1].get_text()
        return wuge_score.replace("分", "").strip(), bazi_score.replace("分", "").strip()


# with open("input.txt") as fin, open("output.txt", "w") as fout:
with open("input.txt",encoding='utf-8') as fin, open("output.txt", "w",encoding='utf-8') as fout:
    for line in fin:
        # line = line.strip()
        # line = line.encode('utf-8').decode('utf-8').strip()
        print(line)
        if not line or len(line) == 0:
            continue
        wuge, bazi = get_name_score(line)
        fout.write(
            "\t".join([
                str("李"),
                line,
                wuge,
                bazi
            ]) + "\n"
        )
