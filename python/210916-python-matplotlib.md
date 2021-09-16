## Visualization (시각화)
> 데이터분석 및 보고에 필요한 시각화 패키지를 알아보고 실제 데이터로 시각화 예제
를 다루어봅니다.
> 데이터 시각화는 데이터분석 과정에서 단순히 데이터를 살펴보는데 그치지 않고 다>양한 분석 가능성을 보여줍니다.
> 또한 3자에게 설명을 함에 있어서도 데이터시각화는 굉장히 설득력있는 리포팅을 가
능하게 해줍니다.

## **Matplotlib**
> 파이썬의 대표적인 시각화 패키지
> 패키지의 이름에서 느껴지듯 MATLAB의 수리데이터 시각화를 파이썬으로 옮겨온 컨셉
> 기본적인 형태의 다양한 시각화 함수를 제공
> 사용이 약간은 불편

### 윈도우 한글 폰트 사용
> 네이버에서 배포하는 나눔바른고딕체 설치 필요
[https://hangeul.naver.com/font](https://hangeul.naver.com/font)

##### 1번째 방법

<pre>
<code>
# family 파라메터에 사용가능한 폰트이름 전달(가장 간단한 방법)
plt.rc('font', family='NanumGothic.ttf')
</code>
</pre>

##### 2번쨰 방법
<pre>
<code>
# 혹은 폰트 경로를 직접 전달해줘도 동작합니다.
# 다만 사용가능한 폰트 목록과 확장자명 확인이 필요합니다.
# font_location = '/Library/Fonts/Arial Unicode.ttf' # for 맥
font_location = 'C:/Windows/Fonts/NanumGothic.ttf' # for windows
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family='NanumBarunGothic')
</code>
</pre>

##### 3번째 방법

<pre>
<code>
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    f_path = '/Library/Fonts/Arial Unicode.ttf'
elif platform.system() == 'Windows':
    f_path = 'c:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=f_path).get_name()
rc('font', family=font_name)

print('Hangul font is set!')
</code>
</pre>

### 기본적인 line plot 그리기
    line plot은 시간 혹은 순서에 따라 데이터가 어떻게 변화하는지를 보기위해 주로
 사용합니다.

<pre>
<code>
# numpy array로 시각화 데이터 생성
# arange, linspace
x = np.arange(10)
y = x ** 2
x, y

x1 = np.linspace(-10, 10 ,300)
y1 = x1 ** 2

# line plot - plt.plot(x축 데이터, y축 데이터)
# plt.show() plt 함수로 정의 한 그래프 설정을 그래프화 시키는 명령어
plt.figure(figsize=(20, 10))
plt.title('line plot')
plt.plot(x1, y1)
</code>
</pre>

#### 스타일 지정
> plot명령어는 보는 사람이 그래프를 조금 더 보기 편하게 하기 위한 다양한 스타일>을 지원합니다.
> plot(데이터, '문자열인수')

<pre>
<code>
# line plot 스타일 지정
# 스타일 문자열은 색, 마커, 선 종류 순으로 지정하며 만약 이중 일부가 생략되면 디
폴트 값이 적용됩니다.
plt.plot(x, y, 'g1--')
</code>
</pre>

#### 자주 사용하는 선스타일 색상
    자주 사용되는 색깔은 한글자 약자를 사용할 수 있으며 약자는 아래 표에 정리하>였습니다.
| 문자열 | 약자 |
|-|-|
| blue | `b` |
| green | `g` |
| red | `r` |
| cyan | `c` |
| magenta | `m` |
| yellow | `y` |
| black | `k` |
| white | `w` |

#### 마커
    데이터의 위치를 표기하는 기호를 마커라고 합니다.
    사용가능한 마커의 종류를 아래 정리 해두었습니다.
| 마커 문자열 | 의미 | 마커 문자열 | 의미 |
|-|-|-|-|
| `.` | point marker  | `1` | tri_down marker |
| `,` | pixel marker | `2` | tri_up marker |
| `o` | circle marker | `3` | tri_left marker |
| `v` | triangle_down marker | `4` | tri_right marker |
| `^` | triangle_up marker | `s` | square marker |
| `<` | triangle_left marker | `p` | pentagon marker |
| `>` | triangle_right marker | `*` | star marker |
| `h` | hexagon1 marker | `x` | x marker |
| `H` | hexagon2 marker | `D` | diamond marker |
| `+` | plus marker | `d` | thin_diamond marker |

