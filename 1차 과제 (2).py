def calculate_monthly_transportation_cost():
    print("한 달 교통비 계산기")

    # 대전에서 충주까지의 교통비 요금 정보
    Daejeon_bus_fare = 1250
    train_fare = 7600
    chungju_bus_fare = 1400

    # 한 달 동안의 이용 횟수 입력 받기
    while True:
        try:
            Daejeon_bus_count = int(input("한 달 동안 대전에서 시내버스를 몇 번 이용했습니까? "))
            train_count = int(input("한 달 동안 대전에서 충주까지 기차를 몇 번 이용했습니까? "))
            chungju_bus_count = int(input("한 달 동안 충주 시내버스를 몇 번 이용했습니까? "))
            break
        except ValueError:
            print("올바른 숫자를 입력하세요.")

    # 한 달 동안의 교통비 계산
    total_fare = (Daejeon_bus_fare * Daejeon_bus_count) + (train_fare * train_count) + (chungju_bus_fare * chungju_bus_count)

    print(f"한 달 동안의 총 교통비는 {total_fare}원 입니다.")

# 한 달 교통비 계산기 실행
calculate_monthly_transportation_cost()
