### 이미지 파일명 불러오기

<pre>
<code>
# 이미지 파일명 설정
img_nm = './data/lena.jpg'

# 이미지를 파이썬으로 불러들임
lena = plt.imread(img_nm)

# 이미지 plotting
plt.imshow(lena);
# ; : 위에 있는 텍스트 삭제

# lena : pixel 0 ~ 255 : 0 검정색, 255 흰색

# 이미지 shape 확인
# 맨 뒤 '4'가 RGB 채널에 해당하는 부분
lena.shape : (512, 512, 4)
</code>
</pre>

### RGB

<pre>
<code>
# RGB 설정
R = lena.copy()
G = lena.copy()
B = lena.copy()

R[:,:, (1, 2)] = 0 # R 채널 값을 제외한 GB 채널 값을 0으로 만들어주는 코드
G[:,:, (0, 2)] = 0 # G 채널 값을 제외한 RB 채널 값을 0으로 만들어주는 코드
B[:,:, (0, 1)] = 0 # B 채널 값을 제외한 RG 채널 값을 0으로 만들어주는 코드

# Red로 이미지 추출
plt.imshow(R);

# RGB 각각의 이미지 한 번에 추출
plt.figure(figsize=(20, 10))

plt.subplot(131)
plt.imshow(R)

plt.subplot(132)
plt.imshow(G)

plt.subplot(133)
plt.imshow(B)

# 한 채널만 사용했을 때 흑백 전환
plt.imshow(lena[:, :, 2])
</code>
</pre>

### 이미지 저장, 크롭

<pre>
<code>
# 이미지 저장
img = Image.fromarray(lena[:,:, 2])
img.save('./data/lena_color_split.jpg')

# 이미지 크롭
plt.imshow(lena[100:500, 100:500])

# 반전, 축변환
mo_lena = lena[:, :, 0]
mo_lena.shape

plt.imshow(mo_lena[::-1].T);

# 명암 대비
plt.imshow(255 - mo_lena)
</code>
</pre>
