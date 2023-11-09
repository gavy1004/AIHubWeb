# 식별자와 변수
def variable(): 
    score = 98
    print(score)    # 98
    type(score)     # <class 'int'>

# 표준 출력
# print(출력 내용, [, sep=구분자] [, end=끝문자])
def print_ex():
    a = 1
    b = 2
    c = 3

    print(a,b,c, sep='|', end="끝")

# 표준 입력
# 입력 받은 값 문자열로 저장됨
def input_ex():
    age = eval(input('몇 살인가요?'))
    type(age)

    a = int(input('1. 정수 입력 = '))
    b = int(input('2. 정수 입력 = '))
    print(a+b)



if __name__ == "__main__":
    input_ex()