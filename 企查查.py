import requests,json,execjs
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "dnt": "1",
    "origin": "https://www.qcc.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "x-pid": "47922c0cd1fdb5184c53c4819ee1a17e",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "QCCSESSID": "1ecb22a527493caa3b80c46a7e",
    "qcc_did": "e132f3c3-306f-4c34-8bd0-a1bb3e6aeec8",
    "UM_distinctid": "197444ab21a1d00-0a3e945d5ae2758-4c657b58-190140-197444ab21b2b3c",
    "tfstk": "gylii_jqDAy62l-LpXN6UbuXv0JL65NbUmCYDSE2LkrCXGCtuSrm0khTXVFN5vi-z1h9CSC01SN223dJwN3_GSznX-VNfMz_7IC43rP_Tao-wEdJwVgaHhy7GQhYd8Y8xoP4Q-rU8kaP3io4QWzUAraVbr5w-eqQlsWa01zF8Pag0SPq0283lkr4gRoq8jPM7lns2X-KKDdWi8TtOP2g4VrZWclewJWsukfVgX2uIuS0xs5qtP0m2OKAZKErFle8mDRdsS0UoD2-I3fimquS3JccbFnrYxm4RvtcnuDqWYM4KFRZ-5qiqXwkMhNi3cG0CAbXP2PZAYZ7QptQ-fh8nuwhYhuK-lyoncKCglHo8D2-9MC8aYini8PP4j6FUKtOGy8xTt6bQya32V-Q5ED8RC9X-eXzhRzQ5BYH-t6bQya32eYhUmwaRPOh.",
    "acw_tc": "0a47308817492052917243317e00849ed6bfe44d45c7140ae5f885154ae490",
    "CNZZDATA1254842228": "1721123811-1749197435-%7C1749205323"
}
name='gezi'
url = "https://www.qcc.com/api/search/searchMulti"
with open("企查查.js", "r", encoding="utf-8") as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
def main(page):
    x=ctx.call("cache",name,page)
    headers[x[0]]=x[1]
    data = {
        "searchKey": name,
        "pageIndex": page,
        "pageSize": 20
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data).json()['Result']
    for i in response:
        print(i['Address'])
main(3)