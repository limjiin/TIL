#TD: final project

#lamb, apply, replace: 조건, 적용, 바꾸기
#sns.scatter or plt scatter: 점 그래프
#index
#arr2.shape
##print("arr2의 ndim : ", arr2.ndim) # arr2의 차원
##print("arr2의 shape : ", arr2.shape) # arr2의 행, 열의 크기
##print("arr2의 size : ", arr2.size) # arr2의 행 x 열
##print("arr2의 dtype : ", arr2.dtype) # arr2의 원소의 타입. # int64 : integer + 64bits
##print("arr2의 itemsize : ", arr2.itemsize) # arr2의 원소의 사이즈(bytes) # 64bits = 8B
##print("arr2의 nbytes : ", arr2.nbytes) # itemsize * size # numpy array가 차지하는 메모리 공간.

# 0이 3x3인 array
##np.zeros((3,3))
# 1이 3개 있는 array
##np.ones(3)
# 1이 2x2인 array
##np.ones((2,2))
# 0부터 9까지 숫자를 자동으로 생성한 array
##np.arange(10)
# 10부터 99까지 숫자를 자동으로 생성한 array
##np.arange(10,100) # python range 함수와 동일한데, np.array 생성까지 자동으로 해줍니다.
# v1 = (1, 2, 3), v2 = (4, 5, 6) 벡터 2개 생성하기.
##v1 = np.array((1,2,3))
##v2 = np.array((4,5,6))
## type(v1), type(v2)
# dot product
##v1 @ v2 # 1x4 + 2x5 + 3x6 = 32
# 위에서 생성한 data에 mask를 적용해본다.
##data[masked_data, :] # true 로 지정된 데이터를 뽑아낸 것
# 마스크를 0으로 바꿔본다. 
##data[mask == 0, :] # 0 = false 로 지정된 데이터를 뽑아낸 것
# mat1 제곱하기
##np.square(mat1)
# mat1의 지수값 구하기
##np.exp(mat1)
# mat의 log값(자연로그) 구하기
##np.log(mat1): log의 밑이 음수가 될 수 없다. (자연로그)
# 상용로그
##np.log10(mat1)
# 이진로그
##np.log2(mat1)
# 부호찾기
##np.sign(mat1)
# 올림
##np.ceil(mat1)
# 내림
##np.floor(mat1)
# 존재하지 않는 값이 있는지 없는지 # nan = not a number
##np.isnan(mat1)
# 평균
##np.mean(mat1)
#mat3 = np.random.rand(5, 3)
#mat3
#표준편차
##np.std(mat3)
# 최소값이 있는 Index
##np.argmin(mat3, axis=0)
# 최대값이 있는 Index
##np.argmax(mat3, axis=1)
#np.cumsum(mat3) #누적합.
#원형 그래프
##plt.figure(figsize=(16, 16))
##plt.pie(Q4.value_counts(),
##       labels=Q4.value_counts().index,
##       autopct='%d%%',
##       startangle=90,
##       textprops={'fontsize':12})
##plt.axis('equal')
##plt.title("Pie chart for Q4 column", fontsize=16)

