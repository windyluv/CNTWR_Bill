import pandas as pd
import os
from func_lib import *
pd.options.display.max_columns = None
org_dir_dx = r'D:\onedirve\OneDrive\桌面\org_bill\塔类产品服务费结算详单-合肥市-电信-20210.xlsx'
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
    root=os.getcwd()
    discount_error_path=['塔类折扣不一致清单','机房折扣不一致清单','配套折扣不一致清单','维护费折扣不一致清单','场地费折扣不一致清单']
    print(u'任务启动')
    dx_clean_bill=bill_clean(datas_root[0])
    dx_tower_error_site=tower_shape_consistency_test(dx_clean_bill)
    discount_errors_list=discount_error_rules(dx_clean_bill)
    dx_tower_error_site.to_excel(os.path.join(root,'塔型不一致清单.xlsx'))
    for i in range(len(discount_errors_list)):
        discount_error = discount_errors_list[i]
        discount_error.to_excel(os.path.join(root,discount_error_path[i]+'.xlsx'),index=False)







    # for i in range(3):
    #     bills.append(bill_clean(datas_root[i]))
    #     print('{} ok '.format(i))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
