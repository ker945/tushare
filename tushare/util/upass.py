# -*- coding:utf-8 -*- 

"""
Created on 2015/08/24
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
"""

import pandas as pd
import os
from tushare.stock import cons as ct

BK = 'bk'

def set_token(token):                              #创建函数，用来在本地存储token为tk.csv文件
    df = pd.DataFrame([token], columns=['token'])  #首先将token创建为DateFrame数据帧对象数据
    user_home = os.path.expanduser('~')            #获取用户目录 如：C:\\Users\\Administarator
    fp = os.path.join(user_home, ct.TOKEN_F_P)     #拼接tk.csv文件地址
    df.to_csv(fp, index=False)                     #将DataFrame数据帧数据存储为csv文件，地址为tk.csv的拼接地址。
    
    
def get_token():                                   #创建函数，用来读取本地存储的token
    user_home = os.path.expanduser('~')            #获取用户目录,如：C:\\Users\\Administarator
    fp = os.path.join(user_home, ct.TOKEN_F_P)     #拼接tk.csv文件地址
    if os.path.exists(fp):                         #如果路径存在则True，不存在则False。
        df = pd.read_csv(fp)                       #如果路径存在则读取 tk.cs文件，获取DataFrame数据帧对象。
        return str(df.loc[0]['token'])             #并返回 token元素内容。
    else:                                          #否则
        print(ct.TOKEN_ERR_MSG)                    #输出提示内容：设置token等。
        return None                                #返回None


def set_broker(broker='', user='', passwd=''):
    df = pd.DataFrame([[broker, user, passwd]], 
                      columns=['broker', 'user', 'passwd'],
                      dtype=object)
    if os.path.exists(BK):
        all = pd.read_csv(BK, dtype=object)
        if (all[all.broker == broker]['user']).any():
            all = all[all.broker != broker]
        all = all.append(df, ignore_index=True)
        all.to_csv(BK, index=False)
    else:
        df.to_csv(BK, index=False)
        
        
def get_broker(broker=''):
    if os.path.exists(BK):
        df = pd.read_csv(BK, dtype=object)
        if broker == '':
            return df
        else:
            return  df[df.broker == broker]
    else:
        return None
    
    
def remove_broker():
    os.remove(BK)
    
