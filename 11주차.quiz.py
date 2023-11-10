import random

def generate_lotto_numbers():
    lotto_numbers = []

    while len(lotto_numbers) < 6:
        new_number = random.randint(1, 45)

        if new_number not in lotto_numbers:
            lotto_numbers.append(new_number)

    lotto_numbers.sort()

    return lotto_numbers

def main():
    # 로또 번호 생성
    lotto_numbers = generate_lotto_numbers()

    # 생성된 로또 번호 출력
    print("생성된 로또 번호는 {} 입니다.".format(' '.join(map(str, lotto_numbers))))

if __name__ == "__main__":
    main()
