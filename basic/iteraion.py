
def while_ex():
    i = 1
    while i <= 10:
        print('i = ', i)
        i += i  # Python 에서는 ++ 연산자 (num++)를 지원하지 않음
def stock_func():
    stockList = [['삼성전자', 79900], ['현대차', 233000], ['카카오', 155000]]
    while True:
        name = input("종목을 입력하세요 = ")

        if name == "종료":
            print("프로그램을 종료 합니다.")
            break
        else:
            for k,v in stockList:
                if k == name:
                    print("종목 =",  k, " 주가 =", v)

if __name__ == "__main__":
    stock_func()