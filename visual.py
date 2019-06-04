# coding:utf-8 #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series,DataFrame
import matplotlib as mpl
from drawsim import DrawUntilMatch,DrawUntilMatchSpecific
#设置风格，尺度
sns.set_style('darkgrid')
sns.set_context('paper')
#mpl.use("pdf")
up = DrawUntilMatchSpecific([(6,1)],1,5000)
normal = DrawUntilMatchSpecific([(6,0),(6,1)],1,5000) 
# print(result)
sns.kdeplot(data=up ,cumulative=True, label = "6 up")
sns.kdeplot(data=normal ,cumulative=True, label = "6 normal")
plt.legend()
plt.savefig("CDF.png")
# sns.distplot(up)
# plt.savefig("up.jpg")
plt.show()