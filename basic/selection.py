def if_ex():
    rank, avg = input('등수와 평균을 입력하세요 : ').split()
    rank = int(rank)
    avg = float(avg)

    if rank <= 5 or avg >= 95:
        print("Pass")
    else:
        print("Fail")

def car_ex():
    carNum , dayNum = input('차량번호와 오늘 날짜를 입력하세요').split()
    carNum = int(carNum)
    dayNum = int(dayNum)

    if carNum%2 == 0:
        print("오늘입차 : 번호가 짝수인 차량")
    else:
        print("오늘입차 : 번호가 홀수인 차량")

    if carNum % 2 == dayNum % 2:
        print("귀하의 차량은 입차 가능합니다.")
    else:
        print("귀하의 차량은 입차 불가능합니다.")

if __name__ == "__main__": 
    car_ex() 