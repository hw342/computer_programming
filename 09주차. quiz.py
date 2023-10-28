def validate_jumin(jumin_number):
    # 주민번호가 13자리인지 확인한다
    if len(jumin_number) != 13:
        return False

    # 마지막 자리를 제외한 숫자 부분을 가져온다
    jumin_digits = jumin_number[:12]

    try:
        jumin_digits = list(map(int, jumin_digits))  # 숫자로 변환한다
    except ValueError:
        return False

    # 2,3,4,5,6,7,8,9,2,3,4,5를 각 자리에 곱하고 모두 더한다
    weighted_sum = sum([a * b for a, b in zip(jumin_digits, [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5])])

    # 더한 결과를 11로 나눈 나머지 값을 구한다
    remainder = weighted_sum % 11

    # 11에서 나머지 값을 뺀다
    subtracted = 11 - remainder

    # 연산의 결과 값이 주민번호의 마지막 자리의 수와 같은지 비교한다
    last_digit = int(jumin_number[12])
    return subtracted == last_digit

# 주민번호를 입력받는다
jumin_number = input("주민번호를 입력하세요 (예: 123456-1234567): ")

# 입력받은 주민번호의 유효성을 체크한다
if validate_jumin(jumin_number):
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")
