import requests
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser


url = "https://fifaonline4.nexon.com/datacenter"
# url = "https://www.inflearn.com/admin"
# url = "https://coupang.com"


robot_url = urljoin(url, "/robots.txt")

print(robot_url)

robot_parser = RobotFileParser()
robot_parser.set_url(robot_url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9"}

r = requests.get(robot_url, headers=headers)

if r.status_code == 200:
    # print(r.text.splitlines())
    robot_parser.parse(r.text.splitlines())

    if robot_parser.can_fetch("Mybot", url):
        print("Allow")
        # 크롤링 코드
    else:
        print("Disallow")
