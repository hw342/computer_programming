scores = [90, 45, 64, 9, 17, 29]
results = []
for score in scores:
    if score >= 71:
        grade = 'A'
    elif score >= 41:
        grade = 'B'
    elif score >= 11:
        grade = 'C'
    else:
        grade = 'D'
    results.append(grade)
print(results)
