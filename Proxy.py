import requests
import re
import threading
import traceback

def checkip(lines):
    lines = lines.strip()
    lines = {'http': lines}
    try:
        r = requests.get('http://www.baidu.com', proxies=lines, timeout=5)
        print r.status_code
        if r.status_code == requests.codes.ok:
            return 1
            print('haha')
        else:
            print('wuwu')
            return 0
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
    return 0

if __name__ == "__main__":
    f = open('proxylist', 'r')
    for lines in f:
        lines = lines.strip()
        print checkip(lines)