#### 선 스타일
    선 스타일에는 실선(solid), 대시선(dashed), 점선(dotted), 대시-점선(dash-dit)을 사용가능합니다.

| 선 스타일 문자열 | 의미 |
|-|-|
| `-` |  solid line style
| `--` |  dashed line style
| `-.` |  dash-dot line style
| `:` |  dotted line style

#### 그래프에 옵션 추가하기
지금부터는 plt 의 다른 함수를 사용하여 보는 사람의 이해를 도울 수 있는 여러 기능
들을 알아보겠습니다.

- `figure` : 그래프가 그려지는 캔버스 설정
- `title` : 그래프 제목
- `xlabel`, `ylabel` : 축 설명
- `legend` : 범례이름
- `xlim`, `ylim` : 축 범위
- `xticks`, `yticks` : 축 구간 내 필요한 구간만 추리기

##### lineplot 예시
<pre>
<code>
plt.figure(figsize=(10, 10)) # 그래프 크기조정, figsize=(가로 세로 사이즈 튜플 >전달) # 캔버스를 만든다.
plt.title('$x^2$ and $x^3$') # 그래프 타이틀 지정
plt.xlabel('$x$') # 범례지정
plt.ylabel('$y$', rotation='0')
plt.xlim([-5, 5]) # 축 범위 설정
plt.ylim([-10, 10])
plt.xticks([-5, 0, 5], rotation='vertical') # 축 구간 지정
plt.yticks([-10, 0 , 10], rotation='vertical')
plt.plot(x1, y1, '--', label='$x^2$') # 스케치
plt.plot(x1, x1**3, '--', label='$x^3') # 스케치
plt.legend(loc=0) # loc 파라메터 전달로 위치 지정
plt.show() # 완성

# 여러 그래프 한꺼번에 그리기
plt.figure(figsize=(10, 7))
plt.title('$x^2$ and $x^3$')
x = np.linspace(-10, 10, 300)
plt.plot(x, x*x, label='$x^2$')
plt.plot(x, x*x*x, 'r--', label='$x^3$') ***
plt.plot(x, np.sin(x), 'g:', label='$sin(x)$')
plt.plot(x, np.cos(x), 'k:', label='$cos(x)$')
plt.xlabel('x')
plt.ylabel('$x^2$ and $x^3$')
plt.xlim(-3, 3)
plt.ylim(-1, 1)
plt.legend(loc='best')
plt.show()
</code>
</pre>

##### 2개 이상의 그래프를 한 번에 정렬
<pre>
<code>
# subplot을 사용하여 여러 그래프 한번에 그리기
# 2 x 1 figure 매트릭스에 그래프 그리기
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.figure(figsize=(12, 8))

