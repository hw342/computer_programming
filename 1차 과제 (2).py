def main():
    ledger = {}  # 가계부 딕셔너리

    while True:
        print("\n가계부 계산기")
        print("1. 항목 추가")
        print("2. 항목 조회")
        print("3. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            add_entry(ledger)
        elif choice == '2':
            view_entries(ledger)
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 옵션을 선택하세요.")

def add_entry(ledger):
    date = input("날짜 (예: 2023-10-26): ")
    amount = float(input("금액: "))

    if date in ledger:
        ledger[date] += amount
    else:
        ledger[date] = amount

    print("항목이 추가되었습니다.")

def view_entries(ledger):
    if not ledger:
        print("가계부에 항목이 없습니다.")
        return

    print("\n가계부 항목:")
    for date, amount in ledger.items():
        print(f"{date}: {amount} 원")

if __name__ == "__main":
    main()
