class standard_tower():
    def __init__(self,data):
        self.order=data['需求确认单编号']                            #订单编号
        self.site_code=data['站址编码']                             #站址编码
        self.property=data['产权属性']                              #产权属性
        self.tower_type=data['产品类型']                            #塔型
        self.antenna_height=data['对应实际最高天线挂高（米）1']        #天线挂高
        self.tower_discount=data['铁塔当前共享折扣']                 #塔共享折扣
        self.unit=data['产品单元数1']                               #产品单元
