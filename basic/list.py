# 수치형과 문자열 
def literal_ex():
    msg = 'kor eng math art'
    splitMsg = msg.split()
    print(splitMsg)     # ['kor', 'eng', 'math', 'art']
    date = '2021.06.10'
    splitDate = date.split('.')
    print(splitDate)    # ['2021', '06', '10']
    joinMsg = '|'.join(splitMsg)    # 'kor|eng|math|art'

    joinMsg = '-'.join(splitDate)
    print(joinMsg)

# 리스트
def list_ex():
    scoreList = [90, 70, 50]
    print(scoreList[0]) # [] 로 생성 , index로 접근가능
    # index 범위를 벗어나면 에러 발생(IndexError: list index out of range)

    # list(range()) 를 사용하여 여러요소 한번에 생성가능
    # list = list(range(begin, end, step))
    a = list(range(10)) # begin == 10
    print(a)            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = list(range(5,10))# begin == 5, end == 10
    print(b)            # [5, 6, 7, 8, 9]
    c = list(range(1, 10, 2))  # begin==1, end==10, step==2
    print(c)            # [1, 3, 5, 7, 9]

    d = list(range(10, 1, -2))   # begin == 1, end == 10, 짝수만 역으로
    print(d)

# list 슬라이싱
def list_slice_ex():
    # list[begin:end:step] 형태로 사용

    # begin부터 end index -1 까지의 list 반환
    scoreList = [90, 70, 50, 60, 80, 100, 95]
    scoreList[2:3]
    print(scoreList[2:3])

    # begin 요소가 생략되면 0번 index 부터 반환
    scoreList[:4]
    print(scoreList[:4])    # [90, 70, 50, 60], [:end]

    # begin과 end 요소가 생략되면 모든 요소 반환
    scoreList[:]
    print(scoreList[:]) # [90, 70, 50, 60, 80, 100, 95]

    # step을 사용하면 해당 step 만큼 index가 증감
    scoreList[::2]  # [90, 50, 80, 95], [::step]
    scoreList[3::-1]  # [60, 50, 70, 90], [begin::-step]

def list_func_ex():
    scoreList = [90, 70, 50, 60, 80, 100, 95, 99]

    len(scoreList)          # 길이
    scoreList.append(40)    # 끝에 요소 추가
    scoreList.insert(0,88)  # 특정 위치에 요소 추가

    # 요소 추가
    # numList1.extend(numList2)

    scoreList.remove(99)  # 요소 중 값이 99인 요소 삭제
    #del(scoreList[0])  # index가 0인 요소 삭제
    #del (scoreList)    # index를 명시하지 않으면 list 자체를 삭제함
    #scoreList.clear()  # 리스트 내부 모든 요소 삭제

    # 정렬 원형 변형
    scoreList.sort()  # default: 오름차순
    scoreList.sort(reverse=True) # 내림차순

    # 정렬 원형 변형 X
    sortedList = sorted(scoreList)  # [50, 60, 70, 80, 90, 95, 100]
    sorted(scoreList, reverse=True)  # [100, 95, 90, 80, 70, 60, 50]

    # 키를 사용하여 정렬
    stringList = ['google', 'go', 'goo']
    stringList.sort(key=len)  # 길이순으로 정렬

    complexList = [['kor', 90], ['eng', 70], ['math', 50]]
    sorted(complexList, key=lambda x: x[1])  # [['math', 50], ['eng', 70], ['kor', 90]], 각 요소의 1번 요소인 점수 순으로 정렬

    # 순서 뒤집기
    scoreList = [90, 70, 50, 60, 80, 100, 95]
    scoreList.reverse()
    scoreList   # [95, 100, 80, 60, 50, 70, 90]

    # value 로 특정 요소 index 반환
    scoreList = [90, 70, 50, 60, 80, 100, 95]
    scoreList.index(100)  # 5, value가 100인 요소의 index 반환

    # 특정 요소값의 count 반환
    scoreList.count(50)  # 1, value가 50인 요소의 개수 반환

    # 합계 계산
    mySum = sum(scoreList)  # 545, 전체 요소의 합계 계산 후 반환
    print(mySum)

    # 평균 계산
    scoreList = [90, 70, 50, 60, 80, 100, 95]
    myAvg = sum(scoreList) / len(scoreList)
    print(myAvg)

    # 최대, 최소
    min(scoreList)
    max(scoreList)

    # 포함 여부 확인
    60 in scoreList  # True
    60 not in scoreList  # False

def attend_func():
    student = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']
    print(student)

    # 가나다 정렬
    print(sorted(student))

    # 박찬호 전학
    student.remove('박찬호')
    print('전체학생 : ',student,', 학생수:',len(student),'명')

    # 선생님 도울 3명
    print(student[:3])

    # 이병규 전학 옴
    student.append('이병규')

    # 학생 순서 역순
    student.reverse()
    print(student)

    # 정우람 -> 정잘남 으로 개명
    idx = student.index('정우람')
    student[idx] = '정잘남'
    print(student)

if __name__ == "__main__":
    attend_func()