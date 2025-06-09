// 7185418d2bb30c9b3109109512010325c3f86ab2c6e5b2aec8ae529431433801b67ae082fc5722ff50bfe08adeac6b7d58afc7d8857146eca659052fda9107f7
const CryptoJS = require("crypto-js");
var a_default={
    "n": 20,
    "codes": {
        "0": "W",
        "1": "l",
        "2": "k",
        "3": "B",
        "4": "Q",
        "5": "g",
        "6": "f",
        "7": "i",
        "8": "i",
        "9": "r",
        "10": "v",
        "11": "6",
        "12": "A",
        "13": "K",
        "14": "N",
        "15": "k",
        "16": "4",
        "17": "L",
        "18": "1",
        "19": "8"
    }
}
function crypto(e, n) {
    return CryptoJS.HmacSHA512(e,n).toString()
}
function R1default() {
                var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
                  , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
                  , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
                  , i = JSON.stringify(e).toLowerCase();
                return crypto(n + "pathString" + i + t, o(n))
            }
function o1default() {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , n = JSON.stringify(e).toLowerCase();
    return crypto(t + n, o(t)).toLowerCase().substr(8, 20)
}
function o() {
    for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        var o = t[i].charCodeAt() % a_default.n;
        n += a_default.codes[o]
    }
    return n
}
function cache(name,page) {
    key=o1default("/api/search/searchmulti",  {"searchkey":name,"pageindex":page,"pagesize":20})

    value=R1default("/api/search/searchmulti",  {"searchkey":name,"pageindex":page,"pagesize":20},'7b4ba15edd2a84a943c656ae3ecc73ba')
    return [key,value]

}
cache(1)