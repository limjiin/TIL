## Seaborn이란?
> matplotlib을 기본으로 다양한 시각화 기법을 제공하는 라이브러리.
> 엄청나게 화려한 시각화 기법들을 제공하며, 기본적으로 이쁩니다.
> pandas DataFrame과 매우 호환이 잘 됩니다.

-  histplot, kdeplot, jointplot, Facetgrid, ...
- e.g. sns.xxxplot(data=df)    **<--- 기본세팅!**

<pre>
<code>
# 라이브러리와 데이터를 불러오고, 시각화를 위한 세팅을 합니다.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
</code>
</pre>

#### Histplot
> 가장 기본적으로 사용되는 히스토그램을 출력하는 plot.
> 전체 데이터를 특정 구간별 정보를 확인할 때 사용합니다.

<pre>
<code>
# penguin 데이터에 histplot을 출력합니다.
sns.histplot(data=penguins, x='flipper_length_mm', hue='species', multiple='stack')
# 종별 쌓여서 출력
</code>
</pre>

#### Displot
> distribution들을 여러 subplot들로 나눠서 출력해주는 plot.
> displot에 kind를 변경하는 것으로, histplot, kdeplot, ecdfplot 모두 출력이 가능
합니다.

- e.g. displot(kind="hist")

<pre>
<code>
# penguin 데이터에 displot을 출력합니다.
sns.displot(data=penguins, x='flipper_length_mm', hue='species', col='species')
</code>
</pre>

#### Barplot
> 어떤 데이터에 대한 값의 크기를 막대로 보여주는 plot. (a.k.a. 막대그래프)
> 가로 / 세로 두 가지로 모두 출력 가능합니다.
> 히스토그램과는 다릅니다!

<pre>
<code>
# penguin 데이터에 barplot을 출력합니다.
sns.barplot(data=penguins, x='flipper_length_mm', y='species', hue='species')

sns.barplot(data=penguins, y='flipper_length_mm', x='species', hue='species')

sns.barplot(data=penguins, y='body_mass_g', x='species', hue='species')
</code>
</pre>

#### Countplot
> 범주형 속성을 가지는 데이터들의 histogram을 보여주는 plot.
> 종류별 count를 보여주는 방법입니다.

<pre>
<code>
# penguin 데이터에 countplot을 출력합니다.
sns.countplot(data=penguins, x='species', hue='sex')
</code>
</pre>

#### Boxplot
> 데이터의 각 종류별로 사분위 수(quantile)를 표시하는 plot.
> 특정 데이터의 전체적인 분포를 확인하기 좋은 시각화 기법입니다.
> box와 전체 range의 그림을 통해 outlier를 찾기 쉽습니다. (IQR : Inter-Quantile Range)

<pre>
<code>
# penguin 데이터에 boxplot을 출력합니다.
sns.boxplot(data=penguins, x='flipper_length_mm', y='species', hue='species')

sns.boxplot(data=penguins, x='body_mass_g', y='species', hue='species')

sns.boxplot(data=penguins, x='body_mass_g', y='species', hue='sex')
</code>
</pre>

#### Violinplot
> 데이터에 대한 분포 자체를 보여주는 plot.
> boxplot과 비슷하지만, 전체 분포에 대한 그림을 보여준다는 점에서 boxplot과 다릅
니다.
> 보통 boxplot과 함께 표시하면, 평균 근처에 데이터가 얼마나 있는지(boxplot) 전체
적으로 어떻게 퍼져있는지(violinplot) 모두 확인이 가능합니다.

<pre>
<code>
# penguin 데이터에 violinplot을 출력합니다.

sns.violinplot(data=penguins, x='flipper_length_mm', y='species', hue='species')

sns.violinplot(data=penguins, x='body_mass_g', y='species', hue='sex')
</code>
</pre>

#### Lineplot
> 특정 데이터를 x, y로 표시하여 관계를 확인할 수 있는 plot. (선 그래프)
> 수치형 지표들 간의 경향을 파악할 때 많이 사용합니다.

<pre>
<code>
# penguin 데이터에 lineplot을 출력합니다.
sns.lineplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='species')

sns.lineplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='sex')

sns.lineplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species')
</code>
</pre>

#### Pointplot
> 특정 수치 데이터를 error bar와 함께 출력해주는 plot.
> 수치 데이터를 다양한 각도에서 한 번에 바라보고 싶을 때 사용합니다.
> 데이터와 error bar를 한 번에 찍어주기 때문에, 살펴보고 싶은 특정 지표들만 사용
하는 것이 좋습니다.

<pre>
<code>
# penguin 데이터에 pointplot을 출력합니다.
sns.pointplot(data=penguins, y='flipper_length_mm', x='sex', hue='species')
</code>
</pre>

#### Scatterplot
> lineplot과 비슷하게 x, y에 대한 전체적인 분포를 확인하는 plot.
> lineplot은 경향성에 초점을 둔다면, scatterplot은 데이터 그 자체가 퍼져있는 모>양에 중점을 둡니다.

<pre>
<code>
# penguin 데이터에 scatterplot을 출력합니다.
sns.scatterplot(data=penguins, x='body_mass_g',y='flipper_length_mm', hue='species')

sns.scatterplot(data=penguins, x='bill_length_mm',y='bill_depth_mm', hue='sex')
</code>
</pre>

#### Pairplot
> 주어진 데이터의 각 feature들 사이의 관계를 표시하는 Plot.
> scatterplot, FacetGrid, kdeplot을 이용하여 feature간의 관계를 잘 보여줍니다.
> 각 feature에 대해 계산된 모든 결과를 보여주기 때문에, feature가 많은 경우 사용
하기 적합하지 않습니다.
> feature의 수가 작을 때 혹은 설정을 해주어서 사용한다.

<pre>
<code>
# penguin 데이터에 pairplot을 출력합니다.
sns.pairplot(data=penguins, hue='island')
# hue = sex, species, island(혼란스러운 정보)
</code>
</pre>

#### Heatmap
> 정사각형 그림에 데이터에 대한 정도 차이를 색 차이로 보여주는 plot.
> 말 그대로 heatmap이기 때문에, 열화상카메라로 사물을 찍은 것처럼 정보의 차이를 보여줍니다.
> pairplot과 비슷하게 feature간 관계를 시각화할 때 많이 사용합니다.

<pre>
<code>
# 각 feature간 상관관계를 파악하기 위해 Correlation matrix를 만듭니다.
corr = penguins.corr()

# penguin 데이터에 heatmap을 출력합니다.
sns.heatmap(data=corr)
</code>
</pre>

#### 원형 그래프

<pre>
<code>
plt.figure(figsize=(16, 16))
plt.pie(sQ4.value_counts(),
       labels=sQ4.value_counts().index,
       autopct='%.2f%%',
        colors=sns.color_palette('hls',len(sQ4.value_counts().index)),
       textprops={'fontsize':12})
plt.axis('equal')
plt.title("Pie chart for sQ4 column", fontsize=32, pad=50)
plt.show()
</code>
</pre>
