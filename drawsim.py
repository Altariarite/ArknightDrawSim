import random
from typing import List
import statistics as stats
import math
Card = (int,int)
# 模拟N次抽卡，已经不使用
def draw(time): 
    
    drawn = []
    history = 0
    bonus = 0
    chance = [0.4,0.5,0.08,0.02]
    for i in range(time):
        # 如果连续五十次没有获得六星，之后每次概率加2%，抽到六星则清零
        if history > 50:
            bonus = 0.02*(history - 49)
            chance[0] = 0.4*(1-bonus)
            chance[1] = 0.5*(1-bonus)
            chance[2] = 0.08*(1-bonus)
            chance[3] = bonus
        result = random.choices(
            # 标准寻访池，决定稀有度
            population = [3,4,5,6],
            weights = chance,
            k = 1
        )
        #没抽到六星增加计数,抽到归零
        if 6 == result[0]: history = 0
        else: 
            history += 1
        
        if result[0]==5 or result[0]==6:
            #决定是否是up
            up = random.randint(0,1)
            drawn.append((result[0],up))
        else:
            drawn.append((result[0],0))
    return drawn

#查看抽卡结果，返回一个统计的dictionary
def check(cards: Card):
    d = {(3,0): 0, (4,0):0, (5,0) :0, (5,1):0, (6,0):0, (6,1):0}
    for card in cards:
            d[card]+=1
    return d

#获得已抽卡数，决定将来一抽的结果
def draw_with_history(history) -> Card:
    bonus = 0
    chance = [0.4,0.5,0.08,0.02]
        # 如果连续五十次没有获得六星，之后每次概率加2%，抽到六星则清零
    if history > 50:
        bonus = 0.02*(history - 49)
        chance[0] = 0.4*(1-bonus)
        chance[1] = 0.5*(1-bonus)
        chance[2] = 0.08*(1-bonus)
        chance[3] = bonus
    result = random.choices(
        # 标准寻访池，决定稀有度
        population = [3,4,5,6],
        weights = chance,
        k = 1
    ) 
    #决定是否up
    if result[0] ==5 or result[0]==6:
        up = random.randint(0,1)
        return (result[0],up)
    else:
        return (result[0],0)

#输入次数和已经抽卡的数量，返回多次抽卡结果
def multi_draw(time,history):
    t = []
    h = history
    for i in range(time):
        result = draw_with_history(h)
        t.append(result)
        # 如果抽到了六星
        if result == (6,1)  or result == (6,0):
            h = 0
        else:
            h+=1
    return t

#输入目标和数量，一直抽卡直到抽到，返回抽数
def keep_drawing(cards,number)->int:
    h = 0
    draws=h
    count = 0
    while(True):
        # keep drawing
        result = draw_with_history(h)
        draws+=1
        if  result in cards: #抽到目标
            count+=1
            if cards == [(6,0),(6,1)]:
                h=0 #六星重置计数
            if count == number:
                return draws
        h+=1

# 进行N次模拟

# size = 50000
# count = 0 
# for i in range(size):
#     card = multi_draw(67,0)
#     result=check(card)

# #抽出至少一个目标：

#     success = False
#     # for target in targets:
#     if result[(6,1)] ==0:
#         success = True
#     if success :
#         count +=1
# print("%d in %d simulation" %(count,size))

#多少抽出一个up五星？
# size = 10000
# s= 0 
# for i in range(size):
#     s += keep_drawing((5,1))
# print("in %d simulation, it takes an average of %d draw(s) to draw a %s" %(size,s/size,(5,1)))

# 多少抽出一个up六星？

# 返回平均抽数和standard dev#
# print(keep_drawing((5,1),1))

print(keep_drawing([(6,0),(6,1)],2))
size = 50000
t = [] 
number = 1
for i in range(size):
    t.append(keep_drawing([(6,0),(6,1)],1))
mean = stats.mean(t)
std = stats.stdev(t)
print("in %d simulation, it takes an average of %d with a stdev of %.2f draw(s) to draw %d %s" %(size,mean,std,number,[(6,0),(6,1)]))


# size = 1000
# count = 0 
# t = 
# for i in range(size):
#     time = 1
#     while(True): #抽到出六星为止
#         result = check(draw(time))
#         if result[(6,1)]==1:
#             count +=1 
#             break
#         else: 
#             time+=1
#      += time

#十连紫气东来的概率有多大？
# time = 10
# size = 5000
# count = 0
# for i in range(size):
#     result=check(draw(time))
#     if result[(3,0)]+result[4,0]==10:
#         count +=1
# print("%d in %d simulation" %(count,size))
#十连双黄的概率有多大？
