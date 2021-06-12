import pandas as pd
import datetime
import os
import numpy as np
t0=datetime.datetime.now()
#Expected 原始账单; Return:分析报告及字典文件
def bill_report(data):
    site_total_num = data['站址编码'].nunique()  # 站址总数量（不区分非标）
    credit_term = data['账期月份'][0]  # 当前账期
    order_total_num = data['需求确认单编号'].nunique()  # 订单总数量
    income_monthly = data['产品服务费合计\n（出账费用）（不含税）'].sum() # 当月产生金额
    income_history_adjust = data['产品服务费合计（历史调增/已抵扣费用）（不含税）'].sum()  # 历史调整金额
    income_total = data[data['运营商']=='电信']['产品服务费合计（出账费用+历史调增/已抵扣费用）（不含税）'].sum() # 当月应出账金额
    income_tower = data['期末铁塔共享后基准价格1+2+3（出账费用）'].sum()
    income_power_room = data['期末机房共享后基准价格1+2+3（出账费用）'].sum()
    income_supply = data['配套共享后基准价格1+2+3（出账费用）'].sum()
    income_repair = data['维护费折扣后金额1+2+3（出账费用）'].sum()
    income_rent = data['场地费折扣后金额（出账费用）'].sum()
    income_eletricity = data['电力引入费折扣后金额（出账费用）'].sum()
    order_standard_num = data[data['业务属性'] == '塔']['需求确认单编号'].nunique()  # 塔类订单总数量
    order_non_standard_num = data[data['业务属性'] == '非标类']['需求确认单编号'].nunique()  # 非标类订单总数量
    order_standard_income = data[data['业务属性'] == '塔']['产品服务费合计（出账费用+历史调增/已抵扣费用）（不含税）'].sum()  # 塔类订单总收入
    order_non_standard_income = data[data['业务属性'] == '非标类']['产品服务费合计（出账费用+历史调增/已抵扣费用）（不含税）'].sum()  # 非标订单总收入
    income_per_site_total = round(income_monthly / site_total_num, 2)
    income_per_site_tower = round(income_tower / site_total_num, 2)
    income_per_site_power_room = round(income_power_room / site_total_num, 2)
    income_per_site_supply = round(income_supply / site_total_num, 2)
    income_per_site_repair = round(income_repair / site_total_num, 2)
    income_per_site_rent = round(income_rent / site_total_num, 2)
    income_per_site_eletricity = round(income_eletricity / site_total_num, 2)

    site_total_alone_num = data[(data['场地费当前共享折扣'] == 1) & (data['场地费'] > 0)]['站址编码'].nunique()#独享站址总数
    site_total_own_num = data[data['产权属性'] == '自建']['站址编码'].nunique()#自建站址数
    site_total_buy_num = data[data['产权属性'] == '注入']['站址编码'].nunique()#注入站址数
    site_total_own_alone_num = data[(data['场地费当前共享折扣'] == 1) & (data['场地费'] > 0) & (data['产权属性'] == '自建')]['站址编码'].nunique()#自建独享站址总数
    site_total_buy_alone_num = data[(data['场地费当前共享折扣'] == 1) & (data['场地费'] > 0) & (data['产权属性'] == '注入')]['站址编码'].nunique()#注入独享站址总数
    percent_of_shared_site_all = round(1 - (site_total_alone_num / site_total_num), 4)#共享站比例
    percent_of_shared_site_own = round(1 - (site_total_own_alone_num / site_total_own_num), 4)#自建共享站比例
    percent_of_shared_site_buy = round(1 - (site_total_buy_alone_num / site_total_buy_num), 4)#注入共享站比例
    report={'账期月份':str(credit_term),'产品服务费合计（出账费用）（不含税）':round(income_monthly,2),'产品服务费合计（历史调增/已抵扣费用）（不含税）':round(income_history_adjust,2),
            '产品服务费合计（出账费用+历史调增/已抵扣费用）（不含税）':round(income_total,2),
            '订单总数量':order_total_num,'塔类订单数量':order_standard_num,'塔类订单出账总金额':order_standard_income,'场地费出账总金额':income_rent,
            '非标订单数量':order_non_standard_num,'非标订单出账总金额':order_non_standard_income,
            '站址总数量':site_total_num,'总站址共享比例':percent_of_shared_site_all,'新建站共享比例':percent_of_shared_site_own,'注入站共享比例':percent_of_shared_site_buy,
            '站均出账金额':income_per_site_total,'站均铁塔出账':income_per_site_tower,'站均机房出账':income_per_site_power_room,
            '站均配套出账':income_per_site_supply,'站均维护费出账':income_per_site_repair,'站均场地费出账':income_per_site_rent,'站均电力引入费出账':income_per_site_eletricity}

    print('{}账期，电信方向出账分析概览如下：'.format(credit_term))
    print('出账总金额：{}万元，当月历史调整金额:{}万元，当月实际出账费用:{}万元'.
          format(round(income_monthly/10000,3), round(income_history_adjust/10000,3), round(income_total/10000,3)))
    print('出账订单合计{}条，其中塔类订单{}条，非标类订单{}条'.
          format(order_total_num, order_standard_num, order_non_standard_num))
    print('塔类订单合计出账：{}万元，非标类订单合计出账：{}万元，场地费合计出账：{}万元'.
          format(round(order_standard_income / 10000, 2), round(order_non_standard_income / 10000, 2),round(income_rent/10000,2)))
    print('出账站址共{}处,站均出账{}元。其中塔租站均{}元，机房站均{}元，配套站均{}元，维护费站均{}元，场租站均{}元，电力引入费站均{}元'.
          format(site_total_num, income_per_site_total, income_per_site_tower, income_per_site_power_room,income_per_site_supply,income_per_site_repair, income_per_site_rent, income_per_site_eletricity))
    print('出账站址共{}处，共享率为{}%'.format(site_total_num, round(percent_of_shared_site_all * 100,2)))
    print('出账注入站站址共{}处，共享率为{}%'.format(site_total_buy_num, round(percent_of_shared_site_buy*100,2)))
    print('出账新建站站址共{}处，共享率为{}%'.format(site_total_own_num, round(percent_of_shared_site_own*100,2)))
    return [report]

