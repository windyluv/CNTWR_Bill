import pandas as pd
import numpy as np
import os.path as osp
root=r''
data_org=pd.read_excel(root,converters={"站址编码":str,"订单号":str})
data_org_dx=data_org[data_org.iloc[:,1]=='电信']
data_org_yd=data_org[data_org.iloc[:,1]=='移动']
data_org_lt=data_org[data_org.iloc[:,1]=='联通']

data=[data_org_dx,data_org_yd,data_org_lt]
opt_path=[]
for i in range(3):
    a=pd.pivot_table(data[i],index=['站址编码','站址产权属性'])
    b=a.iloc[:,[0,1]]
    b.to_excel(opt_path[i])
