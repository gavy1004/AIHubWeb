
# 여러 개의 자료(요소)들을 모아서 하나의 묶음으로 저장
# 많은 변수가 필요한 프로그램 작성시 유용함 (e.g., 학생 1000명의 성적 저장)
# 튜플은 원소의 값이 변경되지 않는다. 리스트는 변경 가능하다.
 
def tupel_ex():
    # 요소가 한 개인 Tuple 생성
    tuple1 = ('kor',)
    print(type(tuple1), tuple1)  # <class 'tuple'> (kor,)
    tuple2 = 'kor',
    print(type(tuple2), tuple2)  # <class 'tuple'> (kor,)

    # 리스트와 상호 변환
    list1 = [1, 2, 3]  # list 생성
    tuple1 = tuple(list1)  # list를 tuple로 변환
    print(type(tuple1), list1)  # <class 'tuple'> (kor,)
    tuple2 = (4, 5, 6)  # tuple 생성
    list2 = list(tuple2)  # tuple를 list로 변환
    print(type(tuple2), tuple2)  # <class 'tuple'> (kor,)

if __name__ == "__main__":
    tupel_ex()