import requests, execjs, time

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "nm-gcore-status": "1",
    "origin": "https://music.163.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://music.163.com/song?id=27965209",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}
cookies = {
    "NMTID": "00Oc-b4Fs-ygpxYfE8uh0iEkU8OOJEAAAGXDPV5aA",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "616d66393c476b59bbde4ac05426151c,1748269105211",
    "_ntes_nuid": "616d66393c476b59bbde4ac05426151c",
    "WEVNSM": "1.0.0",
    "WNMCID": "pjuzjq.1748269105451.01.0",
    "WM_TID": "4VCLJQCffKFEVBUUQQLGeBEAF1sc6RVU",
    "ntes_utid": "tid._.qR4Jas7DxMRFUhQBFEbDOEVUUw5cvZe7._.0",
    "sDeviceId": "YD-OBDEK0MDWm5EA1VBAFfTPAVUA19d7NhA",
    "NTES_P_UTID": "aW8jaFOS9P8nhtR7GGlYKcafYB9Z0xaV|1748716214",
    "P_INFO": "m13303398783@163.com|1748716214|0|mail163|00&99|shh&1748716200&unireg#shh&null#10#0#0|133783&1|unireg|13303398783@163.com",
    "nts_mail_user": "13303398783@163.com:-1:1",
    "__snaker__id": "Cep0i25V1EKNMtiF",
    "__remember_me": "true",
    "gdxidpyhxdE": "EOSYm0KlGD8dQOWW2APrPvJa3xKDLDLRVG37%2B%2BrIjyXWih23C2UG9bC10i2O4THll2cU5gzesCzCrcSXKGapu8iJvzasjZAHCUAcEGd%5C6TpNNf2EgY8TMsJCd6HPcS6bowKvZ%5CIViawqpdWuxekuTsQaHbWPGhKNcjsehBwKcPmPJyiG%3A1749109208890",
    "MUSIC_U": "003B573BD1E15C3E409F9907755AFAAF89047F287BAD94B2BA062D1233FEB157ADFE1535E5DA7F663684D776DBE9C42807A5A9C50D03CBFA2D47D989D9EC1326A5A2B8522D8C378033FB0EFD6DEDEF9FA79DA9FAC50CED2F5554CD8ABB129E1E2656DD592DB3CF101AF6146385407E701B510EA66FDE4C0E304CE400F3987D86C6262B2F171C833DE5D416D120C73135ECED6EB46D9409B30EDF2C346A9E2F00FBCD434A3D5374C4A2D305D012197E1C64BBAA9683F721204065F165B6EB7029A529A759E9151B50ACE5EA25932FF875EC7FDCDCC0673F7EB0A737E1C388C70104BCB7468C39749473164BA6E51D490984B2F52EF26AC515458CA3D9C0262DD9BA63BF1BC17AB254D0595A9BC5FDC28A8184931AD114C00DB695B4BE5DB077F730EA2CBE75CB3719FEABD161AF8B9939D4EED941B45F0C09CE61FE9D035F0336D312800280C65A8BDEF3934001E6347E11DDC0EFC246D5B86EA067FC1CEA2EFBDF",
    "__csrf": "d4fcbb4bb2237d4648cfe8e6a11badba",
    "ntes_kaola_ad": "1",
    "playerid": "66178139",
    "WM_NI": "hjOqdEn2kp2a%2B0cg57A%2F5mY8%2BiBNAZ0LgDQ14VQw076zoYqB4RIWFKiv0cmkB%2BYmEVHkqBPm0JWXGv%2F7F8IoD30dqGGD76peSfZbO82yjTI2XOq7dBbfOtMJTJ9cdGGHd1E%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eeb8d846f794aad3b670f59a8eb2d44f928f9fb0c245f4afe5a4f47091b6b7aad12af0fea7c3b92aacb68192e74faeeea591b16be9f0ad88b83d83f1fb8edc34e9b78eafc452f494a9a5d43bf88a9f98b33df6a6a1baf44af88e87b8c541abaa0084f06182f5978ec85e8cb5bfa3d367f49699b9c67eede98ad9cc6588ed0085f44d859cf9d7f36f91ba9683ce34f2a7a6b5cc3a9c91bfd8e74aa2ba8195d0429896f784e74d8598acd2c837e2a3",
    "JSESSIONID-WYYY": "0%2FegAXO77Ejkj%2B%2Bo%2B4b714Nwqgj9oqEpgU7wNtZ8OX9HeHr5mejP87ljidg7VHC2%2FBRlYJMagFa0PZNO8nryDTHdmx9f7KS%2FbyvdxD03AOR95K%2Bj4Kgu0KCQ6YSyFge%2FkniuewV7p3bJmOFNUXWbUEWE%2Bhq%2Fx5TMWBOYHpNvP%2BeCcy%5Cl%3A1749115321220"
}
url = "https://music.163.com/weapi/comment/resource/comments/get"
params = {
    "csrf_token": "d4fcbb4bb2237d4648cfe8e6a11badba"
}
with open('xx.js', 'r') as f:
    js_code = f.read()
    ctx = execjs.compile(js_code)


def main(x):
    global z
    z += 1
    data = ctx.call('result1', x)
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data).json()['data']['comments']
    for i in response:
        print(i['content'])
    nex = response[-1]['time']
    if z < 10:
        main(get_daa(z, nex))

        time.sleep(3)


def get_daa(z, time):
    daa = {
        "rid": "R_SO_4_27965209",
        "threadId": "R_SO_4_27965209",
        "pageNo": str(z),
        "pageSize": "20",
        "cursor": str(time),
        "offset": "0",
        "orderType": "1",
        "csrf_token": "d4fcbb4bb2237d4648cfe8e6a11badba"
    }
    print(z)
    return str(daa)

if __name__ == '__main__':
    z = 1
    initial_cursor = 1749100943625
    # 修正：确保daa中的{}占位符完整闭合（无遗漏的{或}）

    main(get_daa(z, initial_cursor))
