import pandas as pd
import os
from func_lib import *
pd.options.display.max_columns = None
org_dir_dx = r'D:\onedirve\OneDrive\桌面\org_bill\塔类产品服务费结算详单-合肥市-电信-202105.xlsx'
org_dir_yd = r'D:\onedirve\OneDrive\桌面\org_bill\塔类产品服务费结算详单-合肥市-移动-202105.xlsx'
org_dir_lt = r'D:\onedirve\OneDrive\桌面\org_bill\塔类产品服务费结算详单-合肥市-联通-202105.xlsx'
org_dir_all= r'D:\onedirve\OneDrive\桌面\org_bill\塔类产品服务费结算详单-合肥市-202105.xlsx'
save_path_dx = r'D:\onedirve\OneDrive\桌面\dx_clean_2105.xlsx'
save_path_yd = r'D:\onedirve\OneDrive\桌面\yd_clean_2105.xlsx'
save_path_lt = r'D:\onedirve\OneDrive\桌面\lt_clean_2105.xlsx'
datas_root=[org_dir_dx,org_dir_yd,org_dir_lt]
save_path=[save_path_dx,save_path_yd,save_path_lt]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bills=[]
    print(u'任务启动')
    for i in range(3):
        bill_clean(datas_root[i]).to_excel(save_path[i],index=False)
        print('{} ok '.format(i))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
