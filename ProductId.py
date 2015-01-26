import requests
import json
import lxml.html
import re


def getids_tmall(shopname):
    url = 'http://{}.tmall.com/search.htm?spm=&pageNo=1'.format(shopname)
    r = requests.get(url)
    scode = r.text
    doc = lxml.html.document_fromstring(scode)
    ss = doc.xpath('//p/b[@class="ui-page-s-len"]/text()')
    hrefs = doc.xpath(
        '//div[@class = "J_TItems"] // a[@class = "item-name"] / @href')
    h1 = re.findall(r'id=(\d{11})', str(hrefs))
    maxpagenum = ss[0].replace('1/', '')
    if maxpagenum == 1:
        return set(h1)
    else:
        for i in range(2, int(maxpagenum) + 1):
            url = 'http://{}.tmall.com/search.htm?spm=&pageNo={}'.format(
                shopname, i)
            r = requests.get(url)
            scode = r.text
            doc = lxml.html.document_fromstring(scode)
            hrefs = doc.xpath(
                '//div[@class = "J_TItems"] // a[@class = "item-name"] / @href')
            h1 += re.findall(r'id=(\d{11})', str(hrefs))
        return set(h1)


print(getids_tmall('chipisheaumeiu'))
