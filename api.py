# 公共API 来自于开源社区：https://www.apiopen.top/
# 非常感谢 CSDN 博主peakchao 的无私奉献
import json
import urllib
from urllib import request
import urllib.parse


def main():
    request1("POST", "上海")


# 获取实时天气
def request1(m="POST",text="shanghai"):
    url = "https://www.apiopen.top/weatherApi"
    params = {
        "city": text  # 城市名称的中文名称或拼音，如：上海 或 shanghai
    }
    params = urllib.parse.urlencode(params)
    if m == "POST":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    return res['data']
    # print(res['data'])


if __name__ == '__main__':
    main()

