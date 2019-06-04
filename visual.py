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
result = DrawUntilMatchSpecific((6,1),1,5000)
print(result)
sns.distplot(result)
plt.savefig("image.png")
