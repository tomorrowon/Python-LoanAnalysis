# 데이터 분석을 위한 라이브러리를 가져오기
    # tensorflow : 수치 계산과 대규모 머신러닝을 위한 오픈 소스 라이브러리
    # pandas : 행과 열로 이루어진 데이터 객체를 만들어 다룰 수 있고, 안정적으로 대용량의 데이터들을 처리 가능하도록 하는 데이터 분석 라이브러리
    # seaborn : Matplotlib 을 기반으로 다양한 색상 테마와 통계용 차트 등의 기능을 추가한 시각화 패키지
    # numpy : 벡터, 행렬 등 수치 연산을 수행하는 선형대수 라이브러리
    # matplotlib.pyplot : 데이터를 차트나 플롯으로 그려주는 라이브러리 패키지
    # plot : 값을 서로 연결해서 라인 형태의 그래프를 그리는 함수

import tensorflow as tf
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# plotly 시각화
    # plotly : 컴퓨팅 기술 회사로, 온라인 데이터 분석 및 시각화 툴을 개발

from plotly import tools
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)


# For oversampling Library (Dealing with Imbalanced Datasets)
from imblearn.over_sampling import SMOTE
from collections import Counter


# Other Libraries
import time

# % matplotlib inline
    # 에러 발생 ( https://whoishoo.tistory.com/79 ) 참고

plt.show()
df = pd.read_csv('input/loan.csv', low_memory=False)


# Copy of the dataframe
original_df = df.copy()
df.head()