plt.subplot(211) # 도화지 나누기 2행 1열 그래프의 첫번째
plt.plot(x1, y1, 'yo-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(212) # 도화지 나누기 2행 1열 그래프의 두번째
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.tight_layout() # 여백줄이기
plt.show()

# 2 x 2 figure 매트릭스에 위에 그려진 제곱, 세제곱, sin, cos 그래프 나누기
x = np.linspace(-10, 10, 100)
y1 = x*x
y2 = x*x*x
y3 = np.sin(x)
y4 = np.cos(x)

plt.figure(figsize=(12, 8))

plt.subplot(221) # 도화지를 나누는 함수 괄호안에 (도화지의 행, 도화지 열, 순서)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(x, x*x, label='$x^2$')
plt.legend()
plt.title('$x^2$')

plt.subplot(222)
plt.plot(x, x*x*x, 'r--', label='$x^3$')
plt.legend()

plt.subplot(223)
plt.plot(x, np.sin(x), 'g:', label='$sin(x)$')
plt.legend()

plt.subplot(224)
plt.plot(x, np.cos(x), 'k:', label='$cos(x)$')
plt.legend(loc=0)

plt.tight_layout()
plt.show()

</code>
</pre>

### bar plot
> 전통적으로 bar plot은 범주형 데이터(구간이 나누어져 있는) 데이터의 갯수, 빈도>를 나타내는 데 쓰였습니다.
> 지난 시간 학습한 loan 데이터의 신용등급을 bar plot으로 그려보겠습니다.

<pre>
<code>
pd.options.display.max_columns = 200 # columns 크기 조절

# 세부신용등급 bar plot
plt.figure(figsize=(12, 8))
plt.bar(df['sub_grade'].value_counts().sort_index().index, df['sub_grade'].value_counts().sort_index().values)
plt.show()

# 세부신용등급 barh plot
plt.figure(figsize=(12, 8))
plt.barh(df['sub_grade'].value_counts().sort_index(ascending=False).index, df['sub_grade'].value_counts().sort_index(ascending=False).values)
plt.show()
</code>
</pre>

### 히스토그램
> 데이터의 분포를 확인하고자 할 때 많이 사용하는 시각화 방법입니다.
> 전체 데이터 구간 중 특정 구간에 속한 데이터의 빈도수를 계산하여 구간에 매칭시>킵니다.
> 데이터 구간별 밀도를 확인할 수 있습니다.

<pre>
<code>
# 대출금액분포 hist plot으로 확인
plt.figure(figsize=(12, 8))
plt.hist(df['loan_amnt'], bins=50) # 구간이 촘촘해짐
plt.show()
</code>
</pre>

### scatter plot
> 2개 혹은 2개 이상의 변수간의 관계를 확인하고자 할 때 많이 사용하는 시각화 방법
.
> X축과 Y축에 각각의 변수 데이터를 위치시키고 포인트들이 자리한 평면상의 분포를 통해 상관관계를 파악할 수 있습니다.

<pre>
<code>
# 각각의 변수와 우리가 보고자 하는 값과의 관계를 볼 때 가장 많이 사용합니다.
# loan_amnt(대출금), installment(원리금)
# 캔버스에 그려지는 점 하나가 샘플 하나
plt.figure(figsize=(12, 8))
plt.scatter(df['installment'], df['loan_amnt']) # 양의 상관 관계
plt.show()
</code>
</pre>

[https://matplotlib.org/](https://matplotlib.org/)

## matplotlib 예제 살펴보기

<pre>
<code>
from cycler import cycler
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Define a list of markevery cases and color cases to plot
cases = [None,
         8,
         (30, 8),
         [16, 24, 30],
         [0, -1],
         slice(100, 200, 3),
         0.1,
         0.3,
         1.5,
         (0.0, 0.1),
         (0.45, 0.1)]

colors = ['#1f77b4',
          '#ff7f0e',
          '#2ca02c',
          '#d62728',
          '#9467bd',
          '#8c564b',
          '#e377c2',
          '#7f7f7f',
          '#bcbd22',
          '#17becf',
          '#1a55FF']

# Configure rcParams axes.prop_cycle to simultaneously cycle cases and colors.
mpl.rcParams['axes.prop_cycle'] = cycler(markevery=cases, color=colors)

# Create data points and offsets
x = np.linspace(0, 2 * np.pi)
offsets = np.linspace(0, 2 * np.pi, 11, endpoint=False)
yy = np.transpose([np.sin(x + phi) for phi in offsets])

# Set the plot curve with markers and a title
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])

for i in range(len(cases)):
    ax.plot(yy[:, i], marker='o', label=str(cases[i]))
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.title('Support for axes.prop_cycle cycler with markevery')

plt.show()
</code>
</pre>

##### 3차원 표현 옵션

<pre>
<code>
%matplotlib notebook
# 3차원 표현 옵션
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib notebook # 3D plot을 인터랙티브하게 움직일 수 있도록 주피터노트북 설정
# %matplotlib inline # plot크기를 주피터 노트북에 알맞게(크기에 벗어나지 않게 그
려줌)

plt.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

# Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show() ********
</code>
</pre>

###### 코랩이 아닌 환경에서는 애니메이션 효과도 지원함

<pre>
<code>
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from collections import deque
%matplotlib notebook

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
L = L1 + L2  # maximal length of the combined pendulum
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg
t_stop = 5  # how many seconds to simulate
history_len = 500  # how many trajectory points to display


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

# create a time array from 0..t_stop sampled at 0.02 second steps
dt = 0.02
t = np.arange(0, t_stop, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], ',-', lw=1)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
history_x, history_y = deque(maxlen=history_len), deque(maxlen=history_len)


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    if i == 0:
        history_x.clear()
        history_y.clear()

    history_x.appendleft(thisx[2])
    history_y.appendleft(thisy[2])

    line.set_data(thisx, thisy)
    trace.set_data(history_x, history_y)
    time_text.set_text(time_template % (i*dt))
    return line, trace, time_text


ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
</code>
</pre>
