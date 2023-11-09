import requests
import bs4

def bs_ex():
    res = requests.get("http://info.cern.ch")
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    print(soup)

    print(soup.html.body.header.title)
    print(soup.title)
    print(soup.ul)

    # 주의: select의 결과는 list
    # CSS Selector의 선택방식을 차용해서 만들어진 함수.
    tags = soup.select("a")
    print(tags)

    tags = soup.select("video")
    print(tags)

    # 태그의 속성 정보
    tags = soup.select("a")
    for t in tags:
        print("link", t["href"])
        print("text", t.get_text())

# https://opentutorials.org/course/1
# img의 src 주소 정보만 추출하라.
def mission():
    url = "https://opentutorials.org/course/1"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # HTML Parser
    # html 문서를 트리 형태로 구조화한다.
    # css selector 기능을 이용해 원하는 정보에 쉽게 접근할 수 있다.
    for tag in soup.select("img"):
        print(tag["src"])

        if tag["src"][:4] == "http":
            img = requests.get(tag["src"])
            with open(tag["src"].split("/")[-1], 'wb') as f:
                f.write(img.content)
        else:
            img = requests.get(url + tag["src"])
            with open(tag["src"].split("/")[-1], 'wb') as f:
                f.write(img.content)

if __name__ == "__main__":
    mission()