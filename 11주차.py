data = {
    '이름': ['Alice', 'Bob', 'Charlie', 'David'],
    '나이': [25, 30, 35, 28],
    '성별': ['여', '남', '남', '여']
}

df = pd.DataFrame(data)

print("|n첫 번째 행 조회:")
print(df.loc[0])
