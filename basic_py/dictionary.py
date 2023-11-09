# key와 value의 쌍을 저장하는 대용량 자료구조로 우리가 사용하는 사전과 동일한 형태를 가지고 있음
# dic = {key1: value1, key2: value2 ... } 형태로 사용
# 순서가 없는 타입이었으나 Python 3.7부터는 삽입 순서 유지

def dict_ex(): 
    infoDic = {'roomId': 1, 'name': '휴게실', 'temp': 22.5, 'humidity': 60, 1: True, 2: False}
    print(infoDic)
    print(type(infoDic))

    # 튜플, 정수, 실수, bool, 문자열 키 사용 가능, 리스트, dict 사용 불가
    a = {(1, 2): 1}  # Tuple을 key로 설정, OK
    print(a)  # {(1, 2): 1}

    # 키 중복 불가 (가장 마지막 값)

    # dict 생성
    a = dict()
    b = {}

    # dict 접근
    # dic[key]
    subject = {'kor': '0101', 'eng': '0102', 'math': '0103'}
    # subject[0]  # index 사용, Error
    subject['kor']  # 0101

    # get(key [, value])
    code = subject.get('math')
    print(code)  # 0103

    # 요소 추가
    subject['sci'] = '0110'

    # 요소 삭제
    del subject['sci']
    del(subject['kor'])

    # 모든 요소가 삭제되었으나 dictionary는 남아 있음
    subject.clear()

    # dict 자체 삭제
    del (subject)

    a = {'1':1, '2':2, '3':3}
    a.update({'2':22, '3':33})  # 여러 요소 동시 수정

    a.update({'4': 44, '5': 55})  # key가 없으면 추가
    print(a)  # {'1': 1, '2': 22, '3': 33, '4': 44, '5': 55}

    # 포함 여부 확인
    a = {'1': 1, '2': 2, '3': 3}
    print('2' in a)  # True
    print(3 in a)  # Fals

def dict_func():
    # key 로만 구성된 list 생성
    subject = {'kor': '0101', 'eng': '0102', 'math': '0103', 'sci': '0110'}
    name = subject.keys()  # key 추출
    print(name)  # dict_keys(['kor', 'eng', 'math', 'sci'])
    type(name)  # <class 'dict_keys'>

    # value로만 구성된 List 생성
    subject = {'kor': '0101', 'eng': '0102', 'math': '0103', 'sci': '0110'}
    code = subject.values()   # value 추출
    print(code)               # dict_values(['0101', '0102', '0103', '0110'])
    type(code)                # <class 'dict_values'>

    # key와 value로 구성된 List 생성 items()
    subject = {'kor': '0101', 'eng': '0102', 'math': '0103', 'sci': '0110'}
    subCode = subject.items()  # key와 value 추출
    print(subCode)  # dict_items([('kor', '0101'), ('eng', '0102'), ('math', '0103'), ('sci', '0110')])
    type(subCode)  # <class 'dict_items'>

    # list 로 변환
    subject = {'kor': '0101', 'eng': '0102', 'math': '0103', 'sci': '0110'}
    name = subject.keys()  # key 추출
    nameList = list(name)  # name dict_keys 를 list로 변환
    print(nameList)  # ['kor', 'eng', 'math', 'sci']
    type(nameList)  # <class 'list'>

    code = subject.values()  # value 추출
    codeList = list(code)  # code dict_values 를 list로 변환
    print(codeList)  # ['0101', '0102', '0103', '0110']

    subCode = subject.items()  # key와 value 추출
    subCodeList = list(subCode)  # subCode dict_items 를 list로 변환
    print(subCodeList)  # [('kor', '0101'), ('eng', '0102'), ('math', '0103'), ('sci', '0110')]

if __name__ == "__main__":
    dict_func()