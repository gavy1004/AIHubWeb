import requests
import pandas as pd

def request():
    res = requests.get("http://info.cern.ch")
    print(res.text)
    print(res.headers)
    print(res.status_code)
    print(res.ok)

    res = requests.get("http://info.cern.ch/aaa")
    print(res.text)
    print(res.headers)
    print(res.status_code)
    print(res.ok)

# 텍스트 가져오기 + 저장하기
def getText():
    path = "https://www.gutenberg.org/files/60588/60588-0.txt"
    res = requests.get(path)
    print(res.text)

    with open("novel.txt", "w") as f:
        f.write(res.text)

def getImg():
    path = "https://s3-ap-northeast-2.amazonaws.com/opentutorials-user-file/course/3084/7512.png"
    res = requests.get(path)

    # 이미지를 o2.png 파일로 저장하기.
    with open('o2.png', 'wb') as f:
        f.write(res.content)

def pandas_ex():
    # 표(테이블)로 데이터를 구성하는 과정.
    # list of dictionaries
    data = [
        {'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'Paris'},
        {'name': 'Charlie', 'age': 35, 'city': 'Berlin'}
    ]

    # 데이터를 DataFrame으로 변환
    df = pd.DataFrame(data)
    print(df)
    # DataFrame을 엑셀 파일로 저장
    df.to_excel('output.xlsx', index=False)
    # DataFrame을 csv 파일로 저장
    df.to_csv('output.csv', index=False)

if __name__ == "__main__":
    pandas_ex()