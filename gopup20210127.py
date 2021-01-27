#要记得安装pip install tqdm
# TOKEN：62636bf2aa894a264857b50e82f35c11 
"""
#以下为微博指数
import gopup as gp
df_index = gp.weibo_index(word="疫情", time_type="3month")
print(df_index)

#以下为百度指数
import gopup as gp
cookie = "此处输入您在网页端登录百度指数后的 cookie 数据"
index_df = gp.baidu_search_index(word="口罩", start_date='2020-01-01', end_date='2020-03-01', cookie=cookie)
print(index_df)



#以下为算数指数
import gopup as gp
index_df = gp.toutiao_index(keyword="口罩", start_date='20201016', end_date='20201022', app_name='aweme')
print(index_df)



#以下为获取货币汇率数据
import gopup as gp
g = gp.pro_api(token = "……")
df_index = g.exchange_rate(date="2020-10-10", currency="美元")
print(df_index)

#以下为特许经营许可
import gopup as gp
df_index = gp.franchise_china()
print(df_index)
#txjy=df_index
#txjx.to_csv('txjy.csv')
df_index.to_csv('txjy.csv')

#以下为获取CPI
import gopup as gp
df_index = gp.get_cpi()
print(df_index)
df_index.to_csv('cpi.csv')


#独角兽公司数据
import gopup as gp
df_index = gp.nicorn_company()
print(df_index)
df_index.to_csv('djs.csv')

#以下为湖北省人口迁入与迁出情况
import gopup as gp
migration_area_baidu_df = gp.migration_area_baidu(area="湖北省", indicator="move_in", date="20200201")
print(migration_area_baidu_df)

#以下为全国高校名单 
import gopup as gp
df_index = gp.university()
print(df_index)
df_index.to_csv('全国高校名单.csv')


#全国高校详细信息，为北大为例
import gopup as gp
g = gp.pro_api(token = "62636bf2aa894a264857b50e82f35c11")
df_index = g.details_university(name="北京大学")
print(df_index)


#艺人流量价值
import gopup as gp
df_index = gp.realtime_artist_flow()
print(df_index)
"""



#艺人商业价值
import gopup as gp
df_index = gp.realtime_artist()
print(df_index)