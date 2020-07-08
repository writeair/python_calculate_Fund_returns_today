# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:06:16 2020
3
@author: 48572
"""
import requests
import json
import re
def getUrl(fscode):
  head = 'http://fundgz.1234567.com.cn/js/'
  tail = '.js?rt=1463558676006'
  print(head+fscode+tail)
  return head+fscode+tail
# 根据基金代码获取净值
def getWorth(fscode):  
    content = requests.get(getUrl(fscode))
    cont = re.findall('\{.+\}', content.text)[0]  # 提取list
    jsonObj=json.loads(cont)
    name = jsonObj.get('name')
    code = jsonObj.get('fundcode')
    yes_price =jsonObj.get('dwjz')
    gs_price =jsonObj.get('gsz')
    gs_zf =jsonObj.get('gszzl')
    return name,yes_price,gs_price,gs_zf
allCode =["000404","003096","002851","001837","161725","000751","166002","161122"]                     # 基金的代码 
share =  {'000404':'100.66','003096':'183.66','002851':'6.56','001837':'6.50','161725':'13.22','000751':'2.95','166002':'229.50','161122':'85.27'}   # 持有基金所对应的份额
netWorthFile = open('./netWorth.csv','w')
gs_Sumprofit=0
for code in allCode:
  try:
    name,yes_price,gs_price,gs_zf = getWorth(code)
  except:
    continue
  gs_profit=round((float(gs_price)-float(yes_price))*float(share.get(code)), 2)
  gs_Sumprofit=gs_profit+gs_Sumprofit
  print(code,name,"昨日净值："+yes_price,"估算值："+gs_price,"估算涨幅："+gs_zf+"%","估算收益："+str(gs_profit)+"元") 
  netWorthFile.write("\'"+code+"\',")  
  netWorthFile.write(name+","+yes_price+","+gs_price+","+gs_zf+","+str(gs_profit))
  netWorthFile.write("\n")
  #print("write "+code+"'s data success.")
print("今日估算收益（150）："+str(gs_Sumprofit)+"元")
allCode =["161725","217027","009549","000751","001548","162712"]                     # 基金的代码 
share =  {'161725':'7.73','217027':'42.28','009549':'216','000751':'45.25','001548':'149.75','162712':'6.97'}   # 持有基金所对应的份额

gs_Sumprofit1=0
for code in allCode:
  try:
    name,yes_price,gs_price,gs_zf = getWorth(code)
  except:
    continue
  gs_profit=round((float(gs_price)-float(yes_price))*float(share.get(code)), 2)
  gs_Sumprofit1=gs_profit+gs_Sumprofit1
  print(code,name,"昨日净值："+yes_price,"估算值："+gs_price,"估算涨幅："+gs_zf+"%","估算收益："+str(gs_profit)+"元") 
  netWorthFile.write("\'"+code+"\',")  
  netWorthFile.write(name+","+yes_price+","+gs_price+","+gs_zf+","+str(gs_profit))
  netWorthFile.write("\n")
 # print("write "+code+"'s data success.")
print("今日估算收益（159）："+str(gs_Sumprofit1)+"元")
print("今日估算总收益："+str(gs_Sumprofit+gs_Sumprofit1)+"元")
netWorthFile.close()