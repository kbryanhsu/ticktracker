# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 02:04:37 2021

@author: kathe
"""

import sys
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import csv
import statsmodels.api as sm
import sys 
import time
import gc
import shutil
import os

dataPath1 = "C:/Users/kathe/Documents/BEPP 399/Industry.csv"
dataPath2 = "C:/Users/kathe/Documents/BEPP 399/Market Cap.csv"


df1 = pd.read_csv(dataPath1, dtype={"Ticker" : "string", "Industry" : "string", "Name" : "string"})
df2 = pd.read_csv(dataPath2, dtype={"Ticker" : "string", "Market Cap" : "string", "Name" : "string"})
df1 = df1.dropna()
df2 = df2.dropna()

industryTickerlist = df1.loc[:,"Ticker"].to_list()
industryIndustrylist = df1.loc[:,"Industry"].to_list()
ipointer = 0
while ipointer < len(industryTickerlist):
    newDir = os.path.join(os.getcwd(),industryIndustrylist[ipointer])
    if os.path.isdir(newDir) is not True:
        os.mkdir(newDir)
    getcsv = os.path.join(os.getcwd(),industryTickerlist[ipointer]+".csv")
    if os.path.exists(getcsv) is not True:
        ipointer = ipointer + 1
        continue
    shutil.copy(getcsv,newDir)
    ipointer = ipointer + 1
    
mkcapTickerlist = df2.loc[:,"Ticker"].to_list()
mkcaplist = df2.loc[:,"Market Cap"].to_list()
ipointer = 0
while ipointer < len(mkcapTickerlist):
    newDir = os.path.join(os.getcwd(),mkcaplist[ipointer])
    if os.path.isdir(newDir) is not True:
        os.mkdir(newDir)
    getcsv = os.path.join(os.getcwd(),mkcapTickerlist[ipointer]+".csv")
    if os.path.exists(getcsv) is not True:
        ipointer = ipointer + 1
        continue
    shutil.copy(getcsv,newDir)
    ipointer = ipointer + 1
    
