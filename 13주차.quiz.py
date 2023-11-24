# 필요한 라이브러리 불러오기
import pandas as pd
from sklearn.model_selection import cross_val_score, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# 데이터 불러오기
file_path = 'C:\\Computer_Programming\\computer_programming\\data\\irisdata.csv'
df = pd.read_csv(file_path)

# 데이터 확인
print("데이터 셋의 행렬 크기:", df.shape)
print("데이터 셋의 요약:\n", df.describe())
print("데이터 셋의 클래스 종류:\n", df.groupby('class').size())

# scatter_matrix 그래프 저장
scatter_matrix(df, alpha=0.8, figsize=(10, 10), diagonal='hist')
plt.savefig('C:\\Computer_Programming\\computer_programming\\data\\scatter_matrix.png')

# 독립 변수(X)와 종속 변수(Y)로 분할
X = df.iloc[:, 0:4]
Y = df['class']

# 의사결정 나무 모델 생성
model = DecisionTreeClassifier()

# K-fold 및 cross validation을 사용한 모델 평가
kfold = KFold(n_splits=10, shuffle=True, random_state=42)
cv_results = cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')

# 평균 정확도 출력
print("K-fold의 평균 정확도:", cv_results.mean())