#Expected：原始账单; Return:精简账单
def bill_clean(bill_path):
    bill=pd.read_excel(bill_path,converters={"站址编码":str,"需求确认单编号":str})
    drop_index1 = [i for i in range(3, 6)] + [i for i in range(13, 26)]\
                +[i for i in range(74,78)]+[i for i in range(110, 122)]\
                + [i for i in range(127,133)] + [i for i in range(134, 143)]\
                + [i for i in range(147, 155)]
    tmp_bill = bill.drop(bill.columns[drop_index1], axis=1)
    idx=tmp_bill.columns.tolist()
    idx.insert(10,'产品单元数')
    idx.insert(26,'铁塔基准价格')
    idx.insert(39,'机房基准价格')
    idx.insert(52,'配套基准价格')
    idx.insert(65,'维护费')
    tmp_bill=tmp_bill.reindex(columns=idx)
    tmp_bill=tmp_bill.fillna(0)
    tmp_bill['产品单元数']=tmp_bill['产品单元数1']+tmp_bill['产品单元数2']+tmp_bill['产品单元数3']
    tmp_bill['铁塔基准价格']=tmp_bill['对应铁塔基准价格1']+tmp_bill['对应铁塔基准价格2']+tmp_bill['对应铁塔基准价格3']
    tmp_bill['机房基准价格']=tmp_bill['对应机房基准价格1']+tmp_bill['对应机房基准价格2']+tmp_bill['对应机房基准价格3']
    tmp_bill['配套基准价格']=tmp_bill['对应配套基准价格1']+tmp_bill['对应配套基准价格2']+tmp_bill['对应配套基准价格3']
    tmp_bill['维护费']=tmp_bill['对应维护费1']+tmp_bill['对应维护费2']+tmp_bill['对应维护费3']
    drop_index2=[i for i in range(11,26)]+[i for i in range(36,39)]+[i for i in range(49,52)]+[i for i in range(62,65)]
    clean_bill = tmp_bill.drop(tmp_bill.columns[drop_index2], axis=1)
    return clean_bill
#Expected：精简账单; Return:场租账单
def rent_verify(clean_bill):
    #场地费模式不一致；同站址不同塔型；同站址不同配套；场地费未按折扣出账；
    rent_bill = pd.pivot_table(clean_bill, index=['站址编码','需求确认单编号'],
                       columns=['账期月份'],values=['场地费', '场地费当前共享折扣', '场地费折扣后金额（出账费用）'],
                       aggfunc={'场地费': np.sum, '场地费折扣后金额（出账费用）': np.sum, '场地费当前共享折扣': np.mean},fill_value=0)
    return rent_bill



#Expected：相邻月份账单;   Return：异常数据（变动数据）
#def outliers_export(bill_ex,bill_now):
    #变动数据提取
    #异常数据提取 ||  未按折扣出账  出账金额不在正常区间内



















#
# def data_loader(root_dir):
#     _=os.listdir(root_dir)
#     datas=[]
#     percent_of_share_sites={}
#     t0=datetime.datetime.now()
#     for _ in _:
#         datas.append(os.path.join(root_dir,_))
#     for data in datas:
#         t1 = datetime.datetime.now()
#         _ = data.split('-')[-1].split('.')[0]#账期
#         dataframe=pd.read_excel(data,sheet_name=_)
#         percent_of_share_site=percent_of_shared_site(dataframe)
#         percent_of_share_sites.update({_:str(percent_of_share_site*100)+'%'})
#         print(percent_of_share_sites)
#         print('{}账期共享率为{}%，计算耗时{}'.format(_,percent_of_share_site * 100,datetime.datetime.now()-t1))
#     return percent_of_share_sites